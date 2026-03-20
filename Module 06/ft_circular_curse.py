# ft_circular_curse.py
from alchemy.grimoire import record_spell, validate_ingredients


def ft_circular_curse():
    """Demonstrates circular dependency resolution using late imports."""
    print("=== Circular Curse Breaking ===")

    # Testando a validação pura
    print("\nTesting ingredient validation:")
    print(f"validate_ingredients('fire air'): {validate_ingredients('fire air')}")
    print(f"validate_ingredients('dragon scales'): {validate_ingredients('dragon scales')}")

    # Testando o registro de feitiços (que usa a importação tardia)
    print("\nTesting spell recording with validation:")
    print(f"record_spell('Fireball', 'fire air'): {record_spell('Fireball', 'fire air')}")
    print(f"record_spell('Dark Magic', 'shadow'): {record_spell('Dark Magic', 'shadow')}")

    print("\nTesting late import technique:")
    print(f"record_spell('Lightning', 'air'): {record_spell('Lightning', 'air')}")

    print("\nCircular dependency curse avoided using late imports!")
    print("All spells processed safely!")


if __name__ == "__main__":
    ft_circular_curse()
