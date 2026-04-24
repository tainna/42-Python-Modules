from abc import ABC, abstractmethod
from .creatures import Creature, Flameling, Pyrodon, Aquabub, Torragon


class CreatureFactory(ABC):
    """Abstract factory for creating creature families."""

    @abstractmethod
    def create_base(self) -> Creature:
        """Creates the base creature of the family."""
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        """Creates the evolved creature of the family."""
        pass


class FlameFactory(CreatureFactory):
    """Factory for the Fire family."""

    def create_base(self) -> Creature:
        return Flameling()

    def create_evolved(self) -> Creature:
        return Pyrodon()


class AquaFactory(CreatureFactory):
    """Factory for the Water family."""

    def create_base(self) -> Creature:
        return Aquabub()

    def create_evolved(self) -> Creature:
        return Torragon()
