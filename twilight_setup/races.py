from typing import List

RACES = (
    "Arborec",
    "Barony of Letnev",
    "Clan of Saar",
    "Embers of Muaat",
    "Emirates of Hacan",
    "Federation of Sol",
    "Ghosts of Creuss",
    "L1z1x Mindnet",
    "Mentak Coalition",
    "Naalu Collective",
    "Nekro Virus",
    "Sardakk N'orr",
    "Universities of Jol-Nar",
    "Winnu",
    "Xxcha Kingdoms",
    "Yin Brotherhood",
    "Yssaril Tribes",
)


def get_races() -> List[str]:
    """
    Provides a mutable copy of the constant race list
    """
    return list(RACES)
