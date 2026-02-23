if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")

    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {'level_10', 'treasure_hunter', 'boss_slayer',
               'speed_demon', 'perfectionist'}

    print(f"Player Alice achievements: {alice}")
    print(f"Player Bob achievements: {bob}")
    print(f"Player Charlie achievements: {charlie}")

    print("\n=== Achievement Analytics ===")

    unique = alice | bob | charlie
    print(f"All unique achievements: {unique}")
    print(f"Total unique achievements: {len(unique)}")

    common = alice & bob & charlie
    print(f"\nCommon to all players: {common}")

    print(f"Alice VS Bob common: {alice & bob}")
    print(f"Alice unique: {alice - bob}")
    print(f"Bob unique: {bob - alice}")
