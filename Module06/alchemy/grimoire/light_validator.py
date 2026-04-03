def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    for ingredient in ingredients.split(' '):
        if ingredient.lower() in light_spell_allowed_ingredients():
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
