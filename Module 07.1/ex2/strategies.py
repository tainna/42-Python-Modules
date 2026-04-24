from abc import ABC, abstractmethod
from ex0.creatures import Creature
from ex1.capabilities import TransformCapability, HealCapability


class InvalidStrategyError(Exception):
    """Exception raised for invalid creature-strategy combinations."""
    pass


class BattleStrategy(ABC):
    """Abstract base class for battle strategies."""

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        """Checks if the creature is suitable for the strategy."""
        pass

    @abstractmethod
    def act(self, creature: Creature) -> None:
        """Executes the strategy's action."""
        pass


class NormalStrategy(BattleStrategy):
    """Strategy suitable for any creature."""

    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' for this normal strategy"
            )
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    """Strategy suitable for transforming creatures."""

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        cn = creature.name
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{cn}' for this aggressive strategy"
            )

        if isinstance(creature, TransformCapability):
            print(creature.transform())
            print(creature.attack())
            print(creature.revert())


class DefensiveStrategy(BattleStrategy):
    """Strategy suitable for healing creatures."""

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        cn = creature.name
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{cn}' for this defensive strategy"
            )

        print(creature.attack())
        if isinstance(creature, HealCapability):
            print(creature.heal())
