from alchemy.grimoire import validate_ingredients, record_spell

if __name__ == "__main__":
    print("=== Circular Curse Breaking ===")

    print("\nTesting ingredient validation:")
    print("validate_ingredients(\"fire air\"): " +
          f"{validate_ingredients('fire air')}")
    print("validate_ingredients(\"dragon scales\"): " +
          f"{validate_ingredients('dragon scales')}")

    print("\nTesting recording with validation:")
    print("record_spell(\"Fireball\", \"fire air\"): " +
          f"{record_spell('Fireball', 'fire air')}")
    print("record_spell(\"Dark Magic\", \"shadow\"): " +
          f"{record_spell('Dark Magic', 'shadow')}")

    print("\nCircular dependency curse avoided using late imports!")
    print("All spells processed safely!")
