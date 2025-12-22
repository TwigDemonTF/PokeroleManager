from .auth import MasterLogin, PlayerLogin, Register
from .player import PlayerData
from .item import ItemApi
from .battle import BattleApi, GameApi
from .pokemon import BasePokemonApi, GamePokemonApi, PullCharacterData
from .pokemon_components import NatureApi, AbilityApi, MoveApi, GarmentApi
from .pokemon_manipulation import MoveManipulation, BuyItem, RemoveResourcesApi

def registerResources(api):
    api.add_resource(Register, "/register")
    api.add_resource(MasterLogin, "/masterLogin")
    api.add_resource(PlayerLogin, "/playerLogin")
    api.add_resource(PlayerData, "/playerData/<string:gameId>/<string:playerGuid>")
    
    api.add_resource(MoveApi, "/addMove")
    api.add_resource(NatureApi, "/nature")
    api.add_resource(AbilityApi, "/ability")
    api.add_resource(GarmentApi, "/garment")

    api.add_resource(PullCharacterData, "/PullCharacterData/<string:gameId>/<string:guid>")
    api.add_resource(BasePokemonApi, "/basePokemon")
    api.add_resource(GamePokemonApi, '/gamePokemon')

    api.add_resource(GameApi, "/PullAllPokemon/<string:gameId>")
    api.add_resource(BattleApi, '/battleData')

    api.add_resource(ItemApi, "/Item")

    api.add_resource(MoveManipulation, "/moveManipulation")
    api.add_resource(RemoveResourcesApi, "/removeResources")
    api.add_resource(BuyItem, "/buyItem")