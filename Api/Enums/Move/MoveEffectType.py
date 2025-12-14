from enum import Enum

class MoveEffectTypeEnum(Enum):
    DamageIncrease = "Damage Increase"
    DamageIncreaseDice = "Damage Increase Dice"
    DamageDecrease = "Damage Decrease"
    AccuracyIncrease = "Accuracy Increase"
    AccuracyDecrease = "Accuracy Decrease"
    EvasionIncrease = "Evasion Increase"
    EvasionDecrease = "Evasion Decrease"
    StrengthIncrease = "Strength Increase"
    StrengthDecrease = "Strength Decrease"
    InsightIncrease = "Insight Increase"
    InsightDecrease = "Insight Decrease"
    DexterityIncrease = "Dexterity Increase"
    DexterityDecrease = "Dexterity Decrease"
    SpecialIncrease = "Special Increase"
    SpecialDecrease = "Special Decrease"