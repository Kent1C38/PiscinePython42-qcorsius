from .Combatable import Combatable
from .Magical import Magical
from ..ex0.Card import Card


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str, health: int,
                 mana: int, attack: int, defense: int):
        super().__init__(name, cost, rarity)
        self.health = health
        self.mana = mana
        self.attack_points = attack
        self.defense_points = defense

    def play(self, game_state: dict) -> dict:
        if super().is_playable(game_state["available_mana"]):
            game_state["available_mana"] -= self.cost
            return {"card_played": self.name, 'mana_used': self.cost,
                    "effect": "Elite Creature summoned to battlefield"}
        return None

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        match spell_name:
            case "fireball":
                cost = 4
            case "lighning_bolt":
                cost = 5
            case _:
                from random import randint
                cost = randint(0, 6)

        self.mana -= cost
        return {"caster": self.name, "spell": spell_name, "targets": targets,
                "mana_used": cost}

    def channel_mana(self, amount: int) -> dict:
        self.mana += amount
        return {"channeled": amount, "total_mana": self.mana}

    def get_magic_stats(self) -> dict:
        return {"card_mana": self.mana}

    def attack(self, target) -> dict:
        return {"attacker": self.name, "target": target,
                "damage": self.attack_points,
                "combat_type": "melee"}

    def defend(self, incoming_damage: int):
        damage = incoming_damage - self.defense_points
        blocked = incoming_damage - damage
        if damage < 0:
            damage = 0
        self.health -= damage
        return {"defender": self.name, "damage_taken": damage,
                "damage_blocked": blocked, "still_alive": self.health > 0}

    def get_combat_stats(self) -> dict:
        return {"attack_points": self.attack, "defense_points": self.defense,
                "remaining_health": self.health}

    def get_card_info(self):
        info = super().get_card_info()
        info["health"] = self.health
        info["attack"] = self.attack_points
        info["defense"] = self.defense_points
        info["mana"] = self.mana
        return info
