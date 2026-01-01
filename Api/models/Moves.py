from Api.extensions import database
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import relationship

from ..Enums.Move.DamageType import DamageTypeEnum
from ..Enums.Move.EffectLevel import EffectLevelEnum
from ..Enums.Move.HealMoveTypes import HealMoveTypesEnum
from ..Enums.Move.HitCount import HitCountEnum
from ..Enums.Move.Modifier import ModifierEnum
from ..Enums.Move.MoveEffectType import MoveEffectTypeEnum
from ..Enums.Move.MoveRangeTypes import MoveRangeTypesEnum
from ..Enums.Move.Priority import PriorityEnum
from ..Enums.Move.Target import TargetEnum
from ..Enums.Types import Types as TypeEnum
from ..Enums.WeatherTypes import WeatherTypes

class AccuracyModifierGroup(database.Model):
    __tablename__ = "AccuracyModifierGroup"
    id = database.Column(database.Integer, primary_key=True)
    accuracyModifier1 = database.Column(database.Enum(ModifierEnum), nullable=False)
    accuracyModifier2 = database.Column(database.Enum(ModifierEnum), nullable=True)
    accuracyModifier3 = database.Column(database.Enum(ModifierEnum), nullable=True)

    moves = relationship("Move", back_populates="accuracy_modifier_group")

class DamageModifierGroup(database.Model):
    __tablename__ = "DamageModifierGroup"
    id = database.Column(database.Integer, primary_key=True)
    damageModifier1 = database.Column(database.Enum(ModifierEnum), nullable=False)
    damageModifier2 = database.Column(database.Enum(ModifierEnum), nullable=True)
    damageModifier3 = database.Column(database.Enum(ModifierEnum), nullable=True)

    moves = relationship("Move", back_populates="damage_modifier_group", foreign_keys="[Move.damageModifiersId]")
    modified_by_moves = relationship("Move", back_populates="modified_damage_group", foreign_keys="[Move.modifiedDamageId]")

class HealMove(database.Model):
    __tablename__ = "HealMove"
    id = database.Column(database.Integer, primary_key=True)
    healType = database.Column(database.Enum(HealMoveTypesEnum), nullable=True)
    healAmount = database.Column(database.Integer, nullable=True)

    moves = relationship("Move", back_populates="heal_move")

class MoveEffect(database.Model):
    __tablename__ = "MoveEffect"
    id = database.Column(database.Integer, primary_key=True)
    effect = database.Column(database.Enum(MoveEffectTypeEnum), nullable=False)
    effectLevel = database.Column(database.Enum(EffectLevelEnum), nullable=False)
    effectLevelDice = database.Column(database.Integer, nullable=True)

    move_effect_connections = relationship("MoveEffectConnection", back_populates="move_effect", cascade="all, delete-orphan")

class MoveEffectConnection(database.Model):
    __tablename__ = "MoveEffectConnection"
    id = database.Column(database.Integer, primary_key=True)
    moveId = database.Column(database.Integer, database.ForeignKey("Move.id"), nullable=False)
    moveEffectId = database.Column(database.Integer, database.ForeignKey("MoveEffect.id"), nullable=False)

    move = relationship("Move", back_populates="effect_connections")
    move_effect = relationship("MoveEffect", back_populates="move_effect_connections")

    __table_args__ = (
        UniqueConstraint("moveId", "moveEffectId", name="uq_move_moveeffect"),
    )

