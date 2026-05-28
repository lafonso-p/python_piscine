from abc import ABC, abstractmethod
from typing import cast

from ex0.creature import Creature
from ex1.capabilities import HealCapability, TransformCapability


class InvalidStrategyCreatureError(Exception):
    """Raised when a strategy is used with an incompatible creature."""


class BattleStrategy(ABC):
    """Abstract battle strategy used during tournaments."""

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        """Return whether this strategy can be applied to the creature."""

    @abstractmethod
    def act(self, creature: Creature) -> list[str]:
        """Execute all actions for this strategy and return log lines."""


class NormalStrategy(BattleStrategy):
    """Strategy that only attacks and works for any creature."""

    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> list[str]:
        if not self.is_valid(creature):
            raise InvalidStrategyCreatureError(
                f"Invalid Creature '{creature.name}' for this normal strategy"
            )
        return [creature.attack()]


class AggressiveStrategy(BattleStrategy):
    """Strategy for creatures with transform capability."""

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> list[str]:
        if not self.is_valid(creature):
            raise InvalidStrategyCreatureError(
                f"Invalid Creature '{creature.name}' "
                "for this aggressive strategy"
            )

        transformed_creature = cast(TransformCapability, creature)
        return [
            transformed_creature.transform(),
            creature.attack(),
            transformed_creature.revert(),
        ]


class DefensiveStrategy(BattleStrategy):
    """Strategy for creatures with healing capability."""

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> list[str]:
        if not self.is_valid(creature):
            raise InvalidStrategyCreatureError(
                f"Invalid Creature '{creature.name}' "
                " for this defensive strategy"
            )

        healing_creature = cast(HealCapability, creature)
        return [creature.attack(), healing_creature.heal()]
