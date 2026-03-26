from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"Executed {self.effect_type} effect"
        }

    def resolve_effect(self, targets: list) -> dict:
        return {
                "spell_name": self.name,
                "effect_type": self.effect_type,
                "targets_affected": len(targets),
                "status": "resolved"
        }