class Move(database.Model):
    __tablename__ = "Move"
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(50), nullable=False)
    type = database.Column(database.Enum(TypeEnum), nullable=False)   # assumes TypeEnum exists in your code
    effectText = database.Column(database.Text, nullable=True)
    flavorText = database.Column(database.Text, nullable=True)
    damageType = database.Column(database.Enum(DamageTypeEnum), nullable=False, default=DamageTypeEnum.Physical)
    basePower = database.Column(database.Integer, nullable=True)
    priority = database.Column(database.Enum(PriorityEnum), nullable=True)
    target = database.Column(database.Enum(TargetEnum), nullable=True)
    moveRangeType = database.Column(database.Enum(MoveRangeTypesEnum), nullable=True)
    moveGridRange = database.Column(database.Integer, nullable=True, default=1)

    accuracyModifiersId = database.Column(database.Integer, database.ForeignKey("AccuracyModifierGroup.id"), nullable=True)
    accuracy_modifier_group = relationship("AccuracyModifierGroup", back_populates="moves")

    damageModifiersId = database.Column(database.Integer, database.ForeignKey("DamageModifierGroup.id"), nullable=True)
    damage_modifier_group = relationship("DamageModifierGroup", back_populates="moves", foreign_keys=[damageModifiersId])

    reducedAccuracy = database.Column(database.Integer, nullable=True)

    hasCritical = database.Column(database.Boolean, nullable=False, default=False)
    hasLethal = database.Column(database.Boolean, nullable=False, default=False)
    hasBlock = database.Column(database.Boolean, nullable=False, default=False)
    hasRecoil = database.Column(database.Boolean, nullable=False, default=False)
    hasWeatherChange = database.Column(database.Boolean, nullable=False, default=False)
    hasModifiedDamage = database.Column(database.Boolean, nullable=False, default=False)

    # if hasModifiedDamage True this references a DamageModifierGroup (or you could point to another table depending on semantics)
    modifiedDamageId = database.Column(database.Integer, database.ForeignKey("DamageModifierGroup.id"), nullable=True)
    damage_modifier_group = relationship(
        "DamageModifierGroup",
        back_populates="moves",
        foreign_keys=[damageModifiersId]
    ) 

    weatherChangeTo = database.Column(database.Enum(WeatherTypes), nullable=True)  # placeholder if you want a Weather Enum
    # NOTE: replace the previous line with actual Weather enum column, e.g. database.Column(database.Enum(WeatherEnum), nullable=True)

    alwaysHitEffect = database.Column(database.Boolean, nullable=False, default=False)
    alwaysFailEffect = database.Column(database.Boolean, nullable=False, default=False)
    isChargeMove = database.Column(database.Boolean, nullable=False, default=False)
    isFistBased = database.Column(database.Boolean, nullable=False, default=False)
    isHighCrit = database.Column(database.Boolean, nullable=False, default=False)
    isNeverFail = database.Column(database.Boolean, nullable=False, default=False)
    isHealingMove = database.Column(database.Boolean, nullable=False, default=False)
    isShieldMove = database.Column(database.Boolean, nullable=False, default=False)
    isSoundBased = database.Column(database.Boolean, nullable=False, default=False)
    isMultiHit = database.Column(database.Boolean, nullable=False, default=False)
    isSwitchMove = database.Column(database.Boolean, nullable=False, default=False)

    multiHitCount = database.Column(database.Enum(HitCountEnum), nullable=True)

    # healing type references HealMove
    healingTypeId = database.Column(database.Integer, database.ForeignKey("HealMove.id"), nullable=True)
    heal_move = relationship("HealMove", back_populates="moves")

    requiresRecharge = database.Column(database.Boolean, nullable=False, default=False)

    # relationships
    effect_connections = relationship("MoveEffectConnection", back_populates="move", cascade="all, delete-orphan")
    move_connections = relationship("MoveConnection", back_populates="move", cascade="all, delete-orphan")
    # if you want reverse link to pokemons, you can use an association pattern on MoveConnection (see below)

    # helper for modifiedDamage relationship (optional convenience)
    modified_damage_group = relationship("DamageModifierGroup", foreign_keys=[modifiedDamageId])

class MoveConnection(database.Model):
    __tablename__ = "MoveConnection"
    id = database.Column(database.Integer, primary_key=True)
    pokemonId = database.Column(database.Integer, database.ForeignKey("GamePokemon.id"), nullable=False)
    moveId = database.Column(database.Integer, database.ForeignKey("Move.id"), nullable=False)

    pokemon = relationship("GamePokemon", back_populates="move_connections")
    move = relationship("Move", back_populates="move_connections")

    __table_args__ = (
        UniqueConstraint("pokemonId", "moveId", name="uq_pokemon_move"),
    )