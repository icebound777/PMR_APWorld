from typing import TYPE_CHECKING, Set, Optional, Tuple, List, Dict
import base64

from NetUtils import ClientStatus, NetworkItem
import worlds._bizhawk as bizhawk
from worlds._bizhawk.client import BizHawkClient
from .data.ItemList import item_multiples_ids
from .data.data import *
from .Locations import location_name_to_id
from .items import item_id_prefix
from .data.LocationsList import location_groups, location_table

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
                    new_items: List[NetworkItem] = ctx.items_received[received_items:]
                    if len(new_items) > MAX_ITEMS_RECEIVED_AT_ONCE:
                        new_items = new_items[:MAX_ITEMS_RECEIVED_AT_ONCE]

                    new_items_ids: List[int] = [x.item - item_id_prefix for x in new_items]

                    # Since we can have the exact same item id of "item_multiples_ids" items
                    # in the new_items_ids list, we have to keep track of the repeat_id
                    # of each of them. If didn't do this, we might add the same
                    # repeat-version of an item, leading to e.g. sending multiple
                    # "RuinsKeyA"s despite wanting to send one "RuinsKeyA",
                    # one "RuinsKeyB" and so on
                    same_item_in_received_items: Dict[int, int] = {}

                    for i, item_id in enumerate(new_items_ids):
                        # check what id actually needs sent to the game, as some
                        # items have multiples
                        # items in the player's game will have the biggest available
                        # ID, when receiving we give the smallest
                        if item_id in item_multiples_ids.keys():
                            if item_id in same_item_in_received_items:
                                repeat_id = same_item_in_received_items[item_id] + 1
                            else:
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
                                repeat_id += 1

                            # overwrite item id in list with adjusted id
                            same_item_in_received_items[item_id] = repeat_id
                            new_items_ids[i] = item_multiples_ids[base_item_id][repeat_id]

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
                locs_to_send = set()

                # check through the checks table for checked checks
                for location, data in checks_table.items():
                    loc_id = location_name_to_id[location]
                    loc_val = False

                    # these flags are weird and require a helper function to do
                    # funny math, refer to doc linked in data
                    if data[0] == "MF":
                        loc_val = get_flag_value(data[1], mf_bytes)
                    elif data[0] == "GF":
                        loc_val = get_flag_value(data[1], gf_bytes)

                    if loc_val and loc_id in ctx.server_locations:
                        locs_to_send.add(loc_id)

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
                hints = []
                for loc in location_groups["AutoHint"]:
                    if loc not in self.autohint_released.union(self.autohint_stored):
                        if current_location == (location_table[loc][2], location_table[loc][3]):
                            # don't hint Rowf items you can't see/buy yet
                            if (location_table[loc][2], location_table[loc][3]) == (1, 2):
                                # grab the set number from the location name
                                rowf_set = int(loc[len("TT Plaza District Rowf's Shop Set ")])
                                if rowf_set <= star_spirits + 1:
                                    hints.append(loc)
                            else:
                                hints.append(loc)

                # make sure we aren't scouting anything that's already been checked
                hints = [location_name_to_id[loc] for loc in hints if
                         location_name_to_id[loc] in ctx.missing_locations and
                         location_name_to_id[loc] not in ctx.locations_checked]

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
