from flask import request, jsonify
from flask_restful import Resource

from ..models.Items import Item

from ..Enums.Items.ItemCategory import ItemCategoryEnum
from ..Enums.Items.ShopTiers import ShopTierEnum

from ..utils import enum_from_string

from Api.extensions import database

class ItemApi(Resource):
    def post(self):
        data = request.get_json()

        newItem = Item(
            name=data.get("Name"),
            description=data.get("Description"),
            effect=data.get("Effect"),
            itemCategory=enum_from_string(ItemCategoryEnum, data.get("ItemCategory")),
            minShopTier=enum_from_string(ShopTierEnum, data.get("MinShopTier")),
            buyPrice=data.get("BuyPrice"),
            sellPrice=data.get("SellPrice")
        )

        database.session.add(newItem)
        database.session.commit()
    
    def get(self):
        items = Item.query.all()

        data = [{
            "id": None,
            "name": "None",
            "description": None,
            "effect": None,
            "itemCategory": None,
            "minShopTier": None,
            "buyPrice": None,
            "sellPrice": None
        }]

        data.extend(item.to_dict() for item in items)

        return jsonify(data)