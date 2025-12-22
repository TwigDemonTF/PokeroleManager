from Api.extensions import database
from sqlalchemy import Enum
from sqlalchemy.orm import relationship
from ..Enums.Types import Types as TypeEnum

pokemon_garments = database.Table(
    "pokemon_garments",
    database.Column("pokemon_id", database.Integer, database.ForeignKey("GamePokemon.id"), primary_key=True),
    database.Column("garment_id", database.Integer, database.ForeignKey("Garment.id"), primary_key=True),
)

class BasePokemon(database.Model):
    __tablename__ = "BasePokemon"

    id = database.Column(database.Integer, primary_key=True, nullable=False)
    name = database.Column(database.String(), nullable=False, default="")

    baseHealth = database.Column(database.Integer, nullable=False, default=3)
    will = database.Column(database.Integer, nullable=False, default=3)
    logic = database.Column(database.Integer, nullable=True, default=1)
    instinct = database.Column(database.Integer, nullable=True, default=1)
    primal = database.Column(database.Integer, nullable=True, default=0)

    primaryType = database.Column(Enum(TypeEnum), nullable=False)
    secondaryType = database.Column(Enum(TypeEnum), nullable=True)

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

    def toDict(self):
        data = {}
        for column in self.__table__.columns:
            if column.name != "id":
                data[column.name] = getattr(self, column.name)
        return data

class GamePokemon(database.Model):
    __tablename__ = "GamePokemon"
    id = database.Column(database.Integer, primary_key=True, nullable=False)
    basePokemonId = database.Column(database.Integer, database.ForeignKey("BasePokemon.id"))
    basePokemon = relationship("BasePokemon")

    name = database.Column(database.String(), nullable=False, default="")
    level = database.Column(database.Integer, nullable=False, default=0)
    gender = database.Column(database.String(), nullable=True, default="None")
    age = database.Column(database.Integer, nullable=False, default=0)
    apples = database.Column(database.Integer, nullable=False, default=0)

    primaryType = database.Column(Enum(TypeEnum))
    secondaryType = database.Column(Enum(TypeEnum), nullable=True)

    natureId = database.Column(database.Integer, database.ForeignKey("Nature.id"))
    nature_rel = relationship("Nature", back_populates="pokemon")

    abilityId = database.Column(database.Integer, database.ForeignKey("Ability.id"))
    ability_rel = relationship("Ability", back_populates="pokemon")

    status = database.Column(database.String(), nullable=True, default="Healthy")

    baseHealth = database.Column(database.Integer, nullable=False, default=3)
    health = database.Column(database.Integer, nullable=False)
    lethalHealth = database.Column(database.Integer, nullable=False)
    will = database.Column(database.Integer, nullable=False, default=3)
    logic = database.Column(database.Integer, nullable=True, default=1)
    instinct = database.Column(database.Integer, nullable=True, default=1)
    primal = database.Column(database.Integer, nullable=True, default=0)

    move_connections = relationship("MoveConnection", back_populates="pokemon", cascade="all, delete-orphan")

    bag = relationship("PokemonBag", back_populates="pokemon", uselist=False)

    itemId = database.Column(database.Integer, database.ForeignKey("Item.id"), nullable=True)
    heldItem = relationship("Item")

    garments = relationship("Garment", secondary=pokemon_garments)

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
    playerColor = database.Column(database.String(20), nullable=False, default="None")
    Guid = database.Column(database.String(6), nullable=False, unique=True)

    @property
    def learned_moves(self):
        return [mc.move.name for mc in self.move_connections]

class GameEntities(database.Model):
    __tablename__ = "GameEntities"
    id = database.Column(database.Integer, primary_key=True, nullable=False)

    # Foreign keys
    gameId = database.Column(database.Integer, database.ForeignKey('Game.id'), nullable=False)
    pokemonId = database.Column(database.Integer, database.ForeignKey('GamePokemon.id'), nullable=False)

    # Relationships
    game = relationship("Game", back_populates="entities")
    pokemon = relationship("GamePokemon")

