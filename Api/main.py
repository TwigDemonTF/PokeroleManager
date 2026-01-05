from flask import jsonify, request, Response, stream_with_context

from .models.Pokemon import GamePokemon, GameEntities
from .models.User import Game
from .models.Items import Item, BagItem, PokemonBag

from .Enums.StatusTypes import StatusTypes
from .Enums.BagSize import BagSizeEnum
from .Enums.Items.ItemCategory import ItemCategoryEnum
from .Enums.Items.ShopTiers import ShopTierEnum

from .Utils.utils import broadcast_player_update, clients, STAT_COST_RULES, STAT_TYPE,STATIC_STAT_CAPS , serialize_bag

from Api import create_app
from Api.extensions import database

import queue
import json

app = create_app()

@app.route('/updateHealth', methods=['POST'])
def UpdateHealth():
    data = request.get_json()
    game_id = data.get('gameId')
    guid = data.get('guid')
    new_health = data.get('health')

    if not game_id or not guid or new_health is None:
        return jsonify({"error": "Missing required fields"}), 400

    # Find the game (optional, ensures game exists)
    game = Game.query.filter_by(gameId=game_id).first()
    if not game:
        return jsonify({"error": "Game not found"}), 404

    # Find the Pokémon by GUID
    pokemon = GamePokemon.query.filter_by(Guid=guid).first()
    if not pokemon:
        return jsonify({"error": "Pokemon not found"}), 404

    # Update health
    pokemon.health = new_health

    # Set status to FAINTED if health is zero
    if pokemon.health <= 0:
        pokemon.status = StatusTypes.FAINTED.value
    elif pokemon.status == StatusTypes.FAINTED.value and pokemon.health > 0:
        # Optional: revive if health goes above 0
        pokemon.status = StatusTypes.HEALTHY.value

    database.session.commit()

    subscribers = clients.get(guid, set())

    broadcast_player_update(
        pokemon.Guid,
        Health=pokemon.health,
        Status=pokemon.status
    )

    return jsonify({
        "success": True,
        "pokemon": {
            "name": pokemon.name,
            "guid": pokemon.Guid,
            "health": pokemon.health,
            "status": pokemon.status
        }
    }), 200

@app.route('/updateLethalHealth', methods=['POST'])
def UpdateLethalHealth():
    data = request.get_json()
    game_id = data.get('gameId')
    guid = data.get('guid')
    new_lethal_health = data.get('lethalHealth')

    if not game_id or not guid or new_lethal_health is None:
        return jsonify({"error": "Missing required fields"}), 400

    # Find the game (optional, ensures game exists)
    game = Game.query.filter_by(gameId=game_id).first()
    if not game:
        return jsonify({"error": "Game not found"}), 404

    # Find the Pokémon by GUID
    pokemon = GamePokemon.query.filter_by(Guid=guid).first()
    if not pokemon:
        return jsonify({"error": "Pokemon not found"}), 404

    # Update health
    pokemon.lethalHealth = new_lethal_health

    database.session.commit()

    subscribers = clients.get(guid, set())

    broadcast_player_update(
        pokemon.Guid,
        LethalHealth=pokemon.lethalHealth,
    )

    return jsonify({
        "success": True,
        "pokemon": {
            "name": pokemon.name,
            "guid": pokemon.Guid,
            "health": pokemon.health,
            "status": pokemon.status
        }
    }), 200

@app.route("/buyStat/<string:gameId>/<string:pokemonGuid>", methods=["POST"])
def BuyStat(gameId, pokemonGuid):
    raw = request.get_json()
    if not raw:
        return {"error": "No JSON received"}, 400

    stat_name = raw.get("stat")
    if not stat_name:
        return {"error": "Stat name is required"}, 400

    # 1. Fetch Pokémon (same pattern you already use)
    pokemon = (
        GamePokemon.query
        .join(GameEntities, GamePokemon.id == GameEntities.pokemonId)
        .join(Game, GameEntities.gameId == Game.id)
        .filter(
            Game.gameId == gameId,
            GamePokemon.Guid == pokemonGuid
        )
        .first()
    )

    if not pokemon:
        return {"error": "Pokémon not found"}, 404

    # 2. Validate stat
    stat_type = STAT_TYPE.get(stat_name)
    if stat_type is None:
        return {"error": f"{stat_name} cannot be purchased"}, 400

    cost_fn = STAT_COST_RULES.get(stat_type)
    if not cost_fn:
        return {"error": "Invalid stat configuration"}, 500

    # 3. Get current stat value dynamically
    if not hasattr(pokemon, stat_name.lower()):
        return {"error": f"Unknown stat: {stat_name}"}, 400

    current_value = getattr(pokemon, stat_name.lower())

    # 3.5 Check stat potential cap
    potential_attr = f"{stat_name.lower()}Potential"

    if hasattr(pokemon, potential_attr):
        max_value = getattr(pokemon, potential_attr)
    else:
        # fallback for static stats
        max_value = STATIC_STAT_CAPS.get(stat_name.lower())
        if max_value is None:
            return {
                "error": f"{stat_name} cannot be purchased"
            }, 400

    if current_value >= max_value:
        return {
            "error": f"{stat_name} is already at maximum potential",
            "current": current_value,
            "maximum": max_value
        }, 400

    # 4. Compute cost
    cost = cost_fn(current_value)

    if pokemon.experiencePoints < cost:
        return {
            "error": "Not enough XP",
            "required": cost,
            "current": pokemon.experiencePoints
        }, 400

    # 5. Apply stat + XP deduction
    setattr(pokemon, stat_name.lower(), current_value + 1)
    pokemon.experiencePoints -= cost

    # 6. Add level based on new stat level
    pokemon.level += current_value + 1

    database.session.commit()

    return {
        "success": True,
        "stat": stat_name,
        "newValue": current_value + 1,
        "xpSpent": cost,
        "remainingXP": pokemon.experiencePoints
    }, 200

