from .Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int):
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health

    def play(self, game_state: dict) -> dict:
        if self.is_playable(game_state["available_mana"]):
            game_state["available_mana"]
            return {"card_played": self.name, 'mana_used': self.cost,
                    "effect": "Creature summon to battlefield"}
        return None

    def attack_target(self, target) -> dict:
        damage = self.attack
        if damage >= target.health:
            damage = target.health
        target.health -= damage
        return {"attacker": self.name, "target": target.name,
                "damage_dealt": damage, "combat_resolved": target.health <= 0}

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info["type"] = "Creature"
        info["attack"] = self.attack
        info["health"] = self.health
        return info
