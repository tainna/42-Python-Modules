from typing import Callable, Any


def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
    # Permite modificar a variável 'count' do escopo externo
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    total_power = initial_power

    def add_power(amount: int) -> int:
        nonlocal total_power
    # Permite modificar 'total_power' a cada chamada
        total_power += amount
        return total_power
    return add_power


def enchantment_factory(enchantment_type: str) -> Callable:
    # Não precisa de nonlocal aqui porque estamos apenas lendo
    # o enchantment_type
    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchant


def memory_vault() -> dict[str, Callable]:
    # O dicionário 'vault' é encapsulado aqui (estado privado)
    vault: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        vault[key] = value

    def recall(key: str) -> Any:
        return vault.get(key, "Memory not found")

    return {'store': store, 'recall': recall}


def main():
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell accumulator...")
    accumulator = spell_accumulator(100)
    print(f"Base 100, add 20: {accumulator(20)}")
    print(f"Base 100, add 30: {accumulator(30)}")

    print("\nTesting enchantment factory...")
    flame_enchant = enchantment_factory("Flaming")
    frost_enchant = enchantment_factory("Frozen")
    print(flame_enchant("Sword"))
    print(frost_enchant("Shield"))

    print("\nTesting memory vault...")
    vault = memory_vault()
    vault['store']('secret', 42)
    print("Store 'secret' = 42")
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")


if __name__ == "__main__":
    main()
