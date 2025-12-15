from Api.extensions import database
from sqlalchemy.orm import relationship

class Nature(database.Model):
    __tablename__ = "Nature"

    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(50), nullable=False)
    description = database.Column(database.Text, nullable=False)

    pokemon = relationship("GamePokemon", back_populates="nature_rel")

class Ability(database.Model):
    __tablename__ = "Ability"

    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(50), nullable=False)
    flavorText = database.Column(database.Text, nullable=False)
    effect = database.Column(database.Text, nullable=False)

    pokemon = relationship("GamePokemon", back_populates="ability_rel")
