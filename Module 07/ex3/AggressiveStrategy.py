from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        # Lógica: joga cartas de baixo custo primeiro e ataca
        cards_played = [card.name for card in hand if card.cost <= 3]
        return {
            "strategy": self.get_strategy_name(),
            "cards_played": cards_played,
            "mana_used": sum(c.cost for c in hand if c.name in cards_played),
            "targets_attacked": ["Enemy Player"],
            "damage_dealt": 8  # Valor exemplo para o relatório
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        # Prioriza o jogador adversário diretamente
        return ["Enemy Player"] + available_targets
