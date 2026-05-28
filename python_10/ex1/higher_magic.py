from collections.abc import Callable


Spell = Callable[[str, int], str]
Condition = Callable[[str, int], bool]


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} fire damage"


def heal(target: str, power: int) -> str:
    return f"Heal restore {target} for {power} HP"


def freeze(target: str, power: int) -> str:
    return f"Freeze slows {target} for {power} seconds"


def spell_combiner(spell1: Spell, spell2: Spell) -> Callable:
    def wrapper(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return wrapper


def power_amplifier(base_spell: Spell, multiplier: int) -> Callable:
    def wrapper(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return wrapper


def conditional_caster(condition: Condition, spell: Spell) -> Callable:
    def wrapper(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"

    return wrapper


def spell_sequence(spells: list[Spell]) -> Callable:
    def wrapper(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]

    return wrapper


def main() -> None:
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    combined_result = combined("Dragon", 10)
    print(f"Combined spell result: {combined_result[0]}, {combined_result[1]}")
    print()

    print("Testing power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    print(f"Original: {fireball('Dragon', 10)}")
    print(f"Amplified: {mega_fireball('Dragon', 10)}")
    print()

    print("Testing conditional caster...")

    def strong_enough(_target: str, power: int) -> bool:
        return power >= 20

    conditional_fireball = conditional_caster(strong_enough, fireball)
    print(f"Power 15: {conditional_fireball('Goblin', 15)}")
    print(f"Power 20: {conditional_fireball('Goblin', 20)}")
    print()

    print("Testing spell sequence...")
    combo = spell_sequence([fireball, freeze, heal])
    for result in combo("Orc", 12):
        print(result)


if __name__ == "__main__":
    main()
