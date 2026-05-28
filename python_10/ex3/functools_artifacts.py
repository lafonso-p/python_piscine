import functools
import operator
from collections.abc import Callable
from typing import Any


OperationFn = Callable[[int, int], int]


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    operations: dict[str, OperationFn] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min,
    }

    reducer = operations.get(operation)
    if reducer is None:
        raise ValueError("Unknown operation")

    return functools.reduce(reducer, spells)


def partial_enchanter(
    base_enchantment: Callable,
) -> dict[str, Callable]:
    return {
        "fire": functools.partial(base_enchantment, 50, "Fire"),
        "ice": functools.partial(base_enchantment, 50, "Ice"),
        "lightning": functools.partial(base_enchantment, 50, "Lightning"),
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def dispatch(spell: Any) -> str:
        return "Unknown spell type"

    @dispatch.register
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @dispatch.register
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @dispatch.register
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return dispatch


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"{element} enchantment on {target} with {power} power"


def main() -> None:
    print("Testing spell reducer...")
    values = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(values, 'add')}")
    print(f"Product: {spell_reducer(values, 'multiply')}")
    print(f"Max: {spell_reducer(values, 'max')}")
    print()

    print("Testing partial enchanter...")
    enchanters = partial_enchanter(base_enchantment)
    print(enchanters["fire"]("Sword"))
    print(enchanters["ice"]("Shield"))
    print(enchanters["lightning"]("Staff"))
    print()

    print("Testing memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print(f"Cache info: {memoized_fibonacci.cache_info()}")
    print()

    print("Testing spell dispatcher...")
    dispatch = spell_dispatcher()
    print(dispatch(42))
    print(dispatch("fireball"))
    print(dispatch(["fireball", "heal", "shield"]))
    print(dispatch({"type": "unknown"}))


if __name__ == "__main__":
    main()
