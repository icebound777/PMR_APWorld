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
from NetUtils import (
    ClientStatus,
    NetworkItem,
)
import Patch
from settings import get_settings
import Utils

# run archipelago's module update to fetch emu_loader via requirements.txt
import ModuleUpdate
ModuleUpdate.update()
# For when its a global package
try:
    from emu_loader import EmuLoaderClient
# For when its in the apworld itself
except ImportError:
    from .emu_loader import EmuLoaderClient

from .client_common import (
    get_new_autohints,
    get_newly_checked_item_locations,
    get_receive_items_list,
)
from .data.data import (
    AREA_ADDRESS,
    GAME_MODE_WORLD,
    GF_START_ADDRESS,
    GOAL_FLAG,
    ITM_RCV_SEQ,
    KEY_RECV_BUFFER,
    MAGIC_VALUE,
    MAP_ADDRESS,
    MF_START_ADDRESS,
    MODE_ADDRESS,
    SIGNATURE_OFFSET_PROD,
    STAR_SPIRITS_COUNT,
    UIR_START_ADDRESS,
    get_flag_value,
    item_table,
)


SIGNATURE_OFFSET = SIGNATURE_OFFSET_PROD


class PaperMarioEmuLoaderClient(EmuLoaderClient):

    def __init__(self) -> None:
        #logger.info("Attempting to init EmuLoader")
        super().__init__(
            signature_offset=SIGNATURE_OFFSET,
            signature_value=MAGIC_VALUE,
            pull_from_web=True,
        )


def rom_is_ready_for_communication(client: EmuLoaderClient) -> bool:
    # The randomized ROM is only considered ready while the rando-specific
    # magic value is present
    try:
        rando_magic_value = client.read_u32(SIGNATURE_OFFSET + 0x80000000)

        return rando_magic_value == MAGIC_VALUE
    except Exception:
        return False


class PaperMarioGameState():
    """
    Game-specific game state tracking.
    """
    local_checked_locations: Set[int]
    autohint_stored: Set[int]
    autohint_released: Set[int]
    current_area_id: Optional[int]
    current_map_id: Optional[int]

    def __init__(self):
        self.local_checked_locations = set()
        self.autohint_stored = set()
        self.autohint_released = set()
        self.current_area_id = 1 # Toad Town
        self.current_map_id = 0 # Debug Room


