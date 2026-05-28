"""Validator for intentionally unsafe dark magic imports."""

from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    """Validate ingredients for dark magic and return the verdict string."""
    normalized_ingredients = ingredients.lower()
    allowed_ingredients = dark_spell_allowed_ingredients()
    is_valid = any(
        item in normalized_ingredients for item in allowed_ingredients
    )
    status = "VALID" if is_valid else "INVALID"
    return f"{ingredients} - {status}"