@app.route("/itemEnums", methods=["GET"])
def GetItemEnums():
    # Return enums as lists of tuples [(name, value), ...] to preserve order
    item_categories = [(e.name, e.value) for e in ItemCategoryEnum]
    shop_tiers = [(e.name, e.value) for e in ShopTierEnum]
    
    return {
        "ItemCategoryEnum": item_categories,
        "ShopTierEnum": shop_tiers
    }

@app.route("/addItemToBag/<string:gameId>/<string:pokemonGuid>/<string:itemId>", methods=["POST"])
def AddItemToBag(gameId, pokemonGuid, itemId):
    print(gameId, pokemonGuid, itemId)
    try:
        # 1. Find the game
        game = Game.query.filter_by(gameId=gameId).first()
        if not game:
            return jsonify({"success": False, "message": "Game not found"}), 404

        # 2. Find the Pokémon in that game
        game_entity = GameEntities.query.join(GamePokemon).filter(
            GameEntities.gameId == game.id,
            GamePokemon.Guid == pokemonGuid
        ).first()

        if not game_entity:
            return jsonify({"success": False, "message": "Pokémon not found in this game"}), 404

        pokemon = game_entity.pokemon

        # 3. Find the item
        item = Item.query.filter_by(id=int(itemId)).first()
        if not item:
            return jsonify({"success": False, "message": "Item not found"}), 404

        # 4. Ensure the Pokémon has a bag
        if not pokemon.bag:
            new_bag = PokemonBag(bagSize=BagSizeEnum.size5, pokemon=pokemon)
            database.session.add(new_bag)
            database.session.commit()

        # 5. Check bag capacity
        current_items_count = len(pokemon.bag.items)
        try:
            max_items = int(pokemon.bag.bagSize.value.replace('size', ''))
        except Exception:
            max_items = 5  # default fallback

        if current_items_count >= max_items:
            return jsonify({"success": False, "message": "Bag is full"}), 400

        # 6. Add the item to the bag
        bag_item = BagItem(itemId=item.id, bagId=pokemon.bag.id)
        database.session.add(bag_item)
        database.session.commit()

        broadcast_player_update(
            pokemon.Guid,
            Bag=serialize_bag(pokemon)
        )

        return jsonify({
            "success": True,
            "message": f"{item.name} added to {pokemon.name}'s bag",
            "item": item.to_dict()
        })

    except Exception as e:
        database.session.rollback()
        return jsonify({"success": False, "message": str(e)}), 500

