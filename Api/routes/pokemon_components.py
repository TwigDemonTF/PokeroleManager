from flask import request, jsonify
from flask_restful import Resource

from Api.extensions import database
from ..models.Misc import Nature, Ability
from ..models.Items import Garment
from ..models.Moves import Move, AccuracyModifierGroup, DamageModifierGroup

from ..Enums.Move.Priority import PriorityEnum
from ..Enums.Move.DamageType import DamageTypeEnum
from ..Enums.Move.Target import TargetEnum
from ..Enums.Move.HitCount import HitCountEnum
from ..Enums.Move.DamageType import DamageTypeEnum

from ..Enums.Types import Types as TypeEnum

from ..Enums.Move.HealMoveTypes import HealMoveTypesEnum
from ..Enums.Move.Modifier import ModifierEnum

from ..Utils.utils import enum_to_dict_list, getBooleanFields

class NatureApi(Resource):
    def post(self):
        data = request.get_json()

        newNature = Nature(
            name=data.get("Name"),
            description=data.get("Description"),
        )
        database.session.add(newNature)
        database.session.commit()
    
    def get(self):
        natures = Nature.query.all()

        data = [{"id": None, "name": "None"}]

        for n in natures:
            data.append({
                "id": n.id,
                "name": n.name
            })

        return jsonify(data)

class AbilityApi(Resource):
    def post(self):
        data = request.get_json()

        newAbility = Ability(
            name=data.get("Name"),
            flavorText=data.get("FlavorText"),
            effect=data.get("Effect")
        )
        database.session.add(newAbility)
        database.session.commit()

    def get(self):
        abilities = Ability.query.all()

        data = [{"id": None, "name": "None"}]

        for a in abilities:
            data.append({
                "id": a.id,
                "name": a.name
            })

        return jsonify(data)

class GarmentApi(Resource):
    def get(self):
        garments = Garment.query.all()

        data = [{"id": None, "name": "None"}]

        for g in garments:
            data.append({
                "id": g.id,
                "name": g.name
            })

        return jsonify(data)

class MoveApi(Resource):
    def get(self):
        data = {
            "types": enum_to_dict_list(TypeEnum),
            "damageTypes": enum_to_dict_list(DamageTypeEnum),
            "priority": enum_to_dict_list(PriorityEnum),
            "targets": enum_to_dict_list(TargetEnum),
            "multiHits": enum_to_dict_list(HitCountEnum),
            "healTypes": enum_to_dict_list(HealMoveTypesEnum),
            "accuracyModifiers": enum_to_dict_list(ModifierEnum),
            "damageModifiers":  enum_to_dict_list(ModifierEnum),
            "booleanFields": getBooleanFields()
        }

        return data, 200
    def post(self):
        data = request.get_json()

        print(data)

        # --- 1. Create AccuracyModifierGroup ---
        accuracy_group = AccuracyModifierGroup(
            accuracyModifier1=ModifierEnum[data["accuracyModifier1"]],
            accuracyModifier2=ModifierEnum[data["accuracyModifier2"]],
            accuracyModifier3=ModifierEnum[data["accuracyModifier3"]],
        )
        database.session.add(accuracy_group)
        database.session.flush()  # Flush to get accuracy_group.id

        # --- 2. Create DamageModifierGroup ---
        damage_group = DamageModifierGroup(
            damageModifier1=ModifierEnum[data["damageModifier1"]],
            damageModifier2=ModifierEnum[data["damageModifier2"]],
            damageModifier3=ModifierEnum[data["damageModifier3"]],
        )
        database.session.add(damage_group)
        database.session.flush()  # Flush to get damage_group.id

        booleanFields = getBooleanFields()
        def parse_bool(key):
            return key in data
        
        boolean_values = {field: parse_bool(field) for field in booleanFields}

        # --- 3. Create Move ---
        move = Move(
            name=data["Name"],
            effectText=data.get("effectText"),
            flavorText=data.get("flavorText"),
            basePower=int(data.get("basePower", 0)),
            reducedAccuracy=int(data.get("reducedAccuracy", 0)),
            type=TypeEnum[data["types"]],
            damageType=DamageTypeEnum[data["damageTypes"]],
            priority=PriorityEnum(int(data.get("priority", 0))),
            target=TargetEnum[data["targets"]],
            multiHitCount=HitCountEnum(int(data.get("multiHits", 1))),
            healingTypeId=None,  # Set if needed
            accuracyModifiersId=accuracy_group.id,
            damageModifiersId=damage_group.id,
            **boolean_values
        )

        database.session.add(move)
        database.session.commit()

        return jsonify({"status": "success", "move_id": move.id})
