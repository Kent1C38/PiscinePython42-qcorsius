from ..ex0 import Card
from .Rankable import Rankable
from ..ex2 import Combatable
from random import randint


class TournamentCard(Card, Combatable, Rankable):

    def __init__(self, name: str, cost: int, rartity: str,
                 health: int, attack_dmg: int, defense: int, base_rating: int):
        super().__init__(name, cost, rartity)
        self.health = health
        self.attack_dmg = attack_dmg
        self.defense = defense
        self.rating = base_rating
        self.wins = 0
        self.losses = 0

    def play(self, game_state: dict) -> dict:
        pass

    def attack(self, target) -> dict:
        if isinstance(target, Combatable):
            real_damage = target.defend(self.attack_dmg).get("damage", 0)
            target.health -= real_damage
            return {"attacker": self.name, "defender": target.name,
                    "total_damage": real_damage}

        return {}

    def defend(self, incoming_damages: int) -> dict:
        damage = incoming_damages - \
            randint(incoming_damages // 2, incoming_damages)

        if damage > self.health:
            damage = self.health

        return {"damage": damage}

    def get_combat_stats(self) -> dict:
        return {"health": self.health, "attack_dmg": self.attack_dmg,
                "defense": self.defense}

    def calculate_rating(self) -> int:
        total_games = self.wins + self.losses
        if total_games == 0:
            return self.rating
        winrate = self.wins / total_games

        confidence = min(1.0, total_games / 50)

        adjusted_winrate = 0.5 + (winrate - 0.5) * confidence

        target_rating = 1000 + 1000 * (adjusted_winrate - 0.5)

        return int(self.rating + confidence * (target_rating - self.rating))

    def update_wins(self, wins: int) -> None:
        self.wins = wins

    def update_losses(self, losses: int) -> None:
        self.losses = losses

    def get_rank_info(self) -> dict:
        return {"rating": self.rating}

    def get_tournament_stats(self) -> dict:
        return {"wins": self.wins, "losses": self.losses}

    def get_ratio(self) -> float:
        return self.wins / max((self.wins + self.losses), 1)
