from Api.extensions import database
from Api.models.Items import Item
from Api.Enums.Items.ItemCategory import ItemCategoryEnum
from Api.Enums.Items.ShopTiers import ShopTierEnum
from Api.Utils.utils import enum_from_string


def create_item(data):
    item = Item(
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
        numUses=data.get("numUses", 0),
    )

    database.session.add(item)
    database.session.commit()
    return item


def list_items():
    return Item.query.all()
