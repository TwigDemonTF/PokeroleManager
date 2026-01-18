from Api.extensions import database
from Api.models.Moves import Move, MoveConnection
from Api.models.Pokemon import GamePokemon
from Api.Utils.utils import serialize_move, serialize_move_for_battle, broadcast_player_update


def list_moves_for_battle():
    return [serialize_move_for_battle(m) for m in Move.query.all()]


def add_or_replace_move(guid, move_id, replace_index=None):
    pokemon = GamePokemon.query.filter_by(Guid=guid).first()
    if not pokemon:
        return {"error": "Pokémon not found"}, 404

    move = Move.query.get(move_id)
    if not move:
        return {"error": "Move not found"}, 404

    current_moves = pokemon.move_connections

    if any(mc.moveId == move_id for mc in current_moves):
        return {"error": "Pokémon already knows this move"}, 400

    # ---- REPLACE ----
    if replace_index is not None:
        replace_index = int(replace_index)

        if replace_index < 0 or replace_index >= 4:
            return {"error": "ReplaceIndex must be 0-3"}, 400

        if replace_index < len(current_moves):
            current_moves[replace_index].moveId = move_id
        else:
            if len(current_moves) >= 4:
                return {"error": "Already has 4 moves"}, 400

            database.session.add(
                MoveConnection(pokemonId=pokemon.id, moveId=move_id)
            )

    # ---- ADD ----
    else:
        if len(current_moves) >= 4:
            return {"error": "Already has 4 moves"}, 400

        database.session.add(
            MoveConnection(pokemonId=pokemon.id, moveId=move_id)
        )

    database.session.commit()

    broadcast_player_update(
        pokemon.Guid,
        Moves=[serialize_move(mc.move) for mc in pokemon.move_connections]
    )

    return {
        "message": "Move updated",
        "move": serialize_move(move)
    }, 200
