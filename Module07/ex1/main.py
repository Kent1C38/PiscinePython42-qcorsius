from .Deck import Deck
from ..ex0.Card import Card
from .ArtifactCard import ArtifactCard
from .SpellCard import SpellCard
from ..ex0.CreatureCard import CreatureCard

if __name__ == "__main__":
    print("=== DataDeck Deck Builder ===")

    print("\nBuilding deck with different card types...")
    deck = Deck()

    deck.add_card(CreatureCard("Fire Dragon", 5, "Legendary", 5, 7))
    deck.add_card(SpellCard("Lightning Bolt", 3,
                  "Rare", "Deals 3 damage to target"))
    deck.add_card(ArtifactCard("Mana Crystal", 2,
                  "Common", 5, "+1 Mana per turn"))

    print(f"Deck stats: {deck.get_deck_stats()}")

    game_state = {"available_mana": 100}
    print("\nDrawing and playing cards...")

    def get_type(card: Card) -> str:
        if isinstance(card, CreatureCard):
            return "Creature"
        if isinstance(card, SpellCard):
            return "Spell"
        if isinstance(card, ArtifactCard):
            return "Artifact"
        return "Unknown"

    while card := deck.draw_card():
        print(f"\nDrew {card.name} ({get_type(card)})")
        print(f"Play results: {card.play(game_state)}")

    print("\nPolymorphism in action: Same interface, different card behaviors!")
