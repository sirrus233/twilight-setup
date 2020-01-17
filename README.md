# Twilight Setup: A Setup Tool for Twilight Imperium
This app is a simple setup script for determining the initial game state of a game of
Twilight Imperium. It deals out randomized home systems and races to each player, as
well as choosing the initial speaker.

Pax Magnifica Bellum Gloriosum.

## Usage
There are no dependencies aside from Python 3.8. Execute the main.py file. The CLI utility has prompts to guide you.  
Just run and play.

## Setup Algorithm
Twilight Setup uses a two-round random draft with a mulligan.

1. Start by providing the names of each of your players, and giving a name to each start position around the galaxy.
2. Each player will be dealt a random start position, and two random races.
3. Each player chooses one race to discard, and one to keep.
4. Each player is dealt a new race to replace their discarded race. No player will be re-dealt their discarded race, but you may be dealt the discarded races of others.
5. The speaker is revealed at this time.
6. Players pick their final race choice.

## Contributing
This project uses [Poetry](https://python-poetry.org/) for building and dependency management. You will need to install poetry first. Then simply run:

```
poetry install
poetry run pre-commit install
```
