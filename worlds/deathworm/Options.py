from Options import PerGameCommonOptions, DeathLink
from dataclasses import dataclass


@dataclass
class DeathwormOptions(PerGameCommonOptions):
    death_link: DeathLink