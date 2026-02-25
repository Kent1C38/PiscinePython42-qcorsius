import alchemy.transmutation

if __name__ == "__main__":
    print("=== Pathway Debate Mastery ===")

    print("\nTesting Absolute Imports (from basic.py):")
    print(f"lead_to_gold(): {alchemy.transmutation.lead_to_gold()}")
    print(f"stone_to_gem(): {alchemy.transmutation.stone_to_gem()}")

    print("\nTesting Relative Imports (from advanced.py):")
    print(
        f"philosophers_stone(): {alchemy.transmutation.philosophers_stone()}")
    print(f"elixir_of_life(): {alchemy.transmutation.elixir_of_life()}")

    print("\nTesting Package Access:")
    print(
        "alchemy.transmutation.lead_to_gold(): " +
        f"{alchemy.transmutation.lead_to_gold()}")
    print("alchemy.transmutation.philosophers_stone(): " +
          f"{alchemy.transmutation.philosophers_stone()}")

    print("\nBoth pathways work! Absolute: clear, Relative: concise")
