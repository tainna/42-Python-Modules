from ex2.EliteCard import EliteCard


def main():
    print("\n=== DataDeck Ability System ===")

    # Instanciando a EliteCard conforme o exemplo
    warrior = EliteCard("Arcane Warrior", 6, "Epic", 5, 4)

    print("\nEliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

    print(f"\nPlaying {warrior.name} (Elite Card):")
    # Chamada do método play (obrigatório da classe Card)
    warrior.play({"available_mana": 10})

    print("\nCombat phase:")
    # Saída esperada para o ataque
    attack_res = warrior.attack("Enemy")
    print(f"Attack result: {attack_res}")

    # Saída esperada para a defesa
    defense_res = warrior.defend(2)
    print(f"Defense result: {defense_res}")

    print("\nMagic phase:")
    # Saída esperada para o feitiço
    spell_res = warrior.cast_spell("Fireball", ["Enemy1", "Enemy2"])
    print(f"Spell cast: {spell_res}")

    # Saída esperada para o canal de mana
    mana_res = warrior.channel_mana(3)
    print(f"Mana channel: {mana_res}")

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
