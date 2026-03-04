from ..ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        if self.is_playable(game_state["available_mana"]):
            return {"card_playerd": self.name, "mana_used": self.cost,
                    "effect": self.effect_type}
        return None

    def resolve_effect(self, targets: list) -> dict:
        return {"target_hits": targets, "effect": self.effect_type}

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info["effect_type"] = self.effect_type
        return info
