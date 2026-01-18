from Api.extensions import database
from Api.models.Pokemon import GamePokemon
from Api.Utils.utils import broadcast_player_update, serialize_bag


def remove_resources(data):
    pokemon = GamePokemon.query.filter_by(Guid=data.get("pokemonGuid")).first()
    if not pokemon:
        return {"error": "Pokemon not found"}, 404

    if "removeApples" in data:
        pokemon.apples = max(0, pokemon.apples - int(data["removeApples"]))

    if "removeXp" in data:
        pokemon.experiencePoints = max(
            0, pokemon.experiencePoints - int(data["removeXp"])
        )

    if "removeBagItemIds" in data and pokemon.bag:
        for bag_item_id in data["removeBagItemIds"]:
            bi = next(
                (i for i in pokemon.bag.items if i.id == int(bag_item_id)),
                None
            )
            if bi:
                database.session.delete(bi)

    database.session.commit()

    broadcast_player_update(pokemon.Guid, Bag=serialize_bag(pokemon))
    broadcast_player_update(pokemon.Guid, Apples=pokemon.apples)
    broadcast_player_update(pokemon.Guid, ExperiencePoints=pokemon.experiencePoints)

    return {"message": "Resources removed"}, 200
