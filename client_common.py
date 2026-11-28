from typing import TYPE_CHECKING, NewType, List, Dict, Set, Tuple

from NetUtils import NetworkItem

from .data.data import (
    MAX_ITEMS_RECEIVED_AT_ONCE,
    get_flag_value,
    checks_table,
)
from .data.ItemList import item_multiples_ids, item_table
from .data.LocationsList import location_groups, location_table
from .items import item_id_prefix
from .Locations import location_name_to_id

if TYPE_CHECKING:
    from CommonClient import CommonContext

ItemID = NewType("ItemID", int)
LocationID = NewType("LocationID", int)


def get_receive_items_list(
    ctx: "CommonContext",
    count_received_items: int,
    uir_flags: List[int], # u8
) -> List[ItemID]:
    new_items: List[NetworkItem] = ctx.items_received[count_received_items:]
    if len(new_items) > MAX_ITEMS_RECEIVED_AT_ONCE:
        new_items = new_items[:MAX_ITEMS_RECEIVED_AT_ONCE]

    new_items_ids: List[ItemID] = [x.item - item_id_prefix for x in new_items]

    # Since we can have the exact same item id of "item_multiples_ids" items
    # in the new_items_ids list, we have to keep track of the repeat_id
    # of each of them. If didn't do this, we might add the same
    # repeat-version of an item, leading to e.g. sending multiple
    # "RuinsKeyA"s despite wanting to send one "RuinsKeyA",
    # one "RuinsKeyB" and so on
    same_item_in_received_items: Dict[ItemID, int] = {}

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

            while (    repeat_id < len(item_multiples_ids[item_id])
                    and uir_flags[item_multiples_ids[item_id][repeat_id]]
            ):
                repeat_id += 1

            # overwrite item id in list with adjusted id
            same_item_in_received_items[item_id] = repeat_id
            new_items_ids[i] = item_multiples_ids[item_id][repeat_id]

    return new_items_ids


def get_newly_checked_item_locations(
    ctx: "CommonContext",
    modflag_bytes: bytearray,
    gameflag_bytes: bytearray,
) -> Set[LocationID]:
    locs_to_send: Set[LocationID] = set()

    # check through the checks table for checked checks
    for location, data in checks_table.items():
        loc_id: LocationID = location_name_to_id[location]
        loc_is_checked = False

        # these flags are weird and require a helper function to do
        # funny math, refer to doc linked in data
        if data[0] == "MF":
            loc_is_checked = get_flag_value(data[1], modflag_bytes)
        elif data[0] == "GF":
            loc_is_checked = get_flag_value(data[1], gameflag_bytes)

        if loc_is_checked and loc_id in ctx.server_locations:
            locs_to_send.add(loc_id)

    return locs_to_send


def get_new_autohints(
    ctx: "CommonContext",
    current_location: Tuple[int, int],
    current_star_spirits: int,
    already_handled_autohints: Set[int],
) -> List[LocationID]:
    hints: List[LocationID] = []
    for loc in location_groups["AutoHint"]:
        if loc not in already_handled_autohints:
            if current_location == (location_table[loc][2], location_table[loc][3]):
                # don't hint Rowf items you can't see/buy yet
                if current_location == (1, 2): # area TT, map TT plaza
                    # grab the set number from the location name
                    rowf_set = int(loc[len("TT Plaza District Rowf's Shop Set ")])

                    if rowf_set <= current_star_spirits + 1:
                        hints.append(loc)
                else:
                    hints.append(loc)

    # make sure we aren't scouting anything that's already been checked
    hints = [
        location_name_to_id[loc]
        for loc in hints
        if     location_name_to_id[loc] in ctx.missing_locations
           and location_name_to_id[loc] not in ctx.locations_checked
    ]

    return hints
