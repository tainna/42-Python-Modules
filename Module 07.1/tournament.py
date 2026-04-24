from typing import List, Tuple
from ex0.factories import CreatureFactory, FlameFactory, AquaFactory
from ex1.factories import HealingCreatureFactory, TransformCreatureFactory
from ex2.strategies import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
    InvalidStrategyError
)


def run_tournament(opponents:
                   List[Tuple[CreatureFactory, BattleStrategy]]) -> None:
    """Runs a tournament where each opponent fights all others once."""
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            print("\n* Battle *")
            fac1, strat1 = opponents[i]
            fac2, strat2 = opponents[j]

            c1 = fac1.create_base()
            c2 = fac2.create_base()

            print(c1.describe())
            print("VS.")
            print(c2.describe())
            print("now fight!")

            try:
                strat1.act(c1)
                strat2.act(c2)
            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


def main() -> None:
    """Main testing function."""
    flame_fac = FlameFactory()
    aqua_fac = AquaFactory()
    heal_fac = HealingCreatureFactory()
    trans_fac = TransformCreatureFactory()

    norm_strat = NormalStrategy()
    aggro_strat = AggressiveStrategy()
    def_strat = DefensiveStrategy()

    print("Tournament 0 (basic)")
    print("[(Flameling+Normal), (Healing+Defensive)]")
    run_tournament([(flame_fac, norm_strat), (heal_fac, def_strat)])

    print("\nTournament 1 (error)")
    print("[(Flameling+Aggressive), (Healing+Defensive)]")
    run_tournament([(flame_fac, aggro_strat), (heal_fac, def_strat)])

    print("\nTournament 2 (multiple)")
    print("[(Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive)]")
    run_tournament([
        (aqua_fac, norm_strat),
        (heal_fac, def_strat),
        (trans_fac, aggro_strat)
    ])


if __name__ == "__main__":
    main()
