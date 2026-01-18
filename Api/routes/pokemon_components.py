from flask import request, jsonify
from flask_restful import Resource
from Api.services.PokemonComponentService import (
    create_nature, create_ability, create_move
)
from Api.models.Misc import Nature, Ability
from Api.models.Items import Garment
from Api.Utils.utils import enum_to_dict_list
from Api.Enums import *


class NatureApi(Resource):
    def post(self):
        create_nature(request.get_json())
        return {"status": "ok"}, 201

    def get(self):
        return jsonify(
            [{"id": None, "name": "None"}] +
            [{"id": n.id, "name": n.name} for n in Nature.query.all()]
        )


class AbilityApi(Resource):
    def post(self):
        create_ability(request.get_json())
        return {"status": "ok"}, 201

    def get(self):
        return jsonify(
            [{"id": None, "name": "None"}] +
            [{"id": a.id, "name": a.name} for a in Ability.query.all()]
        )


class GarmentApi(Resource):
    def get(self):
        return jsonify(
            [{"id": None, "name": "None"}] +
            [{"id": g.id, "name": g.name} for g in Garment.query.all()]
        )


class MoveApi(Resource):
    def post(self):
        move_id = create_move(request.get_json())
        return {"status": "success", "move_id": move_id}, 201
