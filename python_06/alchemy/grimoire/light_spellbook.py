"""Spellbook for safe light magic records."""


def light_spell_allowed_ingredients() -> list[str]:
    """Return the allowed ingredients for light magic."""
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    """Record a light spell if its ingredients are validated."""
    from .light_validator import validate_ingredients

    validation = validate_ingredients(ingredients)
    return f"Spell recorded: {spell_name} ({validation})"
