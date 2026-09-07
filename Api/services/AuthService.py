import secrets
from werkzeug.security import generate_password_hash, check_password_hash

from Api.extensions import database
from Api.models.User import User, Game
from Api.models.Pokemon import GamePokemon, GameEntities
from Api.models.Items import GuildStorageBag
from Api.Utils.utils import generate_game_id


def register_user(username: str, password: str):
    if not username or not password:
        return {"status": 400, "message": "Username & password required"}

    if User.query.filter_by(username=username).first():
        return {"status": 409, "message": "Username already exists"}

    salt = secrets.token_hex(32)
    hashed = generate_password_hash(salt + password)

    user = User(
        username=username,
        password=hashed,
        passwordSalt=salt
    )

    database.session.add(user)
    database.session.flush()

    game = Game(
        gameId=generate_game_id(10),
        weather="None",
        userId=user.id
    )

    game.guildStorage = GuildStorageBag(items=[])

    database.session.add(game)
    database.session.commit()

    return {
        "status": 201,
        "message": "User registered successfully",
        "gameId": game.id
    }


def master_login(username: str, password: str):
    user = User.query.filter_by(username=username).first()

    if not user:
        return {"status": 401, "message": "Invalid username or password"}

    salted_input = user.passwordSalt + password

    if not check_password_hash(user.password, salted_input):
        return {"status": 401, "message": "Invalid username or password"}

    game_id = Game.query.filter_by(userId=user.id).first().gameId

    return {
        "status": 200,
        "message": f"Welcome, {username}!",
        "userId": user.id,
        "gameId": game_id
    }


def player_login(game_id: str, game_color: str):
    game = Game.query.filter_by(gameId=game_id).first()

    if not game:
        return {
            "status": 404,
            "message": f"Game with id {game_id} not found"
        }

    player = (
        database.session.query(GamePokemon)
        .join(GameEntities, GameEntities.pokemonId == GamePokemon.id)
        .filter(GameEntities.gameId == game.id)
        .filter(GamePokemon.playerColor == game_color)
        .filter(GamePokemon.isNpc == False)
        .first()
    )

    if not player:
        return {
            "status": 404,
            "message": f"Player with color {game_color} not found within game: {game_id}"
        }

    return {
        "status": 200,
        "message": "Successfully logged in as player",
        "gameId": game_id,
        "playerGuid": player.Guid,
        "ExperiencePoints": player.experiencePoints,
        "Apples": player.apples
    }
