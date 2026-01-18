from Api.extensions import database
from Api.models.User import Game


def toggle_shop(gameId):
    game = Game.query.filter_by(gameId=gameId).first()
    if not game:
        raise ValueError("Game not found")

    game.shopActive = not game.shopActive
    database.session.commit()

    return game.shopActive


def get_shop_state(gameId):
    game = Game.query.filter_by(gameId=gameId).first()
    if not game:
        raise ValueError("Game not found")

    return {
        "isOpen": game.shopActive,
        "activeShopTier": game.activeShopTier.value
    }

from Api.extensions import database
from Api.models.User import Game
from Api.models.Pokemon import GamePokemon, GameEntities
from Api.models.Items import Item, BagItem


def buy_item(gameId, pokemonGuid, itemId):
    game = Game.query.filter_by(gameId=gameId).first()
    if not game:
        return {"error": "Game not found"}, 404

    entity = (
        GameEntities.query
        .join(GamePokemon)
        .filter(
            GameEntities.gameId == game.id,
            GamePokemon.Guid == pokemonGuid
        )
        .first()
    )

    if not entity:
        return {"error": "Pokémon not found"}, 404

    pokemon = GamePokemon.query.get(entity.pokemonId)

    if not pokemon.bag:
        return {"error": "Pokémon has no bag"}, 400

    item = Item.query.get(itemId)
    if not item:
        return {"error": "Item not found"}, 404

    bag = pokemon.bag
    if len(bag.items) >= bag.bagSize.value:
        return {"error": "Bag is full"}, 400

    if pokemon.apples < item.buyPrice:
        return {"error": "Not enough apples"}, 400

    pokemon.apples -= item.buyPrice
    database.session.add(BagItem(itemId=item.id, bagId=bag.id))
    database.session.commit()

    return {
        "success": True,
        "item": item.to_dict(),
        "remainingApples": pokemon.apples
    }, 200
