import ex0

if __name__ == "__main__":
    fire_fac = ex0.FlameFactory()
    water_fac = ex0.AquaFactory()

    print("Testing factory")
    flameling = fire_fac.create_base()
    pyrodon = fire_fac.create_evolved()
    print(flameling.describe())
    print(flameling.attack())
    print(pyrodon.describe())
    print(pyrodon.attack())

    print("\nTesting factory")
    aquabub = water_fac.create_base()
    torragon = water_fac.create_evolved()
    print(aquabub.describe())
    print(aquabub.attack())
    print(torragon.describe())
    print(torragon.attack())

    print("\nTesting Battle")
    print(f"{flameling.describe()}\n vs\n{aquabub.describe()}")
    print(" fight!")
    print(flameling.attack())
    print(aquabub.attack())
