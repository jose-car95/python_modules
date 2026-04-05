def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients

    normalized: str = ingredients.lower()
    allowed: list[str] = light_spell_allowed_ingredients()
    is_valid: bool = any(item in normalized for item in allowed)
    status: str = "VALID" if is_valid else "INVALID"
    return f"{ingredients} - {status}"
