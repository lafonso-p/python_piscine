from ex0 import AquaFactory, CreatureFactory, FlameFactory


def test_factory(factory: CreatureFactory) -> None:
    print("testing factory")
    base = factory.create_base()
    evolved = factory.create_evolved()

    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


def test_battle(first_factory: FlameFactory,
                second_factory: AquaFactory) -> None:
    print("testing battle")
    first_creature = first_factory.create_base()
    second_creature = second_factory.create_base()

    print(f"{first_creature.describe()}\nvs\n"
          f"{second_creature.describe()}\nfight!")
    print(first_creature.attack())
    print(second_creature.attack())


def main() -> None:
    try:
        flame_factory = FlameFactory()
        aqua_factory = AquaFactory()

        test_factory(flame_factory)
        test_factory(aqua_factory)
        test_battle(flame_factory, aqua_factory)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
