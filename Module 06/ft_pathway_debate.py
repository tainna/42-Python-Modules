import alchemy.transmutation.basic
import alchemy.transmutation.advanced
import alchemy.transmutation


def ft_pathway_debate() -> None:
    """Demonstrates absolute vs relative imports and package-level access."""
    print("=== Pathway Debate Mastery ===")

    # Testing Absolute Imports (from basic.py)
    print("\nTesting Absolute Imports (from basic.py):")
    print(f"lead_to_gold(): {alchemy.transmutation.basic.lead_to_gold()}")
    print(f"stone_to_gem(): {alchemy.transmutation.basic.stone_to_gem()}")

    # Testing Relative Imports (from advanced.py)
    print("\nTesting Relative Imports (from advanced.py):")
    print("philosophers_stone(): "
          f"{alchemy.transmutation.advanced.philosophers_stone()}")
    print("elixir_of_life(): "
          f"{alchemy.transmutation.advanced.elixir_of_life()}")

    # Testing Package Access
    print("\nTesting Package Access:")
    print("alchemy.transmutation.lead_to_gold(): "
          f"{alchemy.transmutation.lead_to_gold()}")
    print("alchemy.transmutation.philosophers_stone(): "
          f"{alchemy.transmutation.philosophers_stone()}")

    print("\nBoth pathways work! Absolute: clear, Relative: concise")


if __name__ == "__main__":
    ft_pathway_debate()
