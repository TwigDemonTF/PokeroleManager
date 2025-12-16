from flask import request, jsonify
from flask_restful import Resource

from ..models.Items import Item

from ..Enums.Items.ItemCategory import ItemCategoryEnum
from ..Enums.Items.ShopTiers import ShopTierEnum

from ..Utils.utils import enum_from_string

from Api.extensions import database

class ItemApi(Resource):
    def post(self):
        data = request.get_json()

        new_item = Item(
            name=data.get("name"),
            description=data.get("description"),

            effectKey=data.get("effectKey"),
            effectData=data.get("effectData"),

            itemCategory=enum_from_string(ItemCategoryEnum, data.get("itemCategory")),
            minShopTier=enum_from_string(ShopTierEnum, data.get("minShopTier")),

            isUsable=bool(data.get("isUsable", False)),
            isEquipable=bool(data.get("isEquipable", False)),

            buyPrice=data.get("buyPrice", 0),
            sellPrice=data.get("sellPrice", 0),
            numUses=data.get("numUses", 0)
        )

        database.session.add(new_item)
        database.session.commit()

        return {
            "id": new_item.id,
            "name": new_item.name
        }, 201
    
    def get(self):
        items = Item.query.all()

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

        return jsonify(data)