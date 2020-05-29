import random
from itertools import chain
from unittest.mock import MagicMock, patch

import twilight_setup.app as app


def test_initialize_player_data() -> None:
    names = ["p1", "p2", "p3", "p4", "p5", "p6"]
    data = app.initialize_player_data(names)
    assert len(data) == 6
    assert data[0] is not data[1]
    assert [player_data.name for player_data in data] == names


def test_deal_systems() -> None:
    random.seed("test")
    names = ["p1", "p2", "p3", "p4", "p5", "p6"]
    systems = ["s1", "s2", "s3", "s4", "s5", "s6"]
    data = app.initialize_player_data(names)
    app.deal_systems(data, systems)
    assert sorted([player_data.location for player_data in data]) == systems


def test_deal_initial_races() -> None:
    random.seed("test")
    names = ["p1", "p2", "p3", "p4", "p5", "p6"]
    data = app.initialize_player_data(names)
    app.deal_initial_races(data)
    races = chain.from_iterable([player_data.races for player_data in data])
    assert len(set(races)) == 12


@patch("twilight_setup.app.get_races")
def test_deal_second_round_races(get_races_mock: MagicMock) -> None:
    random.seed("test")
    get_races_mock.return_value = ["a", "b", "c", "d"]
    data = [
        app.PlayerData(races=["a"], discarded="b"),
        app.PlayerData(races=["c"], discarded="d"),
    ]
    app.deal_second_round_races(data)
    assert data[0].races == ["a", "d"]
    assert data[1].races == ["c", "b"]


def test_choose_speaker() -> None:
    random.seed("test")
    names = ["p1", "p2", "p3", "p4", "p5", "p6"]
    data = app.initialize_player_data(names)
    speaker = app.choose_speaker(data)
    assert speaker in data
