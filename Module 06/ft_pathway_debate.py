import alchemy.transmutation.basic
import alchemy.transmutation.advanced
import alchemy.transmutation


def ft_pathway_debate():
    """Demonstrates absolute vs relative imports and package-level access."""
    print("=== Pathway Debate Mastery")

    # Testando Importações Absolutas (de basic.py)
    print("\nTesting Absolute Imports (from basic.py):")
    print(f"lead_to_gold(): {alchemy.transmutation.basic.lead_to_gold()}")
    print(f"stone_to_gem(): {alchemy.transmutation.basic.stone_to_gem()}")

    # Testando Importações Relativas (de advanced.py)
    print("\nTesting Relative Imports (from advanced.py):")
    print(f"philosophers_stone(): "
          f"{alchemy.transmutation.advanced.philosophers_stone()}")
    print(f"elixir_of_life(): "
          f"{alchemy.transmutation.advanced.elixir_of_life()}")

    # Testando Acesso via Pacote (graças ao __init__.py)
    print("\nTesting Package Access:")
    print("alchemy.transmutation.lead_to_gold(): "
          f"{alchemy.transmutation.lead_to_gold()}")
    print("alchemy.transmutation.philosophers_stone(): "
          f"{alchemy.transmutation.philosophers_stone()}")

    print("\nBoth pathways work! Absolute: clear, Relative: concise")


if __name__ == "__main__":
    ft_pathway_debate()
