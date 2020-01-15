from twilight_setup.races import RACES, get_races


def test_default_races() -> None:
    assert len(RACES) == 17


def test_get_races() -> None:
    races = get_races()
    assert len(races) == 17
    # Ensure mutation is allowed and doesn't raise an exception
    races[0] = ""
