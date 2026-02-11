class EventStats:
    def __init__(self):
        self.total_events = 0
        self.treasure_events = 0
        self.levelup_event = 0
        self.kill_events = 0

    def infos(self):
        print(f"Total events processed: {self.total_events}")
        print(f"Level up events: {self.levelup_event}")
        print(f"Treasure found events: {self.treasure_events}")
        print(f"Monster killed events: {self.kill_events}")


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

    def apply(self, stats: EventStats) -> None:
        match self.get_type():
            case "levelup":
                self.get_player().level_up()
                stats.levelup_event += 1
            case "treasure":
                stats.treasure_events += 1
            case "kill":
                stats.kill_events += 1
            case _:
                print("Cannot apply event: Unknown")
        stats.total_events += 1

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


def fibonacci_sequence():
    fibo = [0, 1]
    curr = 0
    while True:
        if curr >= len(fibo):
            fibo += [fibo[curr - 2] + fibo[curr - 1]]
        yield fibo[curr]
        curr += 1


def prime_sequence():
    curr = 2
    while True:
        is_prime = True
        limit = curr ** 0.5
        i = 2

        while i <= limit:
            if curr % i == 0:
                is_prime = False
                break
            i += 1

        if is_prime:
            yield curr
        curr += 1


def gen_event(player_list: list, stats: EventStats) -> Event:
    events = ["levelup", "treasure", "kill"]
    gen_call = 0
    while True:
        event = Event(events[gen_call % len(events)],
                      player_list[gen_call % len(player_list)])
        event.log()
        event.apply(stats)
        gen_call += 1
        yield event


if __name__ == "__main__":
    history = []
    stats = EventStats()
    players = [Player("Alice", 1), Player("Bob", 5), Player("Alex", 2),
               Player("Carole", 10), Player("Camille", 6)]
    generator = gen_event(players, stats)
    tests_number = 1000

    print("=== Game Data Stream Processor ===")
    print("\nProcessing {tests_number} events...\n")
    for i in range(tests_number):
        event = next(generator)
        history += [event]

    print("\n=== Stream Analytics ===")
    stats.infos()

    print("\n=== Generator Demo ===")
    fibo_sequ = fibonacci_sequence()
    fibo = []
    for y in range(10):
        fibo += [next(fibo_sequ)]
    print(f"Fibonacci sequence (10 first): {fibo}")

    prime_sequ = prime_sequence()
    primes = []
    for z in range(10):
        primes += [next(prime_sequ)]
    print(f"Prime numbers (10 first): {primes}")
