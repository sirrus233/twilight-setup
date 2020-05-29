"""Module detailing functions and flows for how a user interacts with the application.
Roughly corresponds to the "view" of the app, though it may be via the CLI."""
from random import seed
from typing import List

from twilight_setup.app import PlayerData


def set_seed() -> None:
    """Prompt user to provide a random seed. This ensures subsequent
    runs of the app can replicate past results.
    """
    print("Set random seed [blank for Default]: ", end="")
    user_input = input()
    seed(user_input if user_input else None)
    print()


def set_player_count() -> int:
    """Query user for the number of players.

    :return: Player count.
    """
    print("How many players: ", end="")
    user_input = input()
    if _validate_player_count(user_input):
        print()
        return int(user_input)
    raise ValueError("Invalid number of players.")


def _validate_player_count(user_input: str) -> bool:
    return user_input.isdigit() and int(user_input) >= 2


def set_player_names(player_count: int) -> List[str]:
    """Query user for the player names.

    :param player_count: Number of players.
    :return: List of player names.
    """
    names = []
    for i in range(1, player_count + 1):
        print(f"Player {i}: ", end="")
        names.append(input())
    print()
    return names


def set_system_names(player_count: int) -> List[str]:
    """Query user for names that can be assigned to the home star systems. These names
    can be arbitrary, but will be used to assign relative positions around the table in
    a pre-constructed galaxy map.

    :param player_count: Number of players.
    :return: List of star system names.
    """
    systems = []
    for i in range(1, player_count + 1):
        print(f"System {i}: ", end="")
        systems.append(input())
    print()
    return systems


def choose_race_drops(data: List[PlayerData]) -> None:
    """Query user for the race drop choices. Each player is permitted to drop one of the
    races that they were dealt. These drop options are input by the user for each player
    in turn.

    :param data: List of player data.
    """
    for player_data in data:
        print(f"Choose race drop for {player_data.name}: ")
        print(f"\t[0]: {player_data.races[0]}")
        print(f"\t[1]: {player_data.races[1]}")
        user_input = input()
        if _validate_drop_choice(user_input):
            discard = player_data.races.pop(int(user_input))
            player_data.discarded = discard
            print()
        else:
            raise ValueError("Invalid race selection.")


def _validate_drop_choice(user_input: str) -> bool:
    return user_input.isdigit() and 0 <= int(user_input) <= 1


def display_results(data: List[PlayerData], speaker: PlayerData) -> None:
    """Show final results, including race assignments, starting systems, and speaker.

    :param data: List of player data.
    :param speaker: Player data for the player who will be the Speaker.
    """
    for player_data in data:
        print(f"{player_data.name}: {player_data.location}")
        print(f"\t{player_data.races[0]}, {player_data.races[1]}")
    print()
    print(f"Speaker: {speaker.name}")
