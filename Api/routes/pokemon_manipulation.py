from flask import request, jsonify
from flask_restful import Resource

from ..models.Moves import Move, MoveConnection
from ..models.Pokemon import GamePokemon, GameEntities
from ..models.User import Game
from ..models.Items import Item, BagItem

from ..Utils.utils import broadcast_player_update, serialize_move, serialize_move_for_battle

from Api.extensions import database
from ..Utils.utils import broadcast_player_update, serialize_bag

class MoveManipulation(Resource):
    def get(self):
        moves = Move.query.all()
        return {
            "moves": [serialize_move_for_battle(m) for m in moves]
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

class RemoveResourcesApi(Resource):
    def post(self):
        """
        POST /api/pokemon/remove-resources
        {
          "pokemonGuid": "ABC123",
          "removeApples": 2,
          "removeXp": 5,
          "removeBagItemIds": [12, 15]
        }
        """
        data = request.get_json()

        pokemon = GamePokemon.query.filter_by(Guid=data.get("pokemonGuid")).first()
        if not pokemon:
            return {"message": "Pokemon not found"}, 404

        # --- Remove apples ---
        if "removeApples" in data:
            pokemon.apples = max(0, pokemon.apples - int(data["removeApples"]))

        # --- Remove XP ---
        if "removeXp" in data:
            pokemon.experiencePoints = max(
                0,
                pokemon.experiencePoints - int(data["removeXp"])
            )

        # --- Remove items ---
        if "removeBagItemIds" in data and pokemon.bag:
            for bag_item_id in data["removeBagItemIds"]:
                print(bag_item_id)
                print(type(bag_item_id))
                bag_item_id = int(bag_item_id)  # 🔑 THIS LINE

                bi = next(
                    (i for i in pokemon.bag.items if i.id == bag_item_id),
                    None
                )
                if bi:
                    database.session.delete(bi)

        database.session.commit()

        broadcast_player_update(
            pokemon.Guid,
            Bag=serialize_bag(pokemon)
        )
        broadcast_player_update(
            pokemon.Guid,
            Apples=pokemon.apples
        )
        broadcast_player_update(
            pokemon.Guid,
            ExperiencePoints=pokemon.experiencePoints
        )

        return {"message": "Resources removed successfully"}, 200