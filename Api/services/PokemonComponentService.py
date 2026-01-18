from Api.extensions import database
from Api.models.Misc import Nature, Ability
from Api.models.Moves import Move, AccuracyModifierGroup, DamageModifierGroup
from Api.Enums.Types import Types as TypeEnum
from Api.Enums.Move import *
from Api.Utils.utils import getBooleanFields


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


def create_move(data):
    accuracy = AccuracyModifierGroup(
        accuracyModifier1=ModifierEnum[data["accuracyModifier1"]],
        accuracyModifier2=ModifierEnum[data["accuracyModifier2"]],
        accuracyModifier3=ModifierEnum[data["accuracyModifier3"]],
    )
    database.session.add(accuracy)
    database.session.flush()

    damage = DamageModifierGroup(
        damageModifier1=ModifierEnum[data["damageModifier1"]],
        damageModifier2=ModifierEnum[data["damageModifier2"]],
        damageModifier3=ModifierEnum[data["damageModifier3"]],
    )
    database.session.add(damage)
    database.session.flush()

    boolean_fields = {
        f: f in data for f in getBooleanFields()
    }

    move = Move(
        name=data["Name"],
        type=TypeEnum[data["types"]],
        damageType=DamageTypeEnum[data["damageTypes"]],
        priority=PriorityEnum(int(data["priority"])),
        target=TargetEnum[data["targets"]],
        moveRangeType=MoveRangeTypesEnum[data["moveRangeType"]],
        accuracyModifiersId=accuracy.id,
        damageModifiersId=damage.id,
        **boolean_fields
    )

    database.session.add(move)
    database.session.commit()
    return move.id
