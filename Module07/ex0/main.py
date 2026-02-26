from .CreatureCard import CreatureCard


if __name__ == "__main__":
    print("=== DataDeck Card foundation ===")

    print("\nTesting Abstract Base Class Design")

    fire_dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    goblin_warrior = CreatureCard("Goblin Warrior", 3, "Common", 2, 2)

    print(f"\nCreatureCard Info:\n{fire_dragon.get_card_info()}")

    game_state = {"available_mana": 6}
    print("\nPlaying Fire Dragon with 6 mana available:")
    print(f"Playable: {fire_dragon.is_playable(game_state['available_mana'])}")
    print(f"Play result: {fire_dragon.play(game_state)}")

    print("\nFire Dragon attacks Goblin Warrior:")
    print(f"Attack result: {fire_dragon.attack_target(goblin_warrior)}")

    print("\nTesting insufficient mana (3 available):")
    print(f"Playable: {fire_dragon.is_playable(3)}")

    print("\nAbstract pattern successfully demonstrated!")
