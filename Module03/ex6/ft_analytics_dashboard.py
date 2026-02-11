class Player:
    def __init__(self, name: str):
        self._name = name

    def get_name(self) -> str:
        return self._name


if __name__ == "__main__":
    scores = {}
    achievements = {}
    players = []

    def add_player(player: Player, score: int, achievements_set: set):
        players.append(player)
        scores[player.get_name()] = score
        achievements[player.get_name()] = achievements_set

    add_player(Player("Alice"), 2500, {"first_kill", "survivor"})
    add_player(Player("Bob"), 300, {"doomed", "first_kill"})
    add_player(Player("Keith"), 6000, {"first_kill", "boss_slayer", "pk"})
    add_player(Player("Carole"), 1500, {"timber", "survivor"})

    print("=== Game Analytics Dashboard ===")

    print("\n=== List Comprehension Example ===")
