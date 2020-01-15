from itertools import chain
from unittest.mock import MagicMock, patch

from twilight_setup.main import main


@patch("builtins.input")
def test_main(input_mock: MagicMock) -> None:
    seed = ["peace cats space turtles"]
    player_count = ["6"]
    players = ["Adam", "Alex", "Bradley", "Emily", "Mason", "Tara"]
    positions = [
        "Schroeder",
        "Unaligned Magi",
        "Jaynor",
        "Vaunt",
        "Mage",
        "The 9 of Spades",
    ]
    inputs = chain(seed, player_count, players, positions)
    input_mock.side_effect = inputs
    main()
