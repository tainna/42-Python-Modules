

class TournamentPlatform:
    def __init__(self):
        self.registry = {}
        self.matches_count = 0

    def register_card(self, card) -> str:
        self.registry[card.card_id] = card
        return card.card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        c1 = self.registry[card1_id]
        c2 = self.registry[card2_id]

        # Lógica simples: quem tem mais ataque vence
        if c1.attack_val >= c2.attack_val:
            winner, loser = c1, c2
        else:
            winner, loser = c2, c1

        winner.update_wins(1)
        loser.update_losses(1)
        self.matches_count += 1

        return {
            "winner": winner.card_id,
            "loser": loser.card_id,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating
        }

    def get_leaderboard(self) -> list:
        # Retorna lista ordenada pelo rating decrescente
        sorted_cards = sorted(self.registry.values(),
                              key=lambda x: x.rating, reverse=True)
        return [
            f"{c.name} Rating: {c.rating}"
            f"({c.wins}-{c.losses})"
            for c in sorted_cards]

    def generate_tournament_report(self) -> dict:
        total = len(self.registry)
        if total == 0:
            avg_rating = 0
        else:
            total_points = sum(c.rating for c in self.registry.values())
            avg_rating = int(total_points / total)

        return {
            "total_cards": total,
            "matches_played": self.matches_count,
            "avg_rating": avg_rating,
            "platform_status": "active"
        }
