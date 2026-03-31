from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def __init__(self):
        """Inicializa o motor do jogo sem configurações iniciais."""
        self.factory: CardFactory = None
        self.strategy: GameStrategy = None
        self.turns_simulated: int = 0
        self.total_damage_dealt: int = 0
        self.cards_created_count: int = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        """
        Configura o motor com uma fábrica de cartas e uma estratégia
        específicas.
        """
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        """
        Simula um turno de jogo criando cartas através da fábrica
        e executando a jogada via estratégia.
        """
        if not self.factory or not self.strategy:
            raise ValueError(
                "Engine must be configured with factory and strategy"
                )

        self.turns_simulated += 1

        # Cria uma mão de cartas temática usando a fábrica
        # Exemplo baseado na saída esperada: 1 Criatura, 1 Feitiço
        hand = [
            self.factory.create_creature("Fire Dragon"),
            self.factory.create_creature("Goblin Warrior"),
            self.factory.create_spell("Lightning Bolt")
        ]
        self.cards_created_count += len(hand)

        # Executa o turno usando a estratégia configurada
        turn_result = self.strategy.execute_turn(hand, [])

        # Acumula o dano para o relatório final
        self.total_damage_dealt += turn_result.get("damage_dealt", 0)

        return turn_result

    def get_engine_status(self) -> dict:
        """
        Retorna um relatório do estado atual e histórico da simulação.
        """
        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used":
            self.strategy.get_strategy_name() if self.strategy else None,
            "total_damage": self.total_damage_dealt,
            "cards_created": self.cards_created_count
        }
