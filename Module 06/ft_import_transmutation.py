
# Método 1: Importação de módulo completo
import alchemy.elements

# Método 2: Importação de função específica
from alchemy.elements import create_water

# Método 3: Importação com apelido (alias)
from alchemy.potions import healing_potion as heal

# Método 4: Importações múltiplas
from alchemy.elements import create_fire, create_earth
from alchemy.potions import strength_potion


def ft_import_transmutation():
    """Demonstrates four different import transmutation methods."""
    print("=== Import Transmutation Mastery ===")

    # Método 1
    print("\nMethod 1 - Full module import:")
    print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")

    # Método 2
    print("\nMethod 2 - Specific function import:")
    print(f"create_water(): {create_water()}")

    # Método 3
    print("\nMethod 3 - Aliased import:")
    print(f"heal(): {heal()}")

    # Método 4
    print("\nMethod 4 - Multiple imports:")
    print(f"create_earth(): {create_earth()}")
    print(f"create_fire(): {create_fire()}")
    print(f"strength_potion(): {strength_potion()}")

    print("\nAll import transmutation methods mastered!")


if __name__ == "__main__":
    ft_import_transmutation()
