from .TournamentPlatform import TournamentPlatform
from .TournamentCard import TournamentCard

if __name__ == "__main__":
    print("=== DataDeck Tournament Platform ===")
    tournament = TournamentPlatform()

    print("\nRegistering Tournament Cards...")

    dragon = tournament.register_card(
        TournamentCard("Fire Dragon", 0, "", 15, 5, 6, 1250))

    wizard = tournament.register_card(
        TournamentCard("Water Wizard", 0, "", 10, 3, 5, 1000))

    print(f"Registered: {dragon}, {wizard}")

    print("\nCreating tournament match...")
    result = tournament.create_match(dragon, wizard)
    print(f"Match result: {result}")

    print("\nTournament Leaderboard:")
    for index, card in enumerate(tournament.get_leaderboard()):
        print(f"#{index + 1}: {card.name}, Rating: {card.rating} "
              f"({card.wins}W | {card.losses}L)")

    print("\nPlatform Report: ")
    print(tournament.generate_tournament_report())
