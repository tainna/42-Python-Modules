from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main():
    print("=== DataDeck Tournament Platform ===")
    platform = TournamentPlatform()

    print("Registering Tournament Cards...")
    dragon = TournamentCard("Fire Dragon", 5, "Legendary", 7, "dragon_001")
    wizard = TournamentCard("Ice Wizard", 4, "Rare", 5, "wizard_001")

    platform.register_card(dragon)
    platform.register_card(wizard)

    # Exibe informações iniciais
    for card in [dragon, wizard]:
        print(f"{card.name} (ID: {card.card_id}):")
        print("Interfaces: [Card, Combatable, Rankable]")
        print(f"Rating: {card.rating}")
        print(f"Record: {card.wins}-{card.losses}")

    print("\nCreating tournament match...")
    match_res = platform.create_match("dragon_001", "wizard_001")
    print(f"Match result: {match_res}")

    print("\nTournament Leaderboard:")
    for i, entry in enumerate(platform.get_leaderboard(), 1):
        print(f"{i}. {entry}")

    print("\nPlatform Report:")
    print(platform.generate_tournament_report())

    print("\nTournament Platform Successfully Deployed!")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
