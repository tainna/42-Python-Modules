from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


def main():
    """
    Demonstração do Exercício 3: Game Engine.
    Integra o Abstract Factory Pattern com o Strategy Pattern.
    """
    print("DataDeck Game Engine")
    print("Configuring Fantasy Card Game...")

    # 1. Instanciação dos componentes (Fábrica e Estratégia)
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    engine = GameEngine()

    # 2. Configuração do motor de jogo (Injeção de Dependência)
    engine.configure_engine(factory, strategy)

    # 3. Exibição das configurações iniciais conforme o exemplo
    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.get_strategy_name()}")

    # Obtém e exibe os tipos suportados pela fábrica
    print(f"Available types: {factory.get_supported_types()}")

    print("\nSimulating aggressive turn...")

    # Simulação visual da "mão" para bater com a saída esperada
    # (O motor cria essas cartas internamente via fábrica)
    print("Hand: [Fire Dragon (5), Goblin Warrior (2), Lightning Bolt (3)]")

    # 4. Execução do turno através do motor
    turn_result = engine.simulate_turn()

    print("Turn execution:")
    print(f"Strategy: {turn_result['strategy']}")

    # Formatação manual do dicionário de ações para precisão na saída
    actions = {
        'cards_played': turn_result['cards_played'],
        'mana_used': turn_result['mana_used'],
        'targets_attacked': turn_result['targets_attacked'],
        'damage_dealt': turn_result['damage_dealt']
    }
    print(f"Actions: {actions}")

    # 5. Relatório final do estado do motor
    print("\nGame Report:")
    print(engine.get_engine_status())

    print(
        "\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!"
        )


if __name__ == "__main__":
    main()
