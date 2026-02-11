class EventStats:
    def __init__(self):
        self.total_events = 0
        self.tresure_events = 0
        self.levelup_event = 0


class Player:
    def __init__(self, name: str, base_level: int):
        if self._is_name_valid(name) and self._is_base_level_valid(base_level):
            self._name = name
            self._level = base_level

    def get_name(self) -> str:
        return self._name

    def get_level(self) -> int:
        return self._level

    def level_up(self) -> None:
        self._level += 1

    def _is_name_valid(self, name: str) -> bool:
        return name is not None and name != ""

    def _is_base_level_valid(self, base_level: int) -> bool:
        return base_level >= 0


class Event:
    def __init__(self, ttype: str, player: Player):
        if self._is_valid_event(ttype, player):
            self._type = ttype
            self._player = player

    def get_type(self) -> str:
        return self._type

    def get_player(self) -> Player:
        return self._player

    def _is_valid_event(self, ttype: str, player: Player) -> bool:
        if player is not None:
            return ttype == "levelup" or ttype == "treasure" or ttype == "kill"
        return False

    def apply(self) -> None:
        if self.get_type() == "levelup":
            self.get_player().level_up()

    def log(self) -> None:
        match self.get_type():
            case "levelup":
                print(f"{self.get_player().get_name()} leveled up " +
                      f"({self.get_player().get_level()} -> " +
                      f"{self.get_player().get_level() + 1})")
            case "treasure":
                print(f"{self.get_player().get_name()} found a treasure")
            case "kill":
                print(f"{self.get_player().get_name()} killed a monster")
            case _:
                print("Unknown Event")


def gen_event(player_list: list) -> Event:
    events = ["levelup", "treasure", "kill"]
    gen_call = 0
    while True:
        event = Event(events[gen_call % len(events)],
                      player_list[gen_call % len(player_list)])
        event.log()
        event.apply()
        gen_call += 1
        yield event


if __name__ == "__main__":
    history = []
    players = [Player("Alice", 1), Player("Bob", 5), Player("Alex", 2),
               Player("Carole", 10), Player("Camille", 6)]
    generator = gen_event(players)
    for i in range(1000):
        event = next(generator)
        history += [event]
