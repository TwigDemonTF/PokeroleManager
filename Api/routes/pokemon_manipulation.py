from flask import request
from flask_restful import Resource
from Api.services.MoveService import list_moves_for_battle, add_or_replace_move
from Api.services.ShopService import buy_item
from Api.services.ResourceService import remove_resources


class MoveManipulation(Resource):
    def get(self):
        return {"moves": list_moves_for_battle()}, 200

    def post(self):
        data = request.get_json()
        return add_or_replace_move(
            data.get("Guid"),
            data.get("MoveId"),
            data.get("ReplaceIndex")
        )


class BuyItem(Resource):
    def post(self):
        data = request.get_json()
        return buy_item(
            data.get("gameId"),
            data.get("pokemonGuid"),
            data.get("itemId")
        )


class RemoveResourcesApi(Resource):
    def post(self):
        return remove_resources(request.get_json())
