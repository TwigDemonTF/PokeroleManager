from sqlalchemy.orm import relationship, backref

from extensions import database
from enums.WeatherTypes import WeatherTypes
from enums.GuildRanks import GuildRanks
from enums.StatusTypes import StatusTypes
from enums.Types import Types


class User(database.Model):
    __tablename__ = "user"

    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(100), nullable=False)
    email = database.Column(database.String(200), nullable=False)
    password = database.Column(database.String(50), nullable=False)
    gameUuid = database.Column(database.String(10), database.ForeignKey('game.uuid'))
    game = database.relationship("Game", backref=backref("game", uselist=False))

    def to_dict(self):
        return {"id": self.id, "name": self.name}

class Game(database.Model):
    __tablename__ = "game"

    id = database.Column(database.Integer, primary_key=True)
    uuid = database.Column(database.String(10), nullable=False)
    activeWeather = database.Column(database.Enum(WeatherTypes), nullable=True)

class Guild(database.Model):
    __tablename__ = "guild"

    id = database.Column(database.Integer, primary_key=True) 
    name = database.Column(database.Integer, nullable=False)
    rank = database.Column(database.Enum(GuildRanks), nullable=False)
    guildPoints = database.Column(database.Integer, nullable=False)
class GameEntities(database.Model):
    __tablename__ = "game_entities"

    id = database.Column(database.Integer, primary_key=True) 
    gameId = database.Column(database.Integer, database.ForeignKey("game.uuid"))
    game = database.relationship("Game", backref=backref("game", uselist=False))
    entityId = database.Column(database.Integer, database.ForeignKey('pokemon.id'))
    entity = database.relationship("Pokemon", backref=backref("pokemon", uselist=False))

class Pokemon(database.Model):
    __tablename__ = "pokemon"

    id = database.Column(database.Integer, primary_key=True) 
    name = database.Column(database.String(100), nullable=False)
    age = database.Column(database.Integer, nullable=True)
    level = database.Column(database.Integer, nullable=False)
    statusId = database.Column(database.Integer, database.ForeignKey("status.id"))
    status = database.relationship("Status", backref=backref("status", uselist=False))
    primaryType = database.Column(database.Enum(Types), nullable=False)
    secondaryType = database.Column(database.Enum(Types), nullable=False)
    natureId = database.Column(database.Integer, database.ForeignKey("nature.id"), nullable=True)
    nature = database.relationship("Nature", backref=backref("nature", uselist=False))
    abilityId = database.Column(database.Integer, database.ForeignKey("ability.id"), nullable=False)
    ability = database.relationship("Ability", backref=backref("ability", uselist=False))
    will = database.Column(database.Integer, nullable=False, default=0)
    willPotential = database.Column(database.Integer, nullable=False, default=0)
    logic = database.Column(database.Integer, nullable=False, default=0)
    logicPotential = database.Column(database.Integer, nullable=False, default=0)
    instinct = database.Column(database.Integer, nullable=False, default=0)
    instinctPotential = database.Column(database.Integer, nullable=False, default=0)
    experiencePoints = database.Column(database.Integer, nullable=False, default=0)
    strength = database.Column(database.Integer, nullable=False, default=0)
    stenghthPotential = database.Column(database.Integer, nullable=False, default=0)
    dexterity = database.Column(database.Integer, nullable=False, default=0)
    dexterityPotential = database.Column(database.Integer, nullable=False, default=0)
    insight = database.Column(database.Integer, nullable=False, default=0)
    insightPotential = database.Column(database.Integer, nullable=False, default=0)
    vitality = database.Column(database.Integer, nullable=False, default=0)
    vitalityPotential = database.Column(database.Integer, nullable=False, default=0)
    special = database.Column(database.Integer, nullable=False, default=0)
    specialPotential = database.Column(database.Integer, nullable=False, default=0)
    defense = database.Column(database.Integer, nullable=False, default=0)
    specialDefense = database.Column(database.Integer, nullable=False, default=0)
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
    isPlayerControlled = database.Column(database.Boolean, default=False, nullable=False)

class Status(database.Model):
    __tablename__ = "status"

    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(100), nullable=False)
    description = database.Column(database.Text, nullable=False)

class Nature(database.Model):
    __tablename__ = "nature"

    id = database.Column(database.Integer, primary_key=True) 
    name = database.Column(database.String(100), nullable=False)
    description = database.Column(database.Text, nullable=False)

class Ability(database.Model):
    __tablename__ = "ability"

    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(100), nullable=False)
    description = database.Column(database.Text, nullable=False)