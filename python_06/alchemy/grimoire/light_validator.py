"""Validator for light magic ingredients."""

from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    """Validate ingredients for light magic and return the verdict string."""
    normalized_ingredients = ingredients.lower()
    allowed_ingredients = light_spell_allowed_ingredients()
    is_valid = any(
        item in normalized_ingredients for item in allowed_ingredients
    )
    status = "VALID" if is_valid else "INVALID"
    return f"{ingredients} - {status}"
