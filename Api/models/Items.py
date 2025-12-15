from Api.extensions import database
from sqlalchemy import Enum
from sqlalchemy.orm import relationship

from ..Enums.Items.ShopTiers import ShopTierEnum
from ..Enums.Items.ItemCategory import ItemCategoryEnum
from ..Enums.BagSize import BagSizeEnum

class Item(database.Model):
    __tablename__ = "Item"

    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(50), nullable=False)
    description = database.Column(database.Text, nullable=True)
    effect = database.Column(database.Text, nullable=True)
    minShopTier = database.Column(database.Enum(ShopTierEnum), default=ShopTierEnum.BASIC)
    itemCategory = database.Column(database.Enum(ItemCategoryEnum), default=ItemCategoryEnum.MISC)
    buyPrice = database.Column(database.Integer, nullable=True, default=0)
    sellPrice = database.Column(database.Integer, nullable=True, default=0)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "effect": self.effect,
            "minShopTier": self.minShopTier.value,
            "itemCategory": self.itemCategory.value,
            "buyPrice": self.buyPrice,
            "sellPrice": self.sellPrice
        }

class Garment(database.Model):
    __tablename__ = "Garment"

    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(50), nullable=False)
    description = database.Column(database.Text, nullable=True)
    effect = database.Column(database.Text, nullable=True)

class BagItem(database.Model):
    __tablename__ = "BagItem"

    id = database.Column(database.Integer, primary_key=True)
    itemId = database.Column(database.Integer, database.ForeignKey("Item.id"), nullable=False)
    bagId = database.Column(database.Integer, database.ForeignKey("PokemonBag.id"), nullable=False)

    # relationships
    item = relationship("Item")
    bag = relationship("PokemonBag", back_populates="items")

class PokemonBag(database.Model):
    __tablename__ = "PokemonBag"

    id = database.Column(database.Integer, primary_key=True)
    bagSize = database.Column(Enum(BagSizeEnum), nullable=False, default=BagSizeEnum.size5)

    pokemonId = database.Column(database.Integer, database.ForeignKey("GamePokemon.id"))
    pokemon = relationship("GamePokemon", back_populates="bag")

    items = relationship("BagItem", back_populates="bag", cascade="all, delete-orphan")
