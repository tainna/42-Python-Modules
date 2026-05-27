from typing import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined_spell(target: str, power: int) -> tuple:
        return (spell1(target, power), spell2(target, power))
    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified_spell(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return conditional_spell


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence_spell(target: str, power: int) -> list:
        return [spell(target, power) for spell in spells]
    return sequence_spell


def main():
    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target}"

    def heal(target: str, power: int) -> str:
        return f"Heals {target}"

    def test_power_spell(target: str, power: int) -> str:
        return str(power)

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    res1, res2 = combined("Dragon", 10)
    print(f"Combined spell result: {res1}, {res2}")

    print("Testing power amplifier...")
    amplified = power_amplifier(test_power_spell, 3)

    print(f"Original: 10, Amplified: {amplified('DummyTarget', 10)}")

    print("\nDemonstrating conditional caster...")

    def is_strong_enough(target: str, power: int) -> bool:
        return power >= 50
    cond_spell = conditional_caster(is_strong_enough, fireball)
    print(f"Power 40 (fails): {cond_spell('Orc', 40)}")
    print(f"Power 60 (works): {cond_spell('Orc', 60)}")

    print("\nDemonstrating spell sequence...")
    seq_spell = spell_sequence([fireball, heal, fireball])
    print(f"Sequence result: {seq_spell('Goblin', 25)}")


if __name__ == "__main__":
    main()
