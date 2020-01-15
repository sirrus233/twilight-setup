from itertools import chain
from unittest.mock import MagicMock, patch

from twilight_setup.app import PlayerData
from twilight_setup.main import main


@patch("builtins.input")
def test_main(input_mock: MagicMock) -> None:
    # Test results based on manual initial run of the program
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
    drops = ["1", "1", "1", "1", "0", "0"]
    inputs = chain(seed, player_count, players, positions, drops)
    input_mock.side_effect = inputs
    data = main()
    assert data[0] == PlayerData(
        name="Emily", location="Schroeder", races=["L1z1x Mindnet", "Yssaril Tribes"]
    )
    assert data[1] == PlayerData(
        name="Adam",
        location="Unaligned Magi",
        races=["Ghosts of Creuss", "Naalu Collective"],
    )
    assert data[2] == PlayerData(
        name="Alex", location="Jaynor", races=["Emirates of Hacan", "Nekro Virus"]
    )
    assert data[3] == PlayerData(
        name="Tara", location="Vaunt", races=["Universities of Jol-Nar", "Winnu"]
    )
    assert data[4] == PlayerData(
        name="Mason", location="Mage", races=["Arborec", "Sardakk N'or"]
    )
    assert data[5] == PlayerData(
        name="Bradley",
        location="The 9 of Spades",
        races=["Embers of Muaat", "Mentak Coalition"],
    )
