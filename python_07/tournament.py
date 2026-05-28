from ex0 import AquaFactory, CreatureFactory, FlameFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    AggressiveStrategy,
    BattleStrategy,
    DefensiveStrategy,
    InvalidStrategyCreatureError,
    NormalStrategy,
)

Opponent = tuple[CreatureFactory, BattleStrategy]


def strategy_label(strategy: BattleStrategy) -> str:
    """Map strategy instances to short display names."""
    if isinstance(strategy, NormalStrategy):
        return "Normal"
    if isinstance(strategy, AggressiveStrategy):
        return "Aggressive"
    if isinstance(strategy, DefensiveStrategy):
        return "Defensive"
    return strategy.__class__.__name__


def describe_opponents(opponents: list[Opponent]) -> str:
    """Return a compact list describing each tournament opponent."""
    labels: list[str] = []
    for factory, strategy in opponents:
        if isinstance(factory, HealingCreatureFactory):
            opponent_name = "Healing"
        elif isinstance(factory, TransformCreatureFactory):
            opponent_name = "Transform"
        else:
            opponent_name = factory.create_base().name
        labels.append(f"({opponent_name}+{strategy_label(strategy)})")
    return "[ " + ", ".join(labels) + " ]"


def battle(opponents: list[Opponent]) -> None:
    """Run a round-robin tournament with strategy-aware actions."""
    print(describe_opponents(opponents))
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    try:
        for first_index, first_opponent in enumerate(opponents):
            for second_opponent in opponents[first_index + 1:]:
                first_factory, first_strategy = first_opponent
                second_factory, second_strategy = second_opponent

                first_creature = first_factory.create_base()
                second_creature = second_factory.create_base()

                print("\n* Battle *")
                print(first_creature.describe())
                print(" vs.")
                print(second_creature.describe())
                print(" now fight!")

                for action in first_strategy.act(first_creature):
                    print(action)
                for action in second_strategy.act(second_creature):
                    print(action)
    except InvalidStrategyCreatureError as error:
        print(f"Battle error, aborting tournament: {error}")


def main() -> None:
    """Run the three sample tournament configurations."""
    normal_strategy = NormalStrategy()
    aggressive_strategy = AggressiveStrategy()
    defensive_strategy = DefensiveStrategy()

    tournament_zero: list[Opponent] = [
        (FlameFactory(), normal_strategy),
        (HealingCreatureFactory(), defensive_strategy),
    ]
    tournament_one: list[Opponent] = [
        (FlameFactory(), aggressive_strategy),
        (HealingCreatureFactory(), defensive_strategy),
    ]
    tournament_two: list[Opponent] = [
        (AquaFactory(), normal_strategy),
        (HealingCreatureFactory(), defensive_strategy),
        (TransformCreatureFactory(), aggressive_strategy),
    ]

    print("Tournament 0 (basic)")
    battle(tournament_zero)
    print()

    print("Tournament 1 (error)")
    battle(tournament_one)
    print()

    print("Tournament 2 (multiple)")
    battle(tournament_two)


if __name__ == "__main__":
    main()
