from random import shuffle
from ..ex0.Card import Card
from ..ex0.CreatureCard import CreatureCard
from .ArtifactCard import ArtifactCard
from .SpellCard import SpellCard


class Deck:
    def __init__(self):
        self.cards = []

    def add_card(self, card: Card):
        self.cards.append(card)

    def remove_card(self, name: str) -> bool:
        for i, card in enumerate(self.cards):
            if name == card.name:
                self.cards.pop(i)
                return True
        return False

    def shuffle(self) -> None:
        shuffle(self.cards)

    def draw_card(self) -> Card:
        if self.cards:
            return self.cards.pop(0)
        return None

    def get_deck_stats(self) -> dict:
        stats = {"total_cards": len(self.cards), "creatures": 0, "spells": 0,
                 "artifacts": 0, "avg_cost": 0}
        deck_cost = 0
        for card in self.cards:
            if isinstance(card, CreatureCard):
                stats["creatures"] += 1
            elif isinstance(card, SpellCard):
                stats["spells"] += 1
            elif isinstance(card, ArtifactCard):
                stats["artifacts"] += 1
            else:
                try:
                    stats["unknown"] += 1
                except KeyError:
                    stats["unknown"] = 1
            deck_cost += card.cost
        try:
            stats["avg_cost"] = round(deck_cost / len(self.cards), 2)
        except ZeroDivisionError:
            stats["avg_cost"] = 0

        return stats
