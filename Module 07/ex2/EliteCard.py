from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
# EliteCard (Multiple Inheritance: Card + Combatable + Magical)


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name, cost, rarity,
                 attack_val, magic_power):
        super().__init__(name, cost, rarity)
        self.attack_val = attack_val
        self.magic_power = magic_power
        self.mana_pool = 0

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "type": "Elite",
            "effect": "Elite unit enters with combat and magic ready"
        }

    def attack(self, target) -> dict:
        return {
            "attacker": self.name, "target": str(target),
            "damage": self.attack_val
            }

    def defend(self, incoming_damage: int) -> dict:
        return {"defender": self.name, "damage_taken": incoming_damage}

    def get_combat_stats(self) -> dict:
        return {"attack": self.attack_val}

    # Implementação dos métodos de Magical
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        return {"caster": self.name, "spell": spell_name, "targets": targets}

    def channel_mana(self, amount: int) -> dict:
        self.mana_pool += amount
        return {"channeled": amount, "total_mana": self.mana_pool}

    def get_magic_stats(self) -> dict:
        return {"magic_power": self.magic_power, "mana_pool": self.mana_pool}
