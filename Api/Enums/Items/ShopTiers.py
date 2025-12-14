from enum import Enum

class ShopTierEnum(Enum):
    BASIC = "Basic Tier"                 # Poké Balls, Potions, Antidotes
    COMMON = "Common Tier"               # Super Potions, Status Heals, Repels
    ADVANCED = "Advanced Tier"           # Hyper Potions, Revives, Great Balls
    ELITE = "Elite Tier"                 # Max Potions, Full Restores, Ultra Balls
    EXPERT = "Expert Tier"               # Max Revives, Ability Capsules, Battle Items
    LEGENDARY = "Legendary Tier"         # Mega Stones, Z-Crystals, Rare Held Items
    MYTHIC = "Mythic Tier"               # Primal Orbs, Z-Moves Variants, Ultra-Necrozma items
    DIVINE = "Divine Tier"               # One-of-a-kind items, custom Mega Stones, Arceus Plates