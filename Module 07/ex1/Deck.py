import random
from typing import List, Optional
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class Deck:
    def __init__(self):
        # Inicia uma lista vazia p Card
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        """Adiciona uma carta ao baralho."""
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        """Remove a primeira ocorrenc de uma carta pelo nome."""
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        """Embaralha as cartas usando o mod random."""
        random.shuffle(self.cards)

    def draw_card(self) -> Optional[Card]:
        """Remove e retorna a last carta do topo do baralho."""
        if not self.cards:
            return None
        return self.cards.pop()

    def get_deck_stats(self) -> dict:
        """Calcula e retorna est sobre a comp do deck."""
        total = len(self.cards)
        if total == 0:
            return {"total_cards": 0, "avg_cost": 0.0}

        # Conta usando isinstance para demonstrar polimorfismo
        creatures = sum(1 for c in self.cards if isinstance(c, CreatureCard))
        spells = sum(1 for c in self.cards if isinstance(c, SpellCard))
        artifacts = sum(1 for c in self.cards if isinstance(c, ArtifactCard))
        avg_cost = sum(c.cost for c in self.cards) / total

        return {
            "total_cards": total,
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": round(avg_cost, 2)
        }