@app.route("/equipItem/<string:gameId>/<string:pokemonGuid>/<int:itemId>", methods=["POST"])
def EquipItem(gameId, pokemonGuid, itemId):
    try:
        # ---- Find Pokémon ----
        pokemon = (
            database.session.query(GamePokemon)
            .join(GameEntities, GamePokemon.id == GameEntities.pokemonId)
            .join(Game, GameEntities.gameId == Game.id)
            .filter(Game.gameId == gameId)
            .filter(GamePokemon.Guid == pokemonGuid)
            .first()
        )

        if not pokemon:
            return {"error": "Pokémon not found"}, 404

        if not pokemon.bag:
            return {"error": "Pokémon has no bag"}, 400

        # ---- Find BagItem ----
        bag_item = BagItem.query.filter_by(
            id=itemId,
            bagId=pokemon.bag.id
        ).first()

        if not bag_item:
            return {"error": "Item not found in Pokémon bag"}, 404

        item = bag_item.item

        # ---- Validate Held Item ----
        if not item.isEquipable:
            return {"error": "Only Equipable Items can be equipped"}, 400

        bag = pokemon.bag
        bag_limit = int(bag.bagSize.name.replace("size", ""))  # size5 → 5

        # ---- Transaction starts ----
        # If Pokémon already has an item equipped, we will swap
        currently_equipped_item = pokemon.heldItem

        # If swapping, bag must have space AFTER removal
        if currently_equipped_item:
            # removing one, adding one → net 0
            pass
        else:
            # removing one → always safe
            pass

        # ---- Remove new item from bag ----
        database.session.delete(bag_item)

        # ---- If Pokémon had an item, put it back in the bag ----
        if currently_equipped_item:
            # Check capacity (safety check)
            if len(bag.items) >= bag_limit:
                database.session.rollback()
                return {"error": "Bag is full"}, 400

            returned_item = BagItem(
                itemId=currently_equipped_item.id,
                bagId=bag.id
            )
            database.session.add(returned_item)

        # ---- Equip new item ----
        pokemon.itemId = item.id

        database.session.commit()

        broadcast_player_update(
            pokemon.Guid,
            Bag=serialize_bag(pokemon),
            HeldItem=item.to_dict()
        )

        return {
            "success": True,
            "equippedItem": item.to_dict()
        }, 200

    except Exception as e:
        database.session.rollback()
        return {"error": str(e)}, 500

@app.route("/unequipItem/<string:gameId>/<string:pokemonGuid>", methods=["GET", "POST"])
def UnequipItem(gameId, pokemonGuid):
    try:
        # ---- Find Pokémon ----
        pokemon = (
            database.session.query(GamePokemon)
            .join(GameEntities, GamePokemon.id == GameEntities.pokemonId)
            .join(Game, GameEntities.gameId == Game.id)
            .filter(Game.gameId == gameId)
            .filter(GamePokemon.Guid == pokemonGuid)
            .first()
        )

        if not pokemon:
            return {"error": "Pokémon not found"}, 404

        if not pokemon.heldItem:
            return {"error": "No item equipped"}, 400

        if not pokemon.bag:
            return {"error": "Pokémon has no bag"}, 400

        bag = pokemon.bag
        bag_limit = int(bag.bagSize.name.replace("size", ""))  # size5 → 5

        # ---- Check bag space ----
        if len(bag.items) >= bag_limit:
            return {"error": "Bag is full, cannot unequip"}, 400

        # ---- Move held item to bag ----
        returned_item = BagItem(
            itemId=pokemon.heldItem.id,
            bagId=bag.id
        )
        database.session.add(returned_item)

        # ---- Unequip item ----
        pokemon.itemId = None

        database.session.commit()

        broadcast_player_update(
            pokemon.Guid,
            Bag=serialize_bag(pokemon),
            HeldItem=None
        )

        return {
            "success": True,
            "bag": serialize_bag(pokemon),
            "message": f"Unequipped {returned_item.item.name}",
            "bagUsage": f"{len(bag.items) + 1}/{bag_limit}"
        }, 200

    except Exception as e:
        database.session.rollback()
        return {"error": str(e)}, 500

@app.route("/sellItem/<string:gameId>/<string:pokemonGuid>/<int:bagItemId>", methods=["POST"])
def SellItem(gameId, pokemonGuid, bagItemId):
    try:
        pokemon = GamePokemon.query.filter_by(Guid=pokemonGuid).first()
        if not pokemon or not pokemon.bag:
            return jsonify(error="Pokémon or bag not found"), 404

        bag_item = BagItem.query.filter_by(
            id=bagItemId,
            bagId=pokemon.bag.id
        ).first()

        if not bag_item:
            return jsonify(error="Item not found in bag"), 404

        item = bag_item.item
        sell_price = item.sellPrice or 0

        if sell_price <= 0:
            return jsonify(error="Item cannot be sold"), 400

        pokemon.apples += sell_price
        database.session.delete(bag_item)
        database.session.commit()

        broadcast_player_update(
            pokemon.Guid,
            Bag=serialize_bag(pokemon),
            Apples=pokemon.apples
        )

        return jsonify({
            "success": True,
            "applesGained": sell_price,
            "totalApples": pokemon.apples
        })

    except Exception as e:
        database.session.rollback()
        return jsonify(error=str(e)), 500

@app.route("/getApples/<string:gameId>/<string:playerGuid>", methods=["POST"])
def GetApples(gameId, playerGuid):
    game = Game.query.filter_by(gameId=gameId).first()
    if not game:
        return jsonify({"success": False, "error": "Game not found"}), 404

    entity = GameEntities.query.filter_by(gameId=game.id).join(GamePokemon).filter(GamePokemon.Guid == playerGuid).first()
    if not entity:
        return jsonify({"success": False, "error": "Player not found in this game"}), 404

    player = entity.pokemon

    return jsonify({"success": True, "apples": player.apples})

