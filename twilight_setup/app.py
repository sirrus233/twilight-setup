"""This module describes most of the business logic of the app's backend."""
import random
from dataclasses import dataclass, field
from typing import List

from twilight_setup.races import get_races


@dataclass
class PlayerData:
    """Represents a player, along with everything the app knows about that player."""

    name: str = ""
    location: str = ""
    races: List[str] = field(default_factory=list)
    discarded: str = ""


def initialize_player_data(player_names: List[str]) -> List[PlayerData]:
    """Creates a PlayerData object for each player in the game.

    :param player_names: Player name strings.
    :return: A list of all created PlayerData objects.
    """
    return [PlayerData(name=name) for name in player_names]


def deal_systems(data: List[PlayerData], systems: List[str]) -> None:
    """Deals out random home systems to each player.

    :param data: List of player data.
    :param systems: Home system names, to be assigned.
    """
    # Copy the list before shuffling, to avoid destroying the original
    systems = systems.copy()
    random.shuffle(systems)
    for player_data, system in zip(data, systems):
        player_data.location = system


def deal_initial_races(data: List[PlayerData]) -> None:
    """Deals out random starting races to each players. Each player is given 2 options.

    :param data: List of player data.
    """
    races = get_races()
    for player_data in data:
        for _ in range(2):
            race = random.choice(races)
            player_data.races.append(race)
            races.remove(race)


def deal_second_round_races(data: List[PlayerData]) -> None:
    """Deals out random starting races, given that each player has already dropped
    one of their racial options, and should not be dealt the same race again, nor a
    race belonging to anybody else.

    :param data: List of player data.
    """
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
    """Pick who will be the Speaker.

    :param data: List of player data.
    :return: A single PlayerData representing the Speaker.
    """
    return random.choice(data)
