from flask_restful import Resource

from Api.extensions import database
from ..models.Pokemon import GameEntities, GamePokemon
from ..models.User import Game
from ..models.Misc import Nature
from ..models.Misc import Ability
from ..models.Items import Item

from ..Utils.utils import extract_modifiers_from_group

from ..services.PlayerService import get_player_data

class PlayerData(Resource):
    def get(self, gameId, playerGuid):
        pokemon_data = get_player_data(gameId, playerGuid)
        return {"status": 200, "data": pokemon_data}, 200
