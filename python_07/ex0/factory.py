from abc import ABC, abstractmethod

from .creature import Creature, Flameling, Pyrodon, Aquabub, Torragon


class CreatureFactory(ABC):
    """Abstract factory for creating a creature family."""

    @abstractmethod
    def create_base(self) -> Creature:
        """Create the base creature for the family."""

    @abstractmethod
    def create_evolved(self) -> Creature:
        """Create the evolved creature for the family."""


class FlameFactory(CreatureFactory):
    """Factory for the flame family."""

    def create_base(self) -> Creature:
        return Flameling()

    def create_evolved(self) -> Creature:
        return Pyrodon()


class AquaFactory(CreatureFactory):
    """Factory for the aqua family."""

    def create_base(self) -> Creature:
        return Aquabub()

    def create_evolved(self) -> Creature:
        return Torragon()
