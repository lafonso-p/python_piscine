from ex0.creature import Creature

from .capabilities import HealCapability, TransformCapability


class Sproutling(Creature, HealCapability):
    """Base creature for the healing family."""

    def __init__(self) -> None:
        super().__init__("Sproutling", "Grass")

    def attack(self) -> str:
        return "Sproutling uses Vine Whip!"

    def heal(self, target: str | None = None) -> str:
        if target is None:
            return "Sproutling heals itself for a small amount"
        return f"Sproutling heals {target} for a small amount"


class Bloomelle(Creature, HealCapability):
    """Evolved creature for the healing family."""

    def __init__(self) -> None:
        super().__init__("Bloomelle", "Grass/Fairy")

    def attack(self) -> str:
        return "Bloomelle uses Petal Dance!"

    def heal(self, target: str | None = None) -> str:
        if target is None:
            return "Bloomelle heals itself and others for a large amount"
        return f"Bloomelle heals {target} for a large amount"


class Shiftling(Creature, TransformCapability):
    """Base creature for the transform family."""

    def __init__(self) -> None:
        super().__init__("Shiftling", "Normal")
        self.is_transformed: bool = False

    def attack(self) -> str:
        if self.is_transformed:
            return "Shiftling performs a boosted strike!"
        return "Shiftling attacks normally."

    def transform(self) -> str:
        self.is_transformed = True
        return "Shiftling shifts into a sharper form!"

    def revert(self) -> str:
        self.is_transformed = False
        return "Shiftling returns to normal."


class Morphagon(Creature, TransformCapability):
    """Evolved creature for the transform family."""

    def __init__(self) -> None:
        super().__init__("Morphagon", "Normal/Dragon")
        self.is_transformed: bool = False

    def attack(self) -> str:
        if self.is_transformed:
            return "Morphagon unleashes a devastating morph strike!"
        return "Morphagon attacks normally."

    def transform(self) -> str:
        self.is_transformed = True
        return "Morphagon morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.is_transformed = False
        return "Morphagon stabilizes its form."
