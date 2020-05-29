"""Main module"""
from typing import List

import twilight_setup.app as app
import twilight_setup.interface as interface


def main() -> List[app.PlayerData]:
    """Start and run the app"""
    interface.set_seed()
    player_count = interface.set_player_count()
    players = interface.set_player_names(player_count)
    systems = interface.set_system_names(player_count)
    data = app.initialize_player_data(players)
    app.deal_systems(data, systems)
    app.deal_initial_races(data)
    interface.choose_race_drops(data)
    app.deal_second_round_races(data)
    speaker = app.choose_speaker(data)
    interface.display_results(data, speaker)
    return data


if __name__ == "__main__":
    main()  # pragma: no cover
