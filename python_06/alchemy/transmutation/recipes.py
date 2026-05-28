"""Recipes for alchemical transmutation."""

from elements import create_fire

from ..elements import create_air
from ..potions import strength_potion


def lead_to_gold() -> str:
    """Transmute lead into gold using elemental and potion ingredients."""
    return (
        "Recipe transmuting Lead to Gold: brew "
        f"'{create_air()}' and '{strength_potion()}' mixed with "
        f"'{create_fire()}'"
    )
