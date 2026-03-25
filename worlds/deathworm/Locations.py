# This file is auto generated. More info: https://github.com/Daivuk/apdoom

from typing import Dict, TypedDict, List, Set


class LocationDict(TypedDict, total=False):
    name: str
    episode: int
    map: int
    index: int  # Thing index as it is stored in the wad file.
    doom_type: int  # In case index end up unreliable, we can use doom type. Maps have often only one of each important things.
    region: str


location_table: Dict[int, LocationDict] = {
    351000: {'name': 'Placeholder',
             'episode': 1,
             'map': 1,
             'index': 1,
             'region': "Menu"}
}

location_name_groups: Dict[str, Set[str]] = {

}
