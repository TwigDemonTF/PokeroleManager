from flask import request, jsonify
from flask_restful import Resource

from ..models.Moves import Move, MoveConnection
from ..models.Pokemon import GamePokemon, GameEntities
from ..models.User import Game
from ..models.Items import Item, BagItem

from ..utils import broadcast_player_update, serialize_move

from Api.extensions import database

class MoveManipulation(Resource):
    def get(self):
        moves = Move.query.all()
        return {
            "moves": [
                {"id": m.id, "name": m.name, "type": m.type.name}
                for m in moves
            ]
        }, 200

    def post(self):
        data = request.get_json()

        guid = data.get("Guid")
        move_id = data.get("MoveId")
        replace_index = data.get("ReplaceIndex")  # optional

        if not guid or not move_id:
            return {"error": "Guid and MoveId required"}, 400

        pokemon = GamePokemon.query.filter_by(Guid=guid).first()
        if not pokemon:
            return {"error": "Pokémon not found"}, 404

        move = Move.query.get(move_id)
        if not move:
            return {"error": "Move not found"}, 404

        # Current moves
        current_moves = pokemon.move_connections
        move_count = len(current_moves)

        # ------------------------------------------------------------
        # REPLACE OR ADD MOVE
        # ------------------------------------------------------------
        if replace_index is not None:
            replace_index = int(replace_index)

            if replace_index < 0 or replace_index >= 4:
                return {"error": "ReplaceIndex must be 0-3"}, 400

            if any(mc.moveId == move_id for mc in current_moves):
                return {"error": "Pokémon already knows this move"}, 400

            # CASE 1: Replace existing move
            if replace_index < move_count:
                mc = current_moves[replace_index]
                mc.moveId = move_id
                database.session.commit()

                broadcast_player_update(
                    pokemon.Guid,
                    Moves=[serialize_move(mc.move) for mc in pokemon.move_connections]
                )

                return {
                    "message": "Move replaced",
                    "slot": replace_index,
                    "move": serialize_move(move)
                }, 200

            # CASE 2: Slot empty → add to next free slot
            if move_count >= 4:
                return {"error": "Already has 4 moves"}, 400

            new_mc = MoveConnection(
                pokemonId=pokemon.id,
                moveId=move_id
            )
            database.session.add(new_mc)
            database.session.commit()

            broadcast_player_update(
                pokemon.Guid,
                Moves=[serialize_move(mc.move) for mc in pokemon.move_connections]
            )

            broadcast_player_update(
                pokemon.Guid,
                Moves=[serialize_move(mc.move) for mc in pokemon.move_connections]
            )

            return {
                "message": "Move added",
                "slot": move_count,
                "move": serialize_move(move)
            }, 200

        # ------------------------------------------------------------
        # ADD MOVE
        # ------------------------------------------------------------
        if move_count >= 4:
            return {"error": "Already has 4 moves. Use ReplaceIndex."}, 400

        if any(mc.moveId == move_id for mc in current_moves):
            return {"error": "Pokémon already knows this move"}, 400

        new_mc = MoveConnection(pokemonId=pokemon.id, moveId=move_id)
        database.session.add(new_mc)
        database.session.commit()

        return {"message": "Move added", "move": move.name}, 200

class BuyItem(Resource):
    def post(self):
        raw = request.get_json()

        if raw is None:
            return {"error": "No JSON received"}, 400

        try:
            gameId = raw.get("gameId")
            pokemonGuid = raw.get("pokemonGuid")
            itemId = raw.get("itemId")
            print(gameId, pokemonGuid, itemId)
            # 1. Fetch game
            game = Game.query.filter_by(gameId=gameId).first()
            if not game:
                return {"error": "Game not found"}, 404

            # 2. Fetch Pokémon via GameEntities + Guid
            gameEntity = (
                GameEntities.query
                .join(GamePokemon)
                .filter(
                    GameEntities.gameId == game.id,
                    GamePokemon.Guid == pokemonGuid
                )
                .first()
            )

            if not gameEntity:
                return {"error": "Pokémon not found in this game"}, 404

            pokemon = GamePokemon.query.get(gameEntity.pokemonId)

            # 3. Ensure Pokémon has a bag
            if not pokemon.bag:
                return {"error": "Pokémon has no bag"}, 400

            bag = pokemon.bag

            # 4. Fetch item
            item = Item.query.get(itemId)
            if not item:
                return {"error": "Item not found"}, 404

            # 5. Check bag capacity
            current_items = len(bag.items)
            max_capacity = bag.bagSize.value

            if current_items >= max_capacity:
                return {"error": "Bag is full"}, 400

            # 6. Check apples (currency)
            if pokemon.apples < item.buyPrice:
                return {
                    "error": "Not enough apples",
                    "required": item.buyPrice,
                    "current": pokemon.apples
                }, 400

            # 7. Deduct apples
            pokemon.apples -= item.buyPrice

            # 8. Add item to bag
            bag_item = BagItem(
                itemId=item.id,
                bagId=bag.id
            )

            database.session.add(bag_item)
            database.session.commit()

            return {
                "success": True,
                "message": f"{pokemon.name} bought {item.name}",
                "item": item.to_dict(),
                "remainingApples": pokemon.apples,
                "bagUsage": f"{current_items + 1}/{max_capacity}"
            }, 200

        except Exception as e:
            database.session.rollback()
            print("BUY ITEM ERROR:", e)
            return jsonify({"error": str(e)}), 500
