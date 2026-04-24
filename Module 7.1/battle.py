from ex0 import CreatureFactory, FlameFactory, AquaFactory


def test_factory(factory: CreatureFactory) -> None:
    """Verifies that a factory can create and describe its creatures."""
    print("Testing factory")

    base = factory.create_base()
    print(base.describe())
    print(base.attack())

    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())


def fight(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    """Makes the base creatures of two factories fight."""
    print("Testing battle")

    base1 = factory1.create_base()
    base2 = factory2.create_base()

    print(base1.describe())
    print("VS.")
    print(base2.describe())
    print("fight!")

    print(base1.attack())
    print(base2.attack())


def main() -> None:
    # Instantiate the factories
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()

    # Test individual factories
    test_factory(flame_factory)
    test_factory(aqua_factory)

    # Test battle between base creatures
    fight(flame_factory, aqua_factory)


if __name__ == "__main__":
    main()
