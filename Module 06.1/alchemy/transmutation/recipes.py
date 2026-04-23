# Absolute import (da raiz do projeto)
from elements import create_fire

# Absolute import (do pacote alchemy)
from alchemy.potions import strength_potion

# Relative import (sobe um nível '..' para a pasta alchemy e pega o elements)
from ..elements import create_air


def lead_to_gold() -> str:
    air = create_air()
    potion = strength_potion()
    fire = create_fire()
    return (
        f"Recipe transmuting Lead to Gold: brew '{air}' and "
        f"'{potion}' mixed with '{fire}'"
        )
