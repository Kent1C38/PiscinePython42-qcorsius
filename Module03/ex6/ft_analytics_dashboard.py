class Player:
    def __init__(self, name: str, score: int, achievements: set[str]) -> None:
        self.__name = name
        self.__score = score
        self.__achievements = achievements

    def get_name(self) -> str:
        return self.__name

    def get_score(self) -> int:
        return self.__score

    def get_achievements(self) -> set[str]:
        return self.__achievements


def list_comprehension_tests(players_list: list[Player]) -> None:
    print("\n=== List Comprehension Examples ===")

    high_scorers = [x.get_name() for x in players_list if x.get_score() > 2000]
    print(f"High scorers (>2000): {high_scorers}")

    doubled_scores = [x.get_score() * 2 for x in players_list]
    print(f"Doubled scores: {doubled_scores}")

    player_names = [x.get_name() for x in players_list]
    print(f"Active players: {player_names}")


def dict_comprehension_tests(players_list: list[Player]) -> None:
    print("\n=== Dict Comprehension Examples ===")

    player_scores = {x.get_name(): x.get_score() for x in players}
    print(f"Player scores: {player_scores}")

    categories = {
        "high": lambda s: s > 1500,
        "medium": lambda s: 750 <= s <= 1500,
        "low": lambda s: s < 750,
    }
    stats_categories = {
        cat_name: len([s for s in player_scores.values() if condition(s)])
        for cat_name, condition in categories.items()
    }
    print(f"Score categories: {stats_categories}")

    achievement_count = {
        player.get_name(): len(player.get_achievements()) for player in players
    }
    print(f"Achievement count: {achievement_count}")


def set_comprehension_tests(players_list: list[Player]) -> None:
    print("\n=== Set Comprehension Examples ===")

    unique_achievements = {
        achievement
        for player in players_list
        for achievement in player.get_achievements()
    }
    print(f"Unique achievements: {unique_achievements}")


def show_global_analytics(players_list: list[Player]) -> None:
    print("\n=== Global Analysis ===")
    total_players = len(players_list)
    print(f"Total players: {total_players}")
    avg = sum([x.get_score() for x in players_list]) / total_players
    print(f"Average score: {avg}")
    top_score = max([player.get_score() for player in players_list])
    top_performers = [
        player for player in players_list if player.get_score() == top_score
    ]
    print(f"Top performer: {top_performers[0].get_name()} ({top_score}pts)")


if __name__ == "__main__":
    players: list[Player] = []

    def create_player(name: str, score: int, achievements_set: set):
        players.append(Player(name, score, achievements_set))

    create_player("Alice", 2500, {"first_kill", "survivor"})
    create_player("Bob", 300, {"doomed", "first_kill"})
    create_player("Keith", 6000, {"first_kill", "boss_slayer", "pk"})
    create_player("Carole", 1500, {"timber", "survivor"})

    print("=== Game Analytics Dashboard ===")

    list_comprehension_tests(players)

    dict_comprehension_tests(players)

    set_comprehension_tests(players)

    show_global_analytics(players)
