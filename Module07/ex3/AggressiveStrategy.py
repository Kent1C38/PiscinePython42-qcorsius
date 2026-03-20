from ..ex0.CreatureCard import CreatureCard
from .GameStrategy import GameSrategy
from .FantasyCardFactory import FantasySpells


class AggressiveStrategy(GameSrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        available_mana = 10
        cards_played = []
        mana_used = 0
        damage = 0

        sorted_hand = sorted(hand, key=lambda x: x.cost)

        targets = self.prioritize_targets(["Enemy Player"])

        for card in sorted_hand:
            if card.cost <= available_mana:
                print(card.play({"available_mana": available_mana}))
                cards_played.append(card.name)
                available_mana -= card.cost
                mana_used += card.cost

                if hasattr(card, "attack"):
                    battlefield.append(card)
                if hasattr(card, "effect_type"):
                    for enum_card in FantasySpells:
                        if enum_card.get_card() == card:
                            damage += enum_card.get_power()
                    card.resolve_effect(targets)

        for creature in battlefield:
            if hasattr(creature, "attack"):
                damage += creature.attack

        return {
            "strategy": self.get_strategy_name(),
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": targets,
            "damage_dealt": damage
        }

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
