from typing import List

import twilight_setup.app as app
import twilight_setup.interface as interface


def main() -> List[app.PlayerData]:
    interface.set_seed()
    player_count = interface.set_player_count()
    players = interface.set_player_names(player_count)
    systems = interface.set_system_names(player_count)
    data = app.initialize_player_data(player_count)
    app.deal_systems(data, players, systems)
    app.deal_initial_races(data)
    interface.choose_race_drops(data)
    app.deal_second_round_races(data)
    speaker = app.choose_speaker(data)
    interface.display_results(data, speaker)
    return data


if __name__ == "__main__":
    main()  # pragma: no cover
