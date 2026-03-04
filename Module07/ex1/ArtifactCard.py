from ..ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, durability: int,
                 effect: str):
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        if self.is_playable(game_state["available_mana"]):
            return {"card_played": self.name, "mana_used": self.cost,
                    "effect": f"Permanent: {self.effect}"}
        return None

    def activate_ability(self) -> dict:
        return {"active_effect": self.effect, "durability": self.durability}

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info["durability"] = self.durability
        info["effect"] = self.effect
        return info
