

def validate_ingredients(ingredients: str) -> str:
    """
    Validates alchemical ingredients. 
    Valid if it contains 'fire', 'water', 'earth', or 'air'.
    """
    valid_elements = ["fire", "water", "earth", "air"]
    # Verifica se qualquer um dos elementos válidos está na string de ingredientes
    if any(element in ingredients.lower() for element in valid_elements):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
