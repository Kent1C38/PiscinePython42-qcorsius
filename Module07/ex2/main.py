from .EliteCard import EliteCard


if __name__ == "__main__":
    arcane_warrior = EliteCard("Arcane Warrior", 7, "Legendary", 10, 13, 4, 3)

    print("Playing Arcane Warrior...")
    print(arcane_warrior.play({"available_mana": 100}))

    print("\nCombat phase:")
    print(f"Combat result: {arcane_warrior.attack('Dummy 1')}")
    print(f"Defense result: {arcane_warrior.defend(8)}")

    print("\nMagic phase:")
    print("Spell cast: " +
          f"{arcane_warrior.cast_spell('fireball', ['Dummy 1', 'Dummy 2'])}")
    print(f"Mana channel: {arcane_warrior.channel_mana(6)}")

    print("\nMultiple interface implementation successfull!")
