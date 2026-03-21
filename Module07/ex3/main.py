from .GameEngine import GameEngine
from .FantasyCardFactory import FantasyCardFactory
from .AggressiveStrategy import AggressiveStrategy

if __name__ == "__main__":
    print("=== DataDeck Game Demo ===")

    print("\nConfiguring Fantasy Card Game...")
    engine = GameEngine()

    engine.configure_engine(FantasyCardFactory(), AggressiveStrategy())
    print(f"Factory: {engine.get_factory().__class__.__name__}")
    print(f"Strategy: {engine.get_strategy().get_strategy_name()}")

    engine.simulate_turn()

    print(f"\nGame Report:\n{engine.get_engine_status()}")
