# alchemy/transmutation/advanced.py
# Importações relativas: '.' para o mesmo nível, '..' para subir um nível
from .basic import lead_to_gold
from ..potions import healing_potion


def philosophers_stone():
    """Creates a philosopher's stone using gold and a healing potion."""
    gold_result = lead_to_gold()
    potion_result = healing_potion()
    return (f"Philosopher's stone created using {gold_result} "
            f"and {potion_result}")


def elixir_of_life():
    """Returns the result of achieving eternal youth."""
    return "Elixir of life: eternal youth achieved!"