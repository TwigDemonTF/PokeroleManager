from Api.extensions import database
from sqlalchemy import Enum
from sqlalchemy.orm import relationship


from . import Game
from ..Enums.Items.ShopTiers import ShopTierEnum
from ..Enums.Items.ItemCategory import ItemCategoryEnum
from ..Enums.BagSize import BagSizeEnum

class Item(database.Model):
    __tablename__ = "Item"

    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(50), nullable=False)
    description = database.Column(database.Text, nullable=True)

    #probably not needed
    effect = database.Column(database.Text, nullable=True)

    # example: POTION
    effectKey = database.Column(database.String(50), nullable=True)
    # example: {"maxAmount": 12}
    effectData = database.Column(database.JSON, nullable=True)
        
    minShopTier = database.Column(database.Enum(ShopTierEnum), default=ShopTierEnum.BASIC)
    itemCategory = database.Column(database.Enum(ItemCategoryEnum), default=ItemCategoryEnum.MISC)
    buyPrice = database.Column(database.Integer, nullable=True, default=0)
    sellPrice = database.Column(database.Integer, nullable=True, default=0)

    isUsable = database.Column(database.Boolean, nullable=False, default=False)
    isEquipable = database.Column(database.Boolean, nullable=False, default=False)

    numUses = database.Column(database.Integer, nullable=True, default=None)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "effect": self.effect,
            "effectKey": self.effectKey,
            "effectData": self.effectData,
            "minShopTier": self.minShopTier.value,
            "itemCategory": self.itemCategory.value,
            "buyPrice": self.buyPrice,
            "sellPrice": self.sellPrice,
            "numUses": self.numUses
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

    #example = {"remainingAmount": 12}
    state = database.Column(database.JSON, nullable=True)

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

class PersonalStorageBag(database.Model):
    __tablename__ = "PersonalStorageBag"

    id = database.Column(database.Integer, primary_key=True)

    pokemonId = database.Column(
        database.Integer,
        database.ForeignKey("GamePokemon.id"),
        nullable=False,
        unique=True
    )

    pokemon = database.relationship(
        "GamePokemon",
        back_populates="personalStorage",
        overlaps="personalStorage"
    )

    items = relationship(
        "PersonalStorageItem",
        back_populates="bag",
        cascade="all, delete-orphan"
    )

class PersonalStorageItem(database.Model):
    __tablename__ = "PersonalStorageItem"

    id = database.Column(database.Integer, primary_key=True)
    itemId = database.Column(database.Integer, database.ForeignKey("Item.id"), nullable=False)
    bagId = database.Column(
        database.Integer,
        database.ForeignKey("PersonalStorageBag.id"),
        nullable=False
    )

    item = relationship("Item")
    bag = relationship("PersonalStorageBag", back_populates="items")

class GuildStorageBag(database.Model):
    __tablename__ = "GuildStorageBag"

    id = database.Column(database.Integer, primary_key=True)

    gameId = database.Column(
        database.Integer,
        database.ForeignKey("Game.id"),
        nullable=False,
        unique=True
    )

    game = database.relationship(
        "Game",
        back_populates="guildStorage",
        overlaps="guildStorage"
    )

    items = relationship(
        "GuildStorageItem",
        back_populates="bag",
        cascade="all, delete-orphan"
    )

class GuildStorageItem(database.Model):
    __tablename__ = "GuildStorageItem"

    id = database.Column(database.Integer, primary_key=True)
    itemId = database.Column(database.Integer, database.ForeignKey("Item.id"), nullable=False)
    bagId = database.Column(
        database.Integer,
        database.ForeignKey("GuildStorageBag.id"),
        nullable=False
    )

    item = relationship("Item")
    bag = relationship("GuildStorageBag", back_populates="items")