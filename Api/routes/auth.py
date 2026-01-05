from flask_restful import Resource
from flask import request
from werkzeug.security import generate_password_hash, check_password_hash
import secrets

from Api.extensions import database
from Api.models.User import User, Game
from Api.models.Pokemon import GamePokemon, GameEntities
from Api.Utils.utils import generate_game_id

class Register(Resource):
    def post(self):
        data = request.form if request.form else request.json

        username: str = data.get("username")
        password: str = data.get("password")

        if not username or not password:
            return {"message": "Username & password required"}, 400

        if User.query.filter_by(username=username).first():
            return {"message": "Username already exists"}, 409

        # Generate a cryptographically secure random salt
        salt: str = secrets.token_hex(32)  # 64 chars

        # Hash salt + password
        hashed: str = generate_password_hash(salt + password)

        newUser: User= User(
            username=username,
            password=hashed,
            passwordSalt=salt
        )

        database.session.add(newUser)
        database.session.commit()

        userGame = Game(
            gameId=generate_game_id(10),
            weather="None",
            userId=newUser.id
        )

        database.session.add(userGame)
        database.session.commit()

        return {
            "message": "User registered successfully",
            "gameId": userGame.gameId
        }, 201


class MasterLogin(Resource):
    def post(self):
        data = request.form if request.form else request.json

        username = data.get("username")
        password = data.get("password")

        user = User.query.filter_by(username=username).first()
        print(user)
        if not user:
            return {"status": 401, "message": "Invalid username or password"}, 401

        # Recreate salted hash input
        salted_input = user.passwordSalt + password

        if not check_password_hash(user.password, salted_input):
            return {"message": "Invalid username or password"}, 401

        game_Id = Game.query.filter_by(userId=user.id).first().gameId
        return {"status": 200, "message": f"Welcome, {username}!", "userId": user.id, "gameId": game_Id}, 200

class PlayerLogin(Resource):
    def post(self):
        data = request.form if request.form else request.json

        gameId = data.get("gameId")
        gameColor = data.get("gameColor")

        if not Game.query.filter_by(gameId=gameId):
            return {
                "status": 404,
                "message": f"Game with id {gameId} not found"
            }   

        player = (
            database.session.query(GamePokemon)
            .join(GameEntities, GameEntities.pokemonId == GamePokemon.id)
            .join(Game, Game.id == GameEntities.gameId)
            .filter(Game.gameId == gameId)
            .filter(GamePokemon.playerColor == gameColor)
            .filter(GamePokemon.isNpc == False)
            .first()
        )

        if not player:
            return {
                "status": 404,
                "message": f"Player with color {gameColor} not found within game: {gameId}"
            }   
        return {
            "gameId": gameId,
            "playerGuid": player.Guid,
            "ExperiencePoints": player.experiencePoints,
            "Apples": player.apples,
            "status": 200,
            "message": "Successfully logged in as player"
        }
