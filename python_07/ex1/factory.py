from ex0.creature import Creature
from ex0.factory import CreatureFactory

from .creature import Bloomelle, Morphagon, Sproutling, Shiftling


class HealingCreatureFactory(CreatureFactory):
    """Factory for the healing family."""

    def create_base(self) -> Creature:
        return Sproutling()

    def create_evolved(self) -> Creature:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    """Factory for the transform family."""

    def create_base(self) -> Creature:
        return Shiftling()

    def create_evolved(self) -> Creature:
        return Morphagon()
