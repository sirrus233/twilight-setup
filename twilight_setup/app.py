from dataclasses import dataclass, field
from random import choice, shuffle
from typing import List

from twilight_setup.races import get_races


@dataclass
class PlayerData:
    name: str = ""
    location: str = ""
    races: List[str] = field(default_factory=list)


def initialize_player_data(player_count: int) -> List[PlayerData]:
    return [PlayerData() for _ in range(player_count)]


def deal_systems(data: List[PlayerData], names: List[str], systems: List[str]) -> None:
    # Copy the list before shuffling, to avoid destroying the original
    shuffle(names)
    for player_data, (system, name) in zip(data, zip(systems, names)):
        player_data.name = name
        player_data.location = system


def deal_initial_races(data: List[PlayerData]) -> None:
    races = get_races()
    for player_data in data:
        for i in range(2):
            race = choice(races)
            player_data.races.append(race)
            races.remove(race)


def choose_speaker(data: List[PlayerData]) -> PlayerData:
    return choice(data)
