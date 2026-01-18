from flask import request
from flask_restful import Resource

from Api.services.ItemService import create_item, list_items


class ItemApi(Resource):
    def post(self):
        item = create_item(request.get_json())
        return {
            "status": 201,
            "id": item.id,
            "name": item.name
        }, 201

    def get(self):
        items = list_items()

        data = [{
            "id": None,
            "name": "None",
            "description": None,
            "effect": None,
            "effectKey": None,
            "effectData": None,
            "itemCategory": None,
            "minShopTier": None,
            "buyPrice": None,
            "sellPrice": None,
            "numUses": None,
        }]

        data.extend(item.to_dict() for item in items)

        return {
            "status": 200,
            "data": data
        }, 200
