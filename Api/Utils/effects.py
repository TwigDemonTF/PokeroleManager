EFFECT_REGISTRY = {
    "heal_pool": HealPoolEffect(),
}

class ItemEffect:
    def apply(self, user, target, data):
        raise NotImplementedError

class HealPoolEffect(ItemEffect):
    def apply(self, user, target, item, data, payload): 
        units = payload["units"]
        used = data.get("unitsUsed", 0)

        remaining = data["maxPool"] - used
        heal = min(units, remaining)

        target.hp = min(target.max_hp, target.hp + heal)
        data["unitsUsed"] += heal