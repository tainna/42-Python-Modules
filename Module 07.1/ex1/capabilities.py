from abc import ABC, abstractmethod


class HealCapability(ABC):
    """Abstract capability for healing."""

    @abstractmethod
    def heal(self) -> str:
        """Heals the creature or target."""
        pass


class TransformCapability(ABC):
    """Abstract capability for transforming."""

    def __init__(self) -> None:
        self.is_transformed: bool = False

    @abstractmethod
    def transform(self) -> str:
        """Transforms the creature."""
        pass

    @abstractmethod
    def revert(self) -> str:
        """Reverts the creature to its normal form."""
        pass
