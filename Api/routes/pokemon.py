from flask import request, jsonify
from flask_restful import Resource

from Api.services.PokemonService import (
    list_base_pokemon,
    create_base_pokemon,
    create_game_pokemon,
    pull_character_data
)


class BasePokemonApi(Resource):
    def get(self):
        return jsonify(list_base_pokemon())

    def post(self):
        raw = request.get_json()
        if raw is None:
            return {"error": "No JSON received"}, 400

        base = create_base_pokemon(raw)
        return {
            "message": f"Created Pokémon '{base.name}'",
            "pokemonId": base.id
        }, 201


class GamePokemonApi(Resource):
    def post(self):
        raw = request.get_json()
        print(raw)
        if raw is None:
            return {"error": "No JSON received"}, 400

        pokemon, entity_or_error = create_game_pokemon(raw)

        if pokemon is None:
            return {"error": entity_or_error}, 400

        return {
            "message": f"Created Pokémon '{pokemon.name}'",
            "pokemonId": pokemon.id,
            "gameEntityId": entity_or_error.id
        }, 201


class PullCharacterData(Resource):
    def get(self, gameId, guid):
        data = pull_character_data(gameId, guid)
        if not data:
            return {"data": None, "message": "Character not found"}, 404

        return {"data": data}, 200
