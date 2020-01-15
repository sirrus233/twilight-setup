import random
from dataclasses import dataclass, field
from typing import List

from twilight_setup.races import get_races


@dataclass
class PlayerData:
    name: str = ""
    location: str = ""
    races: List[str] = field(default_factory=list)
    discarded: str = ""


def initialize_player_data(player_count: int) -> List[PlayerData]:
    return [PlayerData() for _ in range(player_count)]


def deal_systems(data: List[PlayerData], names: List[str], systems: List[str]) -> None:
    # Copy the list before shuffling, to avoid destroying the original
    random.shuffle(names)
    for player_data, (system, name) in zip(data, zip(systems, names)):
        player_data.name = name
        player_data.location = system


def deal_initial_races(data: List[PlayerData]) -> None:
    races = get_races()
    for player_data in data:
        for i in range(2):
            race = random.choice(races)
            player_data.races.append(race)
            races.remove(race)


def deal_second_round_races(data: List[PlayerData]) -> None:
    # Figure out which races have not  already been chosen
    chosen_races = {player_data.races[0] for player_data in data}
    available_races = [race for race in get_races() if race not in chosen_races]

    for player_data in data:
        # Before choosing a random second race, remove the race that this player has
        # already discarded, then after choosing the random race, add the discarded race
        # back so it may be dealt to other players
        if player_data.discarded in available_races:
            available_races.remove(player_data.discarded)
        race = random.choice(available_races)
        player_data.races.append(race)
        available_races.remove(race)
        available_races.append(player_data.discarded)


def choose_speaker(data: List[PlayerData]) -> PlayerData:
    return random.choice(data)
