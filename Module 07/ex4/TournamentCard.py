from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack_val: int, card_id: str):
        super().__init__(name, cost, rarity)
        self.attack_val = attack_val
        self.card_id = card_id
        self.wins = 0
        self.losses = 0
        self.rating = 1200  # Rating inicial padrão

    def play(self, game_state: dict) -> dict:
        return {"card_played": self.name, "id": self.card_id}

    def attack(self, target) -> dict:
        return {"attacker": self.card_id, "damage": self.attack_val}

    def defend(self, incoming_damage: int) -> dict:
        return {"defender": self.card_id, "damage_taken": incoming_damage}

    def get_combat_stats(self) -> dict:
        return {"attack": self.attack_val}

    def calculate_rating(self) -> int:
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self.rating += (wins * 16)  # Exemplo de ganho de rating

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        self.rating -= (losses * 16)  # Exemplo de perda de rating

    def get_rank_info(self) -> dict:
        return {
            "id": self.card_id,
            "rating": self.rating,
            "record": f"{self.wins}-{self.losses}"
        }

    def get_tournament_stats(self) -> dict:
        return self.get_rank_info()
