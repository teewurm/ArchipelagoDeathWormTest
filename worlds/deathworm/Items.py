# This file is auto generated. More info: https://github.com/Daivuk/apdoom

from BaseClasses import ItemClassification
from typing import TypedDict, Dict, Set


class ItemDict(TypedDict, total=False):
    classification: ItemClassification
    count: int
    name: str
    doom_type: int  # Unique numerical id used to spawn the item. -1 is level item, -2 is level complete item.
    episode: int  # Relevant if that item targets a specific level, like keycard or map reveal pickup.
    map: int


item_table: Dict[int, ItemDict] = {
    350000: {'classification': ItemClassification.filler,
             'count': 1,
             'name': 'Placeholder',
             'episode': 1,
             'map': 1}
}

item_name_groups: Dict[str, Set[str]] = {
}
