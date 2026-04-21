import ex0
from ex0.AbstractFactory import CreatureFactory


def check_creaure_creation(factory: CreatureFactory) -> None:
    print("Testing factory...")
    base = factory.create_base()
    evolved = factory.create_evolved()
    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


def battle_base_test(fac1: CreatureFactory, fac2: CreatureFactory) -> None:
    print("Testing battle...")
    base1 = fac1.create_base()
    base2 = fac2.create_base()
    print(f"{base1.describe()}\n vs\n{base2.describe()}\n fight!")
    print(base1.attack())
    print(base2.attack())


if __name__ == "__main__":
    fire_fac = ex0.FlameFactory()
    water_fac = ex0.AquaFactory()

    check_creaure_creation(fire_fac)

    print()

    check_creaure_creation(water_fac)

    print()

    battle_base_test(fire_fac, water_fac)
