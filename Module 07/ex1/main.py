from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main():
    print("=== DataDeck Deck Builder ===")
    print("\nBuilding deck with different card types...")

    my_deck = Deck()

    # 2. Criar instâncias de diferentes tipos de cartas
    # Nota: No ex0 você deve garantir que a raridade use Enum se seguir à risca
    dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    bolt = SpellCard("Lightning Bolt", 3, "Common", "damage")
    crystal = ArtifactCard("Mana Crystal", 2, "Rare", 3, "+1 mana per turn")

    # 3. Adicionar cartas ao deck
    my_deck.add_card(dragon)
    my_deck.add_card(bolt)
    my_deck.add_card(crystal)

    # 4. Mostrar estatísticas do deck
    stats = my_deck.get_deck_stats()
    print(f"Deck stats: {stats}")

    print("\nDrawing and playing cards:")

    # 5. Demonstrar o sorteio (draw) e o polimorfismo
    # Embaralhar antes de sortear
    my_deck.shuffle()

    for _ in range(3):
        card = my_deck.draw_card()
        if card:
            # O polimorfismo permite chamar .play() independente da carta
            # Aqui você pode verificar o tipo para formatar como no exemplo
            card_type = card.__class__.__name__.replace("Card", "")
            print(f"\nDrew: {card.name} ({card_type})")

            # Simulando um estado de jogo genérico
            result = card.play({"available_mana": 10})
            print(f"Play result: {result}")

    print(
        "\nPolymorphism in action:Same interface, different card behaviors!"
        )


if __name__ == "__main__":
    main()
