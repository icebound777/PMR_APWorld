from typing import TYPE_CHECKING, Set, Optional, Tuple, List, Dict
import base64

from NetUtils import ClientStatus, NetworkItem
import worlds._bizhawk as bizhawk
from worlds._bizhawk.client import BizHawkClient

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
    STAR_SPIRITS_COUNT,
    UIR_START_ADDRESS,
    get_flag_value,
    item_table,
)

if TYPE_CHECKING:
    from worlds._bizhawk.context import BizHawkClientContext


class PaperMarioClient(BizHawkClient):
    game = "Paper Mario"
    system = "N64"
    # patch_suffix = ".appm64" # gen bizhawk not as priority client for this apworld
    local_checked_locations: Set[int]

    current_area_id: Optional[int]
    current_map_id: Optional[int]

    def __init__(self) -> None:
        super().__init__()
        self.local_checked_locations = set()
        self.autohint_stored = set()
        self.autohint_released = set()
        self.current_area_id = 1 # Toad Town
        self.current_map_id = 0 # Debug Room

    async def validate_rom(self, ctx: "BizHawkClientContext") -> bool:
        from CommonClient import logger

        try:
            # Check ROM name/patch version
            game_name = await bizhawk.read(ctx.bizhawk_ctx, [(0x20, 0x14, "ROM")])
            if game_name[0].decode("ascii") != "PAPER MARIO         ":
                return False

            pmr_magic_value = await bizhawk.read(
                ctx.bizhawk_ctx,
                [(TABLE_ADDRESS, 0x4, "ROM")]
            )
            if (    pmr_magic_value[0] != MAGIC_VALUE
                and pmr_magic_value[0] != MAGIC_VALUE.to_bytes(4, "big")
            ):
                logger.info(f"This Paper Mario ROM is invalid. {hex(pmr_magic_value[0])}")
                return False

        except UnicodeDecodeError:
            return False
        except bizhawk.RequestFailedError:
            return False  # Should verify on the next pass

        ctx.game = self.game
        ctx.items_handling = 0b101  # get start inventory from server, do not get local items from server
        ctx.want_slot_data = True   # get slot data
        ctx.watcher_timeout = 1     # loop watcher every second
        return True

    async def set_auth(self, ctx: "BizHawkClientContext") -> None:
        auth_raw = (await bizhawk.read(
            ctx.bizhawk_ctx,
            [(AUTH_ADDRESS, 16, "ROM")]
        ))[0]
        ctx.auth = base64.b64encode(auth_raw).decode("utf-8")

    async def game_watcher(self, ctx: "BizHawkClientContext") -> None:
        from CommonClient import logger
        try:

            read_state = await bizhawk.read(
                ctx.bizhawk_ctx,
                [
                    (MODE_ADDRESS, 1, "RDRAM"),
                    (MF_START_ADDRESS, 0x224, "RDRAM"),
                    (GF_START_ADDRESS, 0x107, "RDRAM"),
                    (ITM_RCV_SEQ, 2, "RDRAM"),
                    (AREA_ADDRESS, 1, "RDRAM"),
                    (MAP_ADDRESS, 1, "RDRAM"),
                    (STAR_SPIRITS_COUNT, 1, "RDRAM"),
                    (UIR_START_ADDRESS, len(item_table), "RDRAM"),
                ]
            )

            # check for current state before sending or receiving anything
            game_mode = int.from_bytes(read_state[0], "big")

            if game_mode == GAME_MODE_WORLD:
                # Assign data read
                mod_flags = read_state[1]
                game_flags = read_state[2]
                received_items = int.from_bytes(bytearray(read_state[3]), "big")
                current_location = (
                    int.from_bytes(bytearray(read_state[4]), "big"),
                    int.from_bytes(bytearray(read_state[5]), "big"),
                )
                star_spirits = int.from_bytes(bytearray(read_state[6]), "big")
                uir_flags = read_state[7]

                # BOUNCE TRACKER DATA
                await self.handle_tracker_info(ctx, current_location)

                # RECEIVE ITEMS
                # Add item to buffer as u16 int
                if received_items < len(ctx.items_received):
                    new_items_ids = get_receive_items_list(
                        ctx = ctx,
                        count_received_items = received_items,
                        uir_flags = uir_flags,
                    )

                    # bizhawk wants the data to write as a byte array here,
                    # but `new_items_ids` is a list of halfwords.
                    new_items_ids_as_bytes: List[int] = []
                    for x in new_items_ids:
                        new_items_ids_as_bytes.append((x & 0xFF00) >> 8)
                        new_items_ids_as_bytes.append(x & 0xFF)

                    await bizhawk.guarded_write(
                        ctx.bizhawk_ctx,
                        [(KEY_RECV_BUFFER, new_items_ids_as_bytes, "RDRAM")],
                        [
                            (KEY_RECV_BUFFER, (0).to_bytes(4, "big"), "RDRAM"),
                            (ITM_RCV_SEQ, read_state[3], "RDRAM")
                        ])

                # SEND ITEMS
                mf_bytes = bytearray(mod_flags)
                gf_bytes = bytearray(game_flags)
                locs_to_send: Set[int] = get_newly_checked_item_locations(
                    ctx = ctx,
                    modflag_bytes = mf_bytes,
                    gameflag_bytes = gf_bytes,
                )

                # Send locations if there are any to send
                if locs_to_send != self.local_checked_locations:
                    self.local_checked_locations = locs_to_send

                    if locs_to_send is not None:
                        await ctx.send_msgs([{
                            "cmd": "LocationChecks",
                            "locations": list(locs_to_send)
                        }])

                # AUTO HINTING
                # Build list of items to scout
                hints: List[int] = get_new_autohints(
                    ctx = ctx,
                    current_location = current_location,
                    current_star_spirits = star_spirits,
                    already_handled_autohints = self.autohint_released.union(
                        self.autohint_stored
                    ),
                )

                # scout the auto hint locations in the current area and store
                # what we have scouted but not hinted
                if hints:
                    await ctx.send_msgs([{
                        "cmd": "LocationScouts",
                        "locations": hints,
                        "create_as_hint": 0,
                    }])
                    self.autohint_stored = hints

                # send the hints for the unsent progression items in the stored
                # locations
                # these will have already been scouted
                if self.autohint_stored:
                    await ctx.send_msgs([{
                        "cmd": "LocationScouts",
                        "locations": [
                            loc
                            for loc, n_item in ctx.locations_info.items()
                            if n_item.flags & 0b001
                        ],
                        "create_as_hint": 2,
                    }])
                    self.autohint_released.update(self.autohint_stored)
                    self.autohint_stored = hints

                # GOAL CHECKING
                if not ctx.finished_game and (get_flag_value(GOAL_FLAG, mf_bytes)):
                    await ctx.send_msgs([{
                        "cmd": "StatusUpdate",
                        "status": ClientStatus.CLIENT_GOAL
                    }])

        except bizhawk.RequestFailedError:
            # Exit handler and return to main loop to reconnect.
            pass


    async def handle_tracker_info(
        self,
        ctx: "BizHawkClientContext",
        current_location: Tuple[int, int]
    ):
        (current_area_id, current_map_id) = current_location

        if (   current_area_id != self.current_area_id
            or current_map_id != self.current_map_id
        ):
            self.current_area_id = current_area_id
            self.current_map_id = current_map_id

            await ctx.send_msgs([{
                "cmd": "Bounce",
                "slots": [ctx.slot],
                "data": {
                    "type": "MapUpdate",
                    "areaId": current_area_id,
                    "mapId": current_map_id,
                },
            }])
