from Api.extensions import database
from sqlalchemy import Enum
from sqlalchemy.orm import relationship
from ..Enums.Items.ShopTiers import ShopTierEnum

class User(database.Model):
    __tablename__ = "User"
    id = database.Column(database.Integer, primary_key=True, nullable=False)
    username = database.Column(database.String(100), nullable=False, unique=True)
    password = database.Column(database.String(200), nullable=False)  # hashed(salt + password)
    passwordSalt = database.Column(database.String(64), nullable=False)

    # One-to-one relationship to Game
    game = relationship("Game", back_populates="user", uselist=False)


class Game(database.Model):
    __tablename__ = "Game"
    id = database.Column(database.Integer, primary_key=True, nullable=False)
    gameId = database.Column(database.String(10), nullable=False)
    weather = database.Column(database.String(20), nullable=False, default="None")
    shopActive = database.Column(database.Boolean, nullable=False, default=False)
    activeShopTier = database.Column(database.Enum(ShopTierEnum), default=ShopTierEnum.BASIC, nullable=False)
    # One-to-one foreign key to User
    userId = database.Column(database.Integer, database.ForeignKey('User.id'), nullable=False, unique=True)
    user = relationship("User", back_populates="game")

    # Relationship: one game can have many GameEntities
    entities = relationship("GameEntities", back_populates="game")
