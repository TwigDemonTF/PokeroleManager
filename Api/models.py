from sqlalchemy.orm import relationship, backref

from .database import database
# from Enums.WeatherTypes import WeatherTypes
# from Enums.GuildRanks import GuildRanks
# from Enums.StatusTypes import StatusTypes
# from Enums.Types import Types


class Pokemon(database.Model):
    __tablename__ = "Pokemon"

    id = database.Column(database.Integer, primary_key=True, nullable=False)
    name = database.Column(database.String(), nullable=False, default="")
    level = database.Column(database.Integer, nullable=False, default=0)
    gender = database.Column(database.String(), nullable=True, default="None")
    age = database.Column(database.Integer, nullable=False, default=0)
    nature = database.Column(database.String(), nullable=True, default="None")
    ability = database.Column(database.String(), nullable=False, default="None")
    status = database.Column(database.String(), nullable=True, default="Healthy")

    baseHealth = database.Column(database.Integer, nullable=False, default=3)
    will = database.Column(database.Integer, nullable=False, default=3)
    logic = database.Column(database.Integer, nullable=True, default=1)
    instinct = database.Column(database.Integer, nullable=True, default=1)
    primal = database.Column(database.Integer, nullable=True, default=0)

    heldItem = database.Column(database.String(), nullable=True, default="")
    garment1 = database.Column(database.String(), nullable=True, default="")
    garment2 = database.Column(database.String(), nullable=True, default="")
    garment3 = database.Column(database.String(), nullable=True, default="")

    primaryType = database.Column(database.String(), nullable=False, default="Normal")
    secondaryType = database.Column(database.String(), nullable=True, default="None")

    strength = database.Column(database.Integer, nullable=False, default=0)
    strengthPotential = database.Column(database.Integer, nullable=False, default=0)

    dexterity = database.Column(database.Integer, nullable=False, default=0)
    dexterityPotential = database.Column(database.Integer, nullable=False, default=0)

    vitality = database.Column(database.Integer, nullable=False, default=0)
    vitalityPotential = database.Column(database.Integer, nullable=False, default=0)

    special = database.Column(database.Integer, nullable=False, default=0)
    specialPotential = database.Column(database.Integer, nullable=False, default=0)

    insight = database.Column(database.Integer, nullable=False, default=0)
    insightPotential = database.Column(database.Integer, nullable=False, default=0)

    fight = database.Column(database.Integer, nullable=False, default=0)
    survival = database.Column(database.Integer, nullable=False, default=0)
    contest = database.Column(database.Integer, nullable=False, default=0)
    brawl = database.Column(database.Integer, nullable=False, default=0)
    channel = database.Column(database.Integer, nullable=False, default=0)
    clash = database.Column(database.Integer, nullable=False, default=0)
    evasion = database.Column(database.Integer, nullable=False, default=0)
    alert = database.Column(database.Integer, nullable=False, default=0)
    athletic = database.Column(database.Integer, nullable=False, default=0)
    natureStat = database.Column(database.Integer, nullable=False, default=0)
    stealth = database.Column(database.Integer, nullable=False, default=0)
    allure = database.Column(database.Integer, nullable=False, default=0)
    etiquette = database.Column(database.Integer, nullable=False, default=0)
    intimidate = database.Column(database.Integer, nullable=False, default=0)
    perform = database.Column(database.Integer, nullable=False, default=0) 
    experiencePoints = database.Column(database.Integer, nullable=False, default=0)
    isNpc = database.Column(database.Boolean, nullable=False)
    Guid = database.Column(database.String(6), nullable=False, unique=True)

    def toDict(self):
        data = {}
        for column in self.__table__.columns:
            if column.name != "id":
                data[column.name] = getattr(self, column.name)
        return data

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

    # One-to-one foreign key to User
    userId = database.Column(database.Integer, database.ForeignKey('User.id'), nullable=False, unique=True)
    user = relationship("User", back_populates="game")

    # Relationship: one game can have many GameEntities
    entities = relationship("GameEntities", back_populates="game")


class GameEntities(database.Model):
    __tablename__ = "GameEntities"
    id = database.Column(database.Integer, primary_key=True, nullable=False)

    # Foreign keys
    gameId = database.Column(database.Integer, database.ForeignKey('Game.id'), nullable=False)
    pokemonId = database.Column(database.Integer, database.ForeignKey('Pokemon.id'), nullable=False)

    # Relationships
    game = relationship("Game", back_populates="entities")
    pokemon = relationship("Pokemon")
