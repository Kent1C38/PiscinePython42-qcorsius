def full_import_demo():
    import alchemy.elements
    print("Method 1 - Full module import")
    print(
        "alchemy.elements.create_fire():" +
        f"{alchemy.elements.create_fire()}")


def specific_import_demo():
    from alchemy.elements import create_water
    print("Method 2 - Specific function import")
    print(f"create_water(): {create_water()}")


def aliased_import_demo():
    from alchemy.potions import healing_potion as heal
    print("Method 3 - Aliased import")
    print(f"heal(): {heal()}")


def multiple_import_demo():
    from alchemy.elements import create_earth, create_fire
    from alchemy.potions import strenght_potion
    print("Method 4 - Multiple imports")
    print(f"create_earth(): {create_earth()}")
    print(f"create_fire(): {create_fire()}")
    print(f"strenght_potion(): {strenght_potion()}")


if __name__ == "__main__":
    print("=== Import Transmutation Mastery ===")

    print()
    full_import_demo()

    print()
    specific_import_demo()

    print()
    aliased_import_demo()

    print()
    multiple_import_demo()
