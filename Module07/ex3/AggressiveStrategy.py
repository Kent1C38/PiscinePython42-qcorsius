from ..ex0.CreatureCard import CreatureCard
from .GameStrategy import GameSrategy


class AggressiveStrategy(GameSrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        sorted_hand = sorted(hand, key=lambda x: x.cost)

        print([x.name for x in sorted_hand])

    def get_strategy_name(self) -> str:
        return "Aggressive Strategy"

    def prioritize_targets(self, available_targets: list) -> list:
        if "Enemy Player" in available_targets:
            return ["Enemy Player"]
        else:
            from random import randint
            return available_targets[randint(0, len(available_targets))]


if __name__ == "__main__":
    li = [CreatureCard("t1", 5, "none", 5, 0), CreatureCard(
        "t2", 16, "none", 5, 0), CreatureCard("t3", 8, "none", 5, 0)]
    strat = AggressiveStrategy()
    strat.execute_turn(li, [])
