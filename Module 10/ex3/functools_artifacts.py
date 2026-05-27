import functools
import operator
from typing import Callable, Any


def spell_reducer(spells: list[int], operation: str) -> int:
    """Combines a list of spell powers using reduce and the operator module."""
    if not spells:
        return 0

    operations: dict[str, Callable[[int, int], int]] = {
        "add": operator.add,
        "multiply": operator.mul,

        "max": lambda a, b: max(a, b),
        "min": lambda a, b: min(a, b)
    }

    if operation not in operations:
        raise ValueError(f"Unknown operation: {operation}")

    return functools.reduce(operations[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    """
    Takes a base enchantment (power, element, target) and creates
    3 specialized versions with pre-filled power and elements.
    """
    return {
        "fire": functools.partial(base_enchantment, 50, "fire"),
        "water": functools.partial(base_enchantment, 50, "water"),
        "earth": functools.partial(base_enchantment, 50, "earth")
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """Calculates the nth Fibonacci number,
    utilizing lru_cache for performance."""
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    """Creates a single-dispatch function to handle different
    spell input types."""

    @functools.singledispatch
    def cast_spell(arg: Any) -> str:
        return "Unknown spell type"

    @cast_spell.register(int)
    def _(arg: int) -> str:
        return f"Damage spell: {arg} damage"

    @cast_spell.register(str)
    def _(arg: str) -> str:
        return f"Enchantment: {arg}"

    @cast_spell.register(list)
    def _(arg: list) -> str:
        return f"Multi-cast: {len(arg)} spells"

    return cast_spell


if __name__ == "__main__":
    print("\nTesting spell reducer...")
    spells = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")

    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher([1, 2, 3]))
    print(dispatcher({"some": "dict"}))
