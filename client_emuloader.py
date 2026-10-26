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
                #await game_watcher(ctx)
                None

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
