from ex0.CreatureCard import CreatureCard


def main():
    """Executa os testes básicos do Exercício 0."""
    print("DataDeck Card Foundation")
    print("Testing Abstract Base Class Design:")

    # Instanciação conforme os requisitos
    dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

    print("\nCreatureCard Info:")
    print(dragon.get_card_info())

    # Teste de mana suficiente
    available_mana = 6
    print(f"\nPlaying {dragon.name} with {available_mana} mana available:")
    print(f"Playable: {dragon.is_playable(available_mana)}")
    print(f"Play result: {dragon.play({})}")

    # Teste de combate
    target = "Goblin Warrior"
    print(f"\n{dragon.name} attacks {target}:")
    print(f"Attack result: {dragon.attack_target(target)}")

    # Teste de mana insuficiente
    low_mana = 3
    print(f"\nTesting insufficient mana ({low_mana} available):")
    print(f"Playable: {dragon.is_playable(low_mana)}")

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
