from ex0.Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int):
        # Chamo a classe pai para name, cost e rarity
        super().__init__(name, cost, rarity)

        if not (isinstance(attack, int) and attack > 0):
            raise ValueError("Attack must be a positive integer")
        if not (isinstance(health, int) and health > 0):
            raise ValueError("Health must be a positive integer")

        self.attack = attack
        self.health = health

    def play(self, game_state: dict) -> dict:
        # Lógica de implementação: o que acontece ao jogar a carta
        # Você pode usar game_state para verificar mana disponível, se desejar
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield"
        }

    def attack_target(self, target) -> dict:
        target_name = (target if isinstance(target, str)
                       else getattr(target, 'name', "Unknown"))
        return {
            "attacker": self.name,
            "target": target_name,
            "damage_dealt": self.attack,
            "combat_resolved": True
        }
