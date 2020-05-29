from itertools import chain
from unittest.mock import MagicMock, patch

from twilight_setup.app import PlayerData
from twilight_setup.main import main


@patch("builtins.input")
def test_main(input_mock: MagicMock) -> None:
    # Test results based loosely on manual initial run of the program
    # Original home systems have been changed since a refactor of deal_systems()
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
        name="Adam",
        location="Vaunt",
        races=["L1z1x Mindnet", "Yssaril Tribes"],
        discarded="Yin Brotherhood",
    )
    assert data[1] == PlayerData(
        name="Alex",
        location="Schroeder",
        races=["Ghosts of Creuss", "Naalu Collective"],
        discarded="Federation of Sol",
    )
    assert data[2] == PlayerData(
        name="Bradley",
        location="Unaligned Magi",
        races=["Emirates of Hacan", "Nekro Virus"],
        discarded="Xxcha Kingdoms",
    )
    assert data[3] == PlayerData(
        name="Emily",
        location="The 9 of Spades",
        races=["Universities of Jol-Nar", "Winnu"],
        discarded="Mentak Coalition",
    )
    assert data[4] == PlayerData(
        name="Mason",
        location="Mage",
        races=["Arborec", "Sardakk N'orr"],
        discarded="Winnu",
    )
    assert data[5] == PlayerData(
        name="Tara",
        location="Jaynor",
        races=["Embers of Muaat", "Mentak Coalition"],
        discarded="Sardakk N'orr",
    )
