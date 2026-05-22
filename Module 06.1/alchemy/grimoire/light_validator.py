
def validate_ingredients(ingredients: str) -> str:
    # late import to avoid circular dependency
    from .light_spellbook import light_spell_allowed_ingredients

    allowed = light_spell_allowed_ingredients()
    is_valid = any(item in ingredients.lower() for item in allowed)
    status = "VALID" if is_valid else "INVALID"

    return f"{ingredients} {status}"
