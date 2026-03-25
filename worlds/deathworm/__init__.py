import logging

from BaseClasses import Entrance, CollectionState, Item, Location, MultiWorld, Region, Tutorial, ItemClassification
from worlds.AutoWorld import WebWorld, World
# from . import Items, Locations, Maps, Regions, Rules
from . import Items, Locations
from .Options import DeathwormOptions

logger = logging.getLogger("Deathworm")


class DeathwormLocation(Location):
    game: str = "Deathworm"


class DeathwormItem(Item):
    game: str = "Deathworm"


class DeathwormWeb(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the deathworm",
        "English",
        "setup_en.md",
        "setup/en",
        ["teaworm"]
    )]
    theme = "dirt"


class DeathwormWorld(World):
    """
    Deathworm
    """
    options_dataclass = DeathwormOptions
    options: DeathwormOptions
    game = "Deathworm"
    web = DeathwormWeb()
    required_client_version = (0, 6, 6)  # 1.2.0-prerelease or higher

    item_name_to_id = {data["name"]: item_id for item_id, data in Items.item_table.items()}
    item_name_groups = Items.item_name_groups

    location_name_to_id = {data["name"]: loc_id for loc_id, data in Locations.location_table.items()}
    location_name_groups = Locations.location_name_groups

    def __init__(self, multiworld: MultiWorld, player: int):
        super().__init__(multiworld, player)

    def create_regions(self):
        # Main regions
        menu_region = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions += [menu_region]

    def set_rules(self):
        self.multiworld.completion_condition[self.player] = lambda state: True

    def create_item(self, name: str) -> DeathwormItem:
        return DeathwormItem(name, ItemClassification.filler, 0, self.player)
