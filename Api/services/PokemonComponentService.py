from Api.extensions import database
from Api.models.Misc import Nature, Ability
from Api.models.Moves import Move, AccuracyModifierGroup, DamageModifierGroup
from Api.Enums.Types import Types as TypeEnum
from Api.Utils.utils import getBooleanFields
from sqlalchemy import Boolean, inspect

from ..Enums.Move.DamageType import DamageTypeEnum
from ..Enums.Move.EffectLevel import EffectLevelEnum
from ..Enums.Move.HealMoveTypes import HealMoveTypesEnum
from ..Enums.Move.HitCount import HitCountEnum
from ..Enums.Move.Modifier import ModifierEnum
from ..Enums.Move.MoveEffectType import MoveEffectTypeEnum
from ..Enums.Move.MoveRangeTypes import MoveRangeTypesEnum
from ..Enums.Move.Priority import PriorityEnum
from ..Enums.Move.Target import TargetEnum

def create_nature(data):
    database.session.add(Nature(
        name=data.get("Name"),
        description=data.get("Description")
    ))
    database.session.commit()


def create_ability(data):
    database.session.add(Ability(
        name=data.get("Name"),
        flavorText=data.get("FlavorText"),
        effect=data.get("Effect")
    ))
    database.session.commit()

def modifier_from_data(value):
    if value is None or value == "" or value == "None":
        return ModifierEnum.NONE

    return ModifierEnum(value)

def modifier_from_data(value):
    if value is None or value == "" or value == "None":
        return ModifierEnum.NONE

    return ModifierEnum(value)


def create_move(data):

    accuracy = AccuracyModifierGroup(
        accuracyModifier1=modifier_from_data(data["accuracyModifier1"]),
        accuracyModifier2=modifier_from_data(data["accuracyModifier2"]),
        accuracyModifier3=modifier_from_data(data["accuracyModifier3"]),
    )

    database.session.add(accuracy)
    database.session.flush()

    damage = DamageModifierGroup(
        damageModifier1=modifier_from_data(data["damageModifier1"]),
        damageModifier2=modifier_from_data(data["damageModifier2"]),
        damageModifier3=modifier_from_data(data["damageModifier3"]),
    )

    database.session.add(damage)
    database.session.flush()

    boolean_fields = {
        f: f in data for f in getBooleanFields()
    }

    move = Move(
        name=data["Name"],
        type=TypeEnum(data["types"]),
        damageType=DamageTypeEnum(data["damageTypes"]),
        priority=PriorityEnum(data["priority"]),
        target=TargetEnum(data["targets"]),
        moveRangeType=MoveRangeTypesEnum(data["moveRangeType"]),
        accuracyModifiersId=accuracy.id,
        damageModifiersId=damage.id,
        **boolean_fields
    )

    database.session.add(move)
    database.session.commit()

    return move.id

def getMoveEnumData():
    mapper = inspect(Move)

    boolean_fields = [
        column.key
        for column in mapper.columns
        if isinstance(column.type, Boolean)
    ]

    data = {
        "types": enum_to_dict(TypeEnum),
        "damageTypes": enum_to_dict(DamageTypeEnum),
        "priority": enum_to_dict(PriorityEnum),
        "targets": enum_to_dict(TargetEnum),
        "moveRangeTypesEnum": enum_to_dict(MoveRangeTypesEnum),
        "multiHits": enum_to_dict(HitCountEnum),
        "healTypes": enum_to_dict(HealMoveTypesEnum),
        "accuracyModifiers": enum_to_dict(ModifierEnum),
        "damageModifiers": enum_to_dict(ModifierEnum),
        "booleanFields": boolean_fields,
    }
    
    return data

def enum_to_dict(enum_class):
    return [
        {
            "key": item.name,
            "value": item.value
        }
        for item in enum_class
    ]