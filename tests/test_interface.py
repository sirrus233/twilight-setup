from random import randint, seed
from unittest.mock import MagicMock, patch

import twilight_setup.interface as interface
from pytest import raises  # type: ignore
from twilight_setup.app import PlayerData


@patch("builtins.input")
def test_empty_string_seed_treated_as_default(input_mock: MagicMock) -> None:
    seed("")
    empty_seed_random_int = randint(1, 10 ** 10)

    input_mock.return_value = ""
    interface.set_seed()
    user_seeded_random_int = randint(1, 10 ** 10)

    assert empty_seed_random_int != user_seeded_random_int


@patch("builtins.input")
def test_user_can_set_seed(input_mock: MagicMock) -> None:
    seed("seed")
    default_random_int = randint(1, 10 ** 10)

    input_mock.return_value = "Some non-empty string."
    interface.set_seed()
    user_seeded_random_int = randint(1, 10 ** 10)

    assert default_random_int != user_seeded_random_int


@patch("builtins.input")
def test_set_player_count(input_mock: MagicMock) -> None:
    failing_inputs = ["NaN", "-1", "-1.01", "0", "1", "1.01"]
    passing_inputs = ["2", "6", "8"]

    input_mock.side_effect = failing_inputs
    for _ in failing_inputs:
        with raises(ValueError):
            interface.set_player_count()

    input_mock.side_effect = passing_inputs
    for value in passing_inputs:
        assert interface.set_player_count() == int(value)


@patch("builtins.input")
def test_set_player_names(input_mock: MagicMock) -> None:
    player_names = ["A", "B", "C", "D", "E", "F"]
    input_mock.side_effect = player_names
    player_count = len(player_names)
    assert interface.set_player_names(player_count) == player_names


@patch("builtins.input")
def test_set_system_names(input_mock: MagicMock) -> None:
    system_names = ["A", "B", "C", "D", "E", "F"]
    input_mock.side_effect = system_names
    player_count = len(system_names)
    assert interface.set_system_names(player_count) == system_names


def test_display_results() -> None:
    player_data = PlayerData(name="a", location="b", races=["c", "d"])
    interface.display_results([player_data] * 6, player_data)