@app.route("/addXp/<game_id>/<pokemon_guid>", methods=["POST"])
def AddXp(game_id, pokemon_guid):
    data = request.get_json()
    xp = data.get("xp", 0)

    if xp < 0:
        return jsonify({"error": "XP cannot be negative"}), 400

    pokemon = GamePokemon.query.filter_by(Guid=pokemon_guid).first()
    if not pokemon:
        return jsonify({"error": "Pokémon not found"}), 404

    pokemon.experiencePoints = (pokemon.experiencePoints or 0) + xp
    database.session.commit()

    broadcast_player_update(
        pokemon.Guid,
        ExperiencePoints=pokemon.experiencePoints
    )

    return jsonify({
        "guid": pokemon.Guid,
        "new_xp": pokemon.experiencePoints
    })

@app.route("/addMoney/<game_id>/<pokemon_guid>", methods=["POST"])
def AddMoney(game_id, pokemon_guid):
    data = request.get_json()
    money = data.get("money", 0)

    if money < 0:
        return jsonify({"error": "Money cannot be negative"}), 400

    pokemon = GamePokemon.query.filter_by(Guid=pokemon_guid).first()
    if not pokemon:
        return jsonify({"error": "Pokémon not found"}), 404

    pokemon.apples = (pokemon.apples or 0) + money
    database.session.commit()

    broadcast_player_update(
        pokemon.Guid,
        Apples=pokemon.apples
    )

    return jsonify({
        "guid": pokemon.Guid,
        "new_money": pokemon.apples
    })

@app.route("/addXpBatch/<game_id>", methods=["POST"])
def AddXpBatch(game_id):
    data = request.get_json()
    guids = data.get("guids", [])
    xp = data.get("xp", 0)

    if xp < 0:
        return jsonify({"error": "XP cannot be negative"}), 400

    pokes = GamePokemon.query.filter(GamePokemon.Guid.in_(guids)).all()
    for p in pokes:
        p.experiencePoints = (p.experiencePoints or 0) + xp
    database.session.commit()

    return jsonify({"updated": [p.Guid for p in pokes]})

@app.route("/addMoneyBatch/<game_id>", methods=["POST"])
def AddMoneyBatch(game_id):
    data = request.get_json()
    guids = data.get("guids", [])
    money = data.get("money", 0)

    if money < 0:
        return jsonify({"error": "Money cannot be negative"}), 400

    pokes = GamePokemon.query.filter(GamePokemon.Guid.in_(guids)).all()
    for p in pokes:
        p.apples = (p.apples or 0) + money
    database.session.commit()

    return jsonify({"updated": [p.Guid for p in pokes]})

@app.route("/pokemonStatus/<string:gameId>/<string:pokemonGuid>")
def PokemonmStatus(gameId, pokemonGuid):
    game = Game.query.filter_by(gameId=gameId).first()
    if not game:
        return jsonify({"success": False, "message": "Game not found"}), 404

    # 2. Find the Pokémon in that game
    game_entity = GameEntities.query.join(GamePokemon).filter(
        GameEntities.gameId == game.id,
        GamePokemon.Guid == pokemonGuid
    ).first()

    if not game_entity:
        return jsonify({"success": False, "message": "Pokémon not found in this game"}), 404

    pokemon = game_entity.pokemon

    return {
        "Status": pokemon.status,
        "Health": pokemon.health
    }, 200 

@app.route("/pokemonStatusStream/<string:gameId>/<string:pokemonGuid>")
def pokemonStatusStream(gameId, pokemonGuid):
    q = queue.Queue()

    subscribers = clients.setdefault(pokemonGuid, set())
    subscribers.add(q)

    def event_stream():
        try:
            pokemon = GamePokemon.query.filter_by(Guid=pokemonGuid).first()
            if pokemon:
                payload = {
                    "Health": pokemon.health,
                    "Status": pokemon.status,
                }
                yield f"data: {json.dumps(payload)}\n\n"

            while True:
                data = q.get()
                yield f"data: {json.dumps(data)}\n\n"
        finally:
            subscribers.remove(q)

    return Response(
        stream_with_context(event_stream()),
        mimetype="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no"
        }
    )

@app.route("/playerStateStream/<gameId>/<pokemonGuid>")
def player_state_stream(gameId, pokemonGuid):
    q = queue.Queue()

    clients.setdefault(pokemonGuid, set()).add(q)

    def stream():
        try:
            while True:
                data = q.get()
                yield f"data: {json.dumps(data)}\n\n"
        except GeneratorExit:
            clients[pokemonGuid].discard(q)

    return Response(stream(), mimetype="text/event-stream")

if __name__ == "__main__":
    with app.app_context():
        database.create_all()
    app.run("0.0.0.0", 9000, debug=True)