class PaperMarioContext(CommonContext):
    #command_processor
    items_handling = 0b101
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

    def already_running(self) -> bool:
        try:
            import ctypes

            mutex = ctypes.windll.kernel32.CreateMutexW(None, 1, "PM64_GUI_MUTEX")
            return ctypes.GetLastError() == 183 # ERROR_ALREADY_EXISTS
        except Exception:
            return False

    def run_gui(self):
        if self.already_running():
            sys.exit(1)
        from kvui import GameManager #, Window

        #Window.bind(on_request_close=self.on_request_close)
        #asyncio.create_task(patch_and_run(True))

        class PaperMarioManager(GameManager):
            ctx: PaperMarioContext
            logging_pairs = [("Client", "Archipelago")]
            base_title = "Paper Mario Client (0.7.0) for AP"

            def build(self):
                return super().build()

        self.ui = PaperMarioManager(self)
        self.ui_task = asyncio.create_task(self.ui.async_run(), name="UI")

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

        #logger.info("EmuLoader init'd, waiting for emulator connection and valid game state")
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
    """
    The game_watcher is the per tick game logic.
    Here we check if it's save to read and write data (by checking for the
    game mode), and if so we bounce tracker data, receive and send items,
    handle auto-hints, and check if the player has reached their goal.
    """
    def read_list_u8(client: PaperMarioEmuLoaderClient, address: int, count: int = 1) -> List[int]:
        u8_list: List[int] = []

        for i in range(count):
            u8_list.append(client.read_u8(address + 0x80000000 + i))

        return u8_list

    def write_list_u16(client: PaperMarioEmuLoaderClient, address: int, u16_list: List[int]):
        # we write the list back-to-front, as this function is only used for receiving items,
        # and the receiving items array in the game's RAM is guaranteed to be empty.
        # Since the trigger for ROM to start working through the list is list[0] being
        # non-zero, we write that specific u16 last
        enumerated_u16_list = list(enumerate(u16_list))
        enumerated_u16_list.reverse()
        for i, u16_val in enumerated_u16_list:
            #print(f"Writing {hex(u16_val)} to {hex(address + 0x80000000 + (2*i))}")
            client.write_u16(address + 0x80000000 + (2*i), u16_val)


    client = ctx.emu_loader

    #print("CHECK OVERWORLD STATE")
    # check for current state before sending or receiving anything
    game_mode = client.read_u8(MODE_ADDRESS + 0x80000000)
    if game_mode != GAME_MODE_WORLD:
        # We're not in an "overworld" game state: don't read or write data
        #logger.info(f"we're not in an overworld state: {game_mode=}")
        return

    # BOUNCE TRACKER DATA
    #print("BOUNCE TRACKER DATA")
    current_location = (
        client.read_u8(AREA_ADDRESS + 0x80000000), # current_area_id
        client.read_u8(MAP_ADDRESS + 0x80000000),  # current_map_id
    )

    if (   ctx.pm_game_state.current_area_id != current_location[0]
        or ctx.pm_game_state.current_map_id != current_location[1]
    ):
        ctx.pm_game_state.current_area_id = current_location[0]
        ctx.pm_game_state.current_map_id = current_location[1]

        await ctx.send_msgs([{
            "cmd": "Bounce",
            "slots": [ctx.slot],
            "data": {
                "type": "MapUpdate",
                "areaId": ctx.pm_game_state.current_area_id,
                "mapId": ctx.pm_game_state.current_map_id,
            },
        }])


    # READ UNIQUE ITEM REGISTRY
    #print("READ UNIQUE ITEM REGISTRY")
    uir_flags: list = read_list_u8(client, UIR_START_ADDRESS, len(item_table))


    # RECEIVE ITEMS
    #print("RECEIVE ITEMS")
    can_receive_items = client.read_u16(KEY_RECV_BUFFER + 0x80000000) == 0
    if can_receive_items:
        # Add item(s) to buffer as u16 int(s)
        received_items = client.read_u16(ITM_RCV_SEQ + 0x80000000)

        if received_items < len(ctx.items_received):
            new_items_ids = get_receive_items_list(
                ctx = ctx,
                count_received_items = received_items,
                uir_flags = uir_flags,
            )

            write_list_u16(client, KEY_RECV_BUFFER, new_items_ids)


    # SEND ITEMS
    #print("SEND ITEMS")
    mf_bytes = bytearray(read_list_u8(client, MF_START_ADDRESS, 0x224))
    gf_bytes = bytearray(read_list_u8(client, GF_START_ADDRESS, 0x107))
    locs_to_send: Set[int] = get_newly_checked_item_locations(
        ctx = ctx,
        modflag_bytes = mf_bytes,
        gameflag_bytes = gf_bytes,
    )

    # Send locations if there are any to send
    if locs_to_send != ctx.pm_game_state.local_checked_locations:
        ctx.pm_game_state.local_checked_locations = locs_to_send

        if locs_to_send is not None:
            await ctx.check_locations(list(locs_to_send))


    # AUTO HINTING
    # Build list of items to scout
    star_spirits = client.read_u8(STAR_SPIRITS_COUNT + 0x80000000)
    hints: List[int] = get_new_autohints(
        ctx = ctx,
        current_location = current_location,
        current_star_spirits = star_spirits,
        already_handled_autohints = ctx.pm_game_state.autohint_released.union(
            ctx.pm_game_state.autohint_stored
        ),
    )

    # scout the auto hint locations in the current map and store
    # what we have scouted but not hinted
    if hints:
        await ctx.send_msgs([{
            "cmd": "LocationScouts",
            "locations": hints,
            "create_as_hint": 0,
        }])
        ctx.pm_game_state.autohint_stored = set(hints)

    # send the hints for the unsent progression items in the stored
    # locations
    # these will have already been scouted
    if ctx.pm_game_state.autohint_stored:
        await ctx.send_msgs([{
            "cmd": "LocationScouts",
            "locations": [
                loc
                for loc, n_item in ctx.locations_info.items()
                if n_item.flags & 0b001
            ],
            "create_as_hint": 2,
        }])
        ctx.pm_game_state.autohint_released.update(ctx.pm_game_state.autohint_stored)
        ctx.pm_game_state.autohint_stored = set()


    # GOAL CHECKING
    if not ctx.finished_game and (get_flag_value(GOAL_FLAG, mf_bytes)):
        await ctx.send_msgs([{
            "cmd": "StatusUpdate",
            "status": ClientStatus.CLIENT_GOAL
        }])


def _patch_game(patch_file: str) -> Patch.RomMeta | None:
    """
    Patches the ROM
    """
    try:
        metadata, _ = Patch.create_rom_file(patch_file)
        #Utils.async_start(_run_game(output_file))
        return metadata
    except Exception as exc:
        logger.exception(exc)
        Utils.messagebox("Error Patching Game", str(exc), True)
        return None


def main(*launch_args: str):
    """
    Entry-point for the Paper Mario Client that's based on emu_loader.
    Patches the ROM if required, then waits for a valid randomized PMR ROM
    to be found in any of the supported emulators.
    """
    Utils.init_logging("Paper Mario Client")
    parser = get_base_parser()
    parser.add_argument(
        "patch_file",
        default="",
        type=str,
        nargs="?",
        help="Path to an Archipelago patch file"
    )
    args = launch_args
    if "Paper Mario Client" in args:
        args.remove("Paper Mario Client")
    args = parser.parse_args(args)

    if args.patch_file != "":
        metadata = _patch_game(args.patch_file)
        if metadata is not None and "server" in metadata:
            args.connect = metadata["server"]
        if not get_settings().paper_mario_settings.client_start:
            # If the client_start setting is turned off (meaning the user
            # does _not_ want to use the PMClient but rather the generic
            # bizhawk one), and we're currently in the `Open Patch` context,
            # then abort here after patching.
            return

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
