from .CardFactory import CardFactory
from .GameStrategy import GameSrategy
from .FantasyCardFactory import FantasyCardFactory
from .AggressiveStrategy import AggressiveStrategy


class GameEngine():
    def configure_engine(self, factory: CardFactory,
                         strategy: GameSrategy) -> None:
        self.__factory = factory
        self.__strategy = strategy
        self.__status = {"turn_simulated": 0,
                         "strategy_used": self.__strategy.get_strategy_name(),
                         "total_damage": 0, "cards_created": 0}

    def simulate_turn(self) -> dict:
        print(f"\nSimulating turn with {self.__strategy.get_strategy_name()}")
        hand_dict = self.__factory.create_themed_deck(7)

        hand_list = []
        for card, nb in hand_dict.items():
            for _ in range(nb):
                hand_list.append(card)

        turn_result = self.__strategy.execute_turn(hand_list, ["Enemy Player"])
        self.__status["turn_simulated"] += 1
        self.__status["total_damage"] += turn_result["damage_dealt"]
        self.__status["cards_created"] += 7
        return turn_result

    def get_engine_status(self) -> dict:
        return self.__status


if __name__ == "__main__":
    engine = GameEngine()
    engine.configure_engine(FantasyCardFactory(), AggressiveStrategy())

    print("Turn Execution:")
    turn = engine.simulate_turn()
    engine.simulate_turn()
    engine.simulate_turn()
    print(f"\n{turn}")
    print(f"\nGame Report\n{engine.get_engine_status()}")
