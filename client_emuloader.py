import asyncio
import multiprocessing
import sys
from typing import TYPE_CHECKING, Optional, List, Set, Any, Dict

from CommonClient import (
    CommonContext,
    get_base_parser,
    gui_enabled,
    logger,
)
import Utils

from emu_loader import EmuLoaderClient

from .data.data import *
from .data.ItemList import item_multiples_ids
from .Locations import location_name_to_id
from .items import item_id_prefix

if TYPE_CHECKING:
    from kvui import UILog


class PaperMarioEmuLoaderClient(EmuLoaderClient):

    def __init__(self) -> None:
        logger.info("Attempting to init EmuLoader")
        super().__init__(
            signature_offset=0x4770A0,
            signature_value=MAGIC_VALUE,
            pull_from_web=False,
        )


def rom_is_ready_for_communication(client: EmuLoaderClient) -> bool:
    # The randomized ROM is only considered ready while the rando-specific
    # magic value is present
    try:
        rando_magic_value = client.read_u32(0x4770A0 + 0x80000000)

        return rando_magic_value == MAGIC_VALUE
    except Exception:
        return False


class PaperMarioGameState():
    local_checked_locations: Set[int]
    current_area_id: Optional[int]
    current_map_id: Optional[int]

    def __init__(self):
        self.local_checked_locations = set()
        self.current_area_id = 1 # Toad Town
        self.current_map_id = 0 # Debug Room


class PaperMarioContext(CommonContext):
    #command_processor
    items_handling = 0b111
    want_slot_data = True
    slot_data: Dict[str, Any] | None = None
    #tab_items

    pm_game_state: Optional[PaperMarioGameState]

    def __init__(self, server_address: str | None, password: str | None):
        super().__init__(server_address, password)
        self.game = "Paper Mario"
        self.emu_loader: PaperMarioEmuLoaderClient | None = None
        self.emu_monitor_task: asyncio.Task | None = None
        self.emu_status: str = "Not attached"

        self.slot_data = {}
        self.pm_game_state = None

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super(PaperMarioContext, self).server_auth(password_requested)
        if not self.auth:
            await self.get_username()
            await self.send_connect()

    def on_package(self, cmd, args):
        if cmd == "Connected":
            self.slot_data = args.get("slot_data")

#    def run_gui(self):
#        from kvui import GameManager, Window, UILog
#
#        Window.bind(on_request_close=self.on_request_close)
#        asyncio.create_task(patch_and_run(True))
#
#        class PaperMarioManager(GameManager):
#            ctx: PaperMarioContext
#            logging_pairs = [("Client", "Archipelago")]
#            base_title = "Paper Mario Client for AP"
#
#            def build(self):
#                return super().build()
#
#        self.ui = PaperMarioManager(self)
#        self.ui_task = asyncio.create_task(self.ui.async_run(), name="UI")

#    def on_request_close(self, *args: Any) -> bool:
#        from kvui import MessageBox
#
#        title = "Warning: Autostart program still running!"
#        message = "Attempting to close this window again will forcibly close it."
#        def cleanup():
#            self._messagebox = None
#        if self._messagebox and self._messagebox.title == title:
#            return False
#        if program and program.poll() is None:
#            self.gui_error(title, message)
#            if self._messagebox:
#                self._messagebox.bind(on_dismiss=cleanup)
#            return True
#        return False


async def emu_loader_monitor_task(ctx: PaperMarioContext):
    poll_interval = 1.0

    while not ctx.exit_event.is_set():
        ctx.emu_status = "Waiting for Emulator"
        ctx.emu_loader = PaperMarioEmuLoaderClient()
        ctx.pm_game_state = PaperMarioGameState()

        logger.info("EmuLoader init'd, waiting for emulator connection and valid game state")
        await ctx.emu_loader.wait_for_emulator(validate=rom_is_ready_for_communication)

        if ctx.exit_event.is_set():
            return

        emu_name = ctx.emu_loader.emulator_info.id
        ctx.emu_status = f"Connected to {emu_name}."

        while not ctx.exit_event.is_set():
            try:
                # per tick game logic here
                #logger.info("<game loop tick>")
                await game_watcher(ctx)

            except Exception as e:
                print("Paper Mario Connector lost its connection; reconnecting...")
                print(e)
                ctx.emu_status = "Lost emulator connection; reconnecting..."
                try:
                    if ctx.emu_loader is not None:
                        ctx.emu_loader.disconnect()
                except Exception:
                    pass
                ctx.emu_loader = None
                await asyncio.sleep(1)
                break

            try:
                await asyncio.wait_for(ctx.exit_event.wait(), timeout=poll_interval)
                return
            except asyncio.TimeoutError:
                pass


