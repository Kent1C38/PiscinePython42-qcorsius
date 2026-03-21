from .TournamentCard import TournamentCard


class TournamentPlatform:

    def __init__(self):
        self.cards_registry = dict()
        self.played_matches = 0

    def register_card(self, card: TournamentCard) -> str:
        registered = False
        identifier = 0
        while not registered:
            card_id = card.name.lower() + f"{identifier}"
            card_id = card_id.replace(" ", "_")
            if card_id in self.cards_registry.keys():
                identifier += 1
            else:
                self.cards_registry[card_id] = card
                registered = True
                return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        if card1_id not in self.cards_registry.keys() and \
                card2_id not in self.cards_registry.keys():
            print("Could not create match: unknown ID")
            return {}

        card1: TournamentCard = self.cards_registry[card1_id]
        card2: TournamentCard = self.cards_registry[card2_id]

        winner = None
        loser = None

        while card1.health > 0 and card2.health > 0:
            card1.attack(card2)
            if card2.health <= 0:
                winner = card1
                loser = card2
                continue

            card2.attack(card1)
            if card1.health <= 0:
                winner = card2
                loser = card1
                continue

        winner.update_wins(winner.wins + 1)
        loser.update_losses(loser.losses + 1)

        winner.rating = winner.calculate_rating()
        loser.rating = loser.calculate_rating()

        self.played_matches += 1

        return {"winner": winner.name, "loser": loser.name,
                "winner_rating": winner.rating, "loser_rating": loser.rating}

    def get_leaderboard(self) -> list:
        cards_list = [card for card in self.cards_registry.values()]
        sorted_list = sorted(cards_list, key=lambda x: x.get_ratio(),
                             reverse=True)
        return sorted_list

    def generate_tournament_report(self) -> dict:
        ratings = [card.rating for card in self.cards_registry.values()]
        avg_rating = sum(ratings) / len(ratings)
        return {"total_cards": len(ratings),
                "match_played": self.played_matches,
                "avg_rating": avg_rating,
                "platform_status": "active"}