async def game_watcher(ctx: PaperMarioContext):
    def read_list_u8(client: PaperMarioEmuLoaderClient, address: int, count: int = 1) -> List[int]:
        u8_list: List[int] = []

        for i in range(count):
            u8_list.append(client.read_u8(address + 0x80000000 + i))

        return u8_list


    client = ctx.emu_loader

    print("CHECK OVERWORLD STATE")
    # check for current state before sending or receiving anything
    game_mode = client.read_u8(MODE_ADDRESS + 0x80000000)
    if game_mode != GAME_MODE_WORLD:
        # We're not in an "overworld" game state: don't read or write data
        #logger.info(f"we're not in an overworld state: {game_mode=}")
        return

    # BOUNCE TRACKER DATA
    print("BOUNCE TRACKER DATA")
    (current_area_id, current_map_id) = (
        client.read_u8(AREA_ADDRESS + 0x80000000),
        client.read_u8(MAP_ADDRESS + 0x80000000),
    )

    if (   ctx.pm_game_state.current_area_id != current_area_id
        or ctx.pm_game_state.current_map_id != current_map_id
    ):
        ctx.pm_game_state.current_area_id = current_area_id
        ctx.pm_game_state.current_map_id = current_map_id

        await ctx.send_msgs([{
            "cmd": "Bounce",
            "slots": [ctx.slot],
            "data": {
                "type": "MapUpdate",
                "areaId": current_area_id,
                "mapId": current_map_id,
            },
        }])


    # READ UNIQUE ITEM REGISTRY
    print("READ UNIQUE ITEM REGISTRY")
    uir_flags: list = read_list_u8(client, UIR_START_ADDRESS, len(item_table))


    # RECEIVE ITEMS
    print("RECEIVE ITEMS")
    # Add item(s) to buffer as u16 int(s)
    received_items = client.read_u16(ITM_RCV_SEQ + 0x80000000)
    #logger.info(f"{received_items=}")

    if received_items < len(ctx.items_received):
        can_receive_items = client.read_u16(KEY_RECV_BUFFER + 0x80000000) == 0

        if can_receive_items:
            print(f"{ctx.items_received=}")
            next_item = ctx.items_received[received_items]
            item_id = next_item.item - item_id_prefix
            if item_id in item_multiples_ids.keys():
                repeat_id = 0

                # magical seeds need to skip seed 1 if only 3 seeds
                # required, 1 and 2 if 2 seeds required, etc
                if item_id == item_table["Magical Seed"][2]:
                    repeat_id = min(
                        4 - ctx.slot_data["magical_seeds"],
                        3 # maximum of 3 in case command used
                    )

                base_item_id = item_id
                item_id = item_multiples_ids[base_item_id][repeat_id]
                while (    repeat_id < len(item_multiples_ids[base_item_id])
                        and uir_flags[item_id]
                ):
                    item_id = item_multiples_ids[base_item_id][repeat_id]
                    repeat_id += 1

            client.write_u16(KEY_RECV_BUFFER + 0x80000000, item_id)


    # SEND ITEMS
    print("SEND ITEMS")
    mf_bytes = bytearray(read_list_u8(client, MF_START_ADDRESS, 0x224))
    gf_bytes = bytearray(read_list_u8(client, GF_START_ADDRESS, 0x107))
    locs_to_send: Set[int] = set()

    # check through the checks table for checked checks
    for location, data in checks_table.items():
        loc_id = location_name_to_id[location]
        loc_is_checked = False

        # these flags are weird and require a helper function to do
        # funny math, refer to doc linked in data
        if data[0] == "MF":
            loc_is_checked = get_flag_value(data[1], mf_bytes)
        elif data[0] == "GF":
            loc_is_checked = get_flag_value(data[1], gf_bytes)

        if loc_is_checked and loc_id in ctx.server_locations:
            locs_to_send.add(loc_id)

    # Send locations if there are any to send
    if locs_to_send != ctx.pm_game_state.local_checked_locations:
        ctx.pm_game_state.local_checked_locations = locs_to_send

        if locs_to_send is not None:
            await ctx.send_msgs([{
                "cmd": "LocationChecks",
                "locations": list(locs_to_send)
            }])


def main():
    Utils.init_logging("Paper Mario Client")
    parser = get_base_parser()
    args = sys.argv[1:]  # the default for parse_args()
    if "Paper Mario Client" in args:
        args.remove("Paper Mario Client")
    args = parser.parse_args(args)

    async def _main():
        multiprocessing.freeze_support()

        ctx = PaperMarioContext(args.connect, args.password)
        ctx.emu_monitor_task = asyncio.create_task(
            emu_loader_monitor_task(ctx),
            name="EmuLoader Monitor"
        )

        if gui_enabled:
            ctx.run_gui() # self-defined ? todo
        ctx.run_cli() # inherited from CommonContext

        await ctx.exit_event.wait()
        ctx.server_address = None
        await ctx.shutdown()

        if ctx.emu_monitor_task:
            try:
                await asyncio.wait_for(ctx.emu_monitor_task, timeout=3.0)
            except (asyncio.TimeoutError, asyncio.CancelledError):
                pass
            if ctx.emu_loader is not None:
                try:
                    ctx.emu_loader.disconnect()
                except Exception:
                    pass

    import colorama
    colorama.init

    asyncio.run(_main())
    colorama.deinit()


if __name__ == "__main__":
    main()
