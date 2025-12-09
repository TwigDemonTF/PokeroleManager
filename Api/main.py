from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash

from .database import database
from .models import BasePokemon, GamePokemon, User, Game, GameEntities, Nature, Ability, Item, Garment, AccuracyModifierGroup, DamageModifierGroup, HealMove, MoveEffect, MoveEffectConnection, Move, MoveConnection
from .utils import generate_game_id, enum_to_dict_list, getBooleanFields, extract_modifiers_from_group

from .Enums.Types import Types as TypeEnum
from .Enums.Move.DamageType import DamageTypeEnum
from .Enums.Move.EffectLevel import EffectLevelEnum
from .Enums.Move.HealMoveTypes import HealMoveTypesEnum
from .Enums.Move.HitCount import HitCountEnum
from .Enums.Move.Modifier import ModifierEnum
from .Enums.Move.MoveEffectType import MoveEffectTypeEnum
from .Enums.Move.Priority import PriorityEnum
from .Enums.Move.Target import TargetEnum

import secrets

# Set app
app = Flask(__name__)
CORS(app, origins=["*"])
api = Api(app)

# Database Config
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

database.init_app(app)

class BasePokemonApi(Resource):
    def get(self):
        base_pokemon = BasePokemon.query.all()

        data = []

        for p in base_pokemon:
            data.append({
                "id": p.id,
                "name": p.name
            })

        return jsonify(data)
    
    def post(self):
        raw = request.get_json()
        print("Incomming JSON:", raw)

        if raw is None:
            return {"error": "No JSON received"}, 400

        try:
            basePokemon = BasePokemon(
                name=raw.get("Name"),
                baseHealth=raw.get("BaseHealth"),
                primaryType=raw.get("PrimaryType"),
                secondaryType=raw.get("secondaryType"),
                strength=raw.get("Strength"),
                strengthPotential=raw.get("StrengthPotential"),
                dexterity=raw.get("Dexterity"),
                dexterityPotential=raw.get("DexterityPotential"),
                vitality=raw.get("Vitality"),
                vitalityPotential=raw.get("VitalityPotential"),
                special=raw.get("Special"),
                specialPotential=raw.get("SpecialPotential"),
                insight=raw.get("Insight"),
                insightPotential=raw.get("InsightPotential"),

                fight=raw.get("Fight"),
                survival=raw.get("Survival"),
                contest=raw.get("Contest"),
                brawl=raw.get("Brawl"),
                channel=raw.get("Channel"),
                clash=raw.get("Clash"),
                evasion=raw.get("Evasion"),
                alert=raw.get("Alert"),
                athletic=raw.get("Atheletic"),
                natureStat=raw.get("NatureStat"),
                stealth=raw.get("Stealth"),
                allure=raw.get("Allure"),
                etiquette=raw.get("Etiquette"),
                intimidate=raw.get("Intimidate"),
                perform=raw.get("Perform")
            )
            database.session.add(basePokemon)
            database.session.commit()

        except Exception as e:
            print("DB ERROR:", e)
            database.session.rollback()
            return {"error": str(e)}, 500

        return {
                "message": f"Created Pokémon '{basePokemon.name}'",
                "pokemonId": basePokemon.id,
            }, 201

class GamePokemonApi(Resource):
    def post(self):
        raw = request.get_json()
        print("Incoming JSON:", raw)

        if raw is None:
            return {"error": "No JSON received"}, 400

        try:
            # 1. Fetch Game using gameId (lowercase from form)
            game = Game.query.filter_by(gameId=raw.get("gameId")).first()
            if not game:
                return {"error": "Game not found"}, 404

            # 2. Load BasePokemon
            base = BasePokemon.query.get(raw.get("basePokemonId"))
            if not base:
                return {"error": "BasePokemon not found"}, 404

            # 3. Create GamePokemon
            gamePokemon = GamePokemon(
                basePokemonId=base.id,

                # User-input fields (use correct model names)
                name=raw.get("name"),
                level=raw.get("level"),
                gender=raw.get("gender"),
                age=raw.get("age"),

                natureId=raw.get("natureId"),
                abilityId=raw.get("abilityId"),
                status=raw.get("status"),

                itemId=raw.get("itemId"),
                isNpc=raw.get("isNpc", False),
                experiencePoints=raw.get("experiencePoints", 0),
                playerColor=raw.get("playerColor"),
                Guid=raw.get("Guid"),

                # Base stats
                baseHealth=base.baseHealth,
                health=base.baseHealth + base.vitality,
                will=base.will,
                logic=base.logic,
                instinct=base.instinct,
                primal=base.primal,

                primaryType=base.primaryType,
                secondaryType=base.secondaryType,

                strength=base.strength,
                strengthPotential=base.strengthPotential,
                dexterity=base.dexterity,
                dexterityPotential=base.dexterityPotential,
                vitality=base.vitality,
                vitalityPotential=base.vitalityPotential,
                special=base.special,
                specialPotential=base.specialPotential,
                insight=base.insight,
                insightPotential=base.insightPotential,

                fight=base.fight,
                survival=base.survival,
                contest=base.contest,
                brawl=base.brawl,
                channel=base.channel,
                clash=base.clash,
                evasion=base.evasion,
                alert=base.alert,
                athletic=base.athletic,
                natureStat=base.natureStat,
                stealth=base.stealth,
                allure=base.allure,
                etiquette=base.etiquette,
                intimidate=base.intimidate,
                perform=base.perform,
            )

            database.session.add(gamePokemon)
            database.session.commit()

            # 4. Attach garments (MANY-TO-MANY)
            garment_ids = raw.get("garments", [])
            for gid in garment_ids:
                garment = Garment.query.get(gid)
                if garment:
                    gamePokemon.garments.append(garment)

            database.session.commit()

            # 5. Link Pokémon into gameEntities table
            gameEntity = GameEntities(
                gameId=game.id,
                pokemonId=gamePokemon.id,
            )
            database.session.add(gameEntity)
            database.session.commit()

        except Exception as e:
            print("DB ERROR:", e)
            database.session.rollback()
            return {"error": str(e)}, 500

        return {
            "message": f"Created Pokémon '{gamePokemon.name}' in Game '{game.gameId}'",
            "pokemonId": gamePokemon.id,
            "gameEntityId": gameEntity.id
        }, 201

class Register(Resource):
    def get(self):
        return render_template_string(register_template)

    def post(self):
        data = request.form if request.form else request.json

        username: str = data.get("username")
        password: str = data.get("password")

        if not username or not password:
            return {"message": "Username & password required"}, 400

        if User.query.filter_by(username=username).first():
            return {"message": "Username already exists"}, 409

        # Generate a cryptographically secure random salt
        salt: str = secrets.token_hex(32)  # 64 chars

        # Hash salt + password
        hashed: str = generate_password_hash(salt + password)

        newUser: User= User(
            username=username,
            password=hashed,
            passwordSalt=salt
        )

        database.session.add(newUser)
        database.session.commit()

        userGame = Game(
            gameId=generate_game_id(10),
            weather="None",
            userId=newUser.id
        )

        database.session.add(userGame)
        database.session.commit()

        return {"message": "User registered successfully"}, 201

class Login(Resource):
    def get(self):
        return render_template_string(login_template)

    def post(self):
        data = request.form if request.form else request.json

        username = data.get("username")
        password = data.get("password")

        user = User.query.filter_by(username=username).first()
        if not user:
            return {"message": "Invalid username or password"}, 401

        # Recreate salted hash input
        salted_input = user.passwordSalt + password

        if not check_password_hash(user.password, salted_input):
            return {"message": "Invalid username or password"}, 401

        game_Id = Game.query.filter_by(userId=user.id).first().gameId
        return {"message": f"Welcome, {username}!", "userId": user.id, "gameId": game_Id}, 200

class PullCharacterData(Resource):
    def get(self, gameId, guid):
        targetPokemon = (
            database.session.query(GamePokemon)
            .join(GameEntities, GamePokemon.id == GameEntities.pokemonId)
            .join(Game, GameEntities.gameId == Game.id)
            .filter(Game.gameId == gameId)          # gameId = your string code
            .filter(GamePokemon.Guid == guid)        # guid = 6-char GUID
            .first()
        )

        if not targetPokemon:
            return {
                "data": None,
                "message": "Character not found"
            }, 404

        base = targetPokemon.basePokemon

        # Merge GamePokemon + BasePokemon fields into one dict
        data = {
            "GameId": gameId,
            "Guid": targetPokemon.Guid,
            "Name": targetPokemon.name,
            "Level": targetPokemon.level,
            "Gender": targetPokemon.gender,
            "Age": targetPokemon.age,
            "Nature": targetPokemon.nature,
            "Ability": targetPokemon.ability,
            "BaseHealth": targetPokemon.baseHealth or base.baseHealth,
            "Will": targetPokemon.will or base.will,
            "Logic": targetPokemon.logic or base.logic,
            "Instinct": targetPokemon.instinct or base.instinct,
            "Primal": targetPokemon.primal or base.primal,
            "HeldItem": targetPokemon.heldItem,
            "Garment1": targetPokemon.garment1,
            "Garment2": targetPokemon.garment2,
            "Garment3": targetPokemon.garment3,
            "Status": targetPokemon.status,
            "PrimaryType": targetPokemon.primaryType or base.primaryType,
            "SecondaryType": targetPokemon.secondaryType or base.secondaryType,

            # Stats — fallback to BasePokemon values if GamePokemon hasn’t modified them
            "Strength": targetPokemon.strength or base.strength,
            "StrengthPotential": targetPokemon.strengthPotential or base.strengthPotential,
            "Dexterity": targetPokemon.dexterity or base.dexterity,
            "DexterityPotential": targetPokemon.dexterityPotential or base.dexterityPotential,
            "Vitality": targetPokemon.vitality or base.vitality,
            "VitalityPotential": targetPokemon.vitalityPotential or base.vitalityPotential,
            "Special": targetPokemon.special or base.special,
            "SpecialPotential": targetPokemon.specialPotential or base.specialPotential,
            "Insight": targetPokemon.insight or base.insight,
            "InsightPotential": targetPokemon.insightPotential or base.insightPotential,

            # Skills
            "Fight": targetPokemon.fight or base.fight,
            "Survival": targetPokemon.survival or base.survival,
            "Contest": targetPokemon.contest or base.contest,
            "Brawl": targetPokemon.brawl or base.brawl,
            "Channel": targetPokemon.channel or base.channel,
            "Clash": targetPokemon.clash or base.clash,
            "Evasion": targetPokemon.evasion or base.evasion,
            "Alert": targetPokemon.alert or base.alert,
            "Athletic": targetPokemon.athletic or base.athletic,
            "NatureStat": targetPokemon.natureStat or base.natureStat,
            "Stealth": targetPokemon.stealth or base.stealth,
            "Allure": targetPokemon.allure or base.allure,
            "Etiquette": targetPokemon.etiquette or base.etiquette,
            "Intimidate": targetPokemon.intimidate or base.intimidate,
            "Perform": targetPokemon.perform or base.perform,

            "ExperiencePoints": targetPokemon.experiencePoints,
            "IsNpc": targetPokemon.isNpc,
            "PlayerColor": targetPokemon.playerColor,
        }

        return {"data": data}, 200

class GameApi(Resource):
    def get(self, gameId):

        # Get all NON-NPC pokemon for this game
        allPokemon = (
            database.session.query(GamePokemon)
            .join(GameEntities, GamePokemon.id == GameEntities.pokemonId)
            .join(Game, GameEntities.gameId == Game.id)
            .filter(Game.gameId == gameId)
            # .filter(GamePokemon.isNpc == False)
            .all()
        )

        if not allPokemon:
            return {"data": [], "message": "No characters found"}, 200

        result = []

        for p in allPokemon:

            base = p.basePokemon  # FK relationship

            nature = Nature.query.get(p.natureId) if p.natureId else None
            ability = Ability.query.get(p.abilityId) if p.abilityId else None
            item = Item.query.get(p.itemId) if p.itemId else None

            moves_data = []

            # --- Build full move objects properly ---
            for mc in p.move_connections:
                move = mc.move

                # Accuracy mods
                acc_mods = extract_modifiers_from_group(
                    move.accuracy_modifier_group,
                    "accuracyModifier"
                )

                # Damage mods
                dmg_mods = extract_modifiers_from_group(
                    move.damage_modifier_group,
                    "damageModifier"
                )

                # Heal move
                heal_data = None
                if move.heal_move:
                    heal_data = {
                        "healType": move.heal_move.healType.name if move.heal_move.healType else None,
                        "healAmount": move.heal_move.healAmount
                    }

                # Effects
                effects = []
                for conn in move.effect_connections:
                    me = conn.move_effect
                    effects.append({
                        "effect": me.effect.name,
                        "effectLevel": me.effectLevel.name,
                        "effectLevelDice": me.effectLevelDice
                    })

                # Final move object (matching frontend!)
                move_json = {
                    "id": move.id,
                    "name": move.name,
                    "type": move.type.name if move.type else None,
                    "damageType": move.damageType.name if move.damageType else None,

                    "basePower": move.basePower,
                    "target": move.target.name if move.target else None,
                    "priority": move.priority.name if move.priority else None,

                    "accuracyModifiers": acc_mods,
                    "damageModifiers": dmg_mods,
                    "reducedAccuracy": move.reducedAccuracy,

                    "hasCritical": move.hasCritical,
                    "hasLethal": move.hasLethal,
                    "hasBlock": move.hasBlock,
                    "hasRecoil": move.hasRecoil,
                    "hasWeatherChange": move.hasWeatherChange,
                    "weatherChangeTo": move.weatherChangeTo.name if move.weatherChangeTo else None,
                    "hasModifiedDamage": move.hasModifiedDamage,
                    "alwaysHitEffect": move.alwaysHitEffect,
                    "alwaysFailEffect": move.alwaysFailEffect,
                    "isChargeMove": move.isChargeMove,
                    "isFistBased": move.isFistBased,
                    "isHighCrit": move.isHighCrit,
                    "isNeverFail": move.isNeverFail,
                    "isHealingMove": move.isHealingMove,
                    "isShieldMove": move.isShieldMove,
                    "isSoundBased": move.isSoundBased,
                    "isMultiHit": move.isMultiHit,
                    "multiHitCount": move.multiHitCount.name if move.multiHitCount else None,
                    "isSwitchMove": move.isSwitchMove,
                    "requiresRecharge": move.requiresRecharge,

                    "healMove": heal_data,
                    "effects": effects,
                    "effectText": move.effectText,
                    "flavorText": move.flavorText,
                }

                moves_data.append(move_json)

            # ——— Build Pokémon Output ———
            data = {
                "GameId": gameId,
                "Guid": p.Guid,
                "Name": p.name,
                "Level": p.level,
                "Gender": p.gender,
                "Age": p.age,
                "Nature": nature.name if nature else None,
                "Ability": ability.name if ability else None,
                "HeldItem": item.name if item else None,
                "Garments": [g.name for g in p.garments] if p.garments else [],
                "Status": p.status,

                # Core stats
                "BaseHealth": p.baseHealth or base.baseHealth,
                "Will": p.will or base.will,
                "Logic": p.logic or base.logic,
                "Instinct": p.instinct or base.instinct,
                "Primal": p.primal or base.primal,

                # Types
                "PrimaryType": (p.primaryType.name if p.primaryType else (base.primaryType.name if base.primaryType else None)),
                "SecondaryType": (p.secondaryType.name if p.secondaryType else (base.secondaryType.name if base.secondaryType else None)),

                # Attributes
                "Strength": p.strength or base.strength,
                "StrengthPotential": p.strengthPotential or base.strengthPotential,
                "Dexterity": p.dexterity or base.dexterity,
                "DexterityPotential": p.dexterityPotential or base.dexterityPotential,
                "Vitality": p.vitality or base.vitality,
                "VitalityPotential": p.vitalityPotential or base.vitalityPotential,
                "Special": p.special or base.special,
                "SpecialPotential": p.specialPotential or base.specialPotential,
                "Insight": p.insight or base.insight,
                "InsightPotential": p.insightPotential or base.insightPotential,

                # Skills
                "Fight": p.fight or base.fight,
                "Survival": p.survival or base.survival,
                "Contest": p.contest or base.contest,
                "Brawl": p.brawl or base.brawl,
                "Channel": p.channel or base.channel,
                "Clash": p.clash or base.clash,
                "Evasion": p.evasion or base.evasion,
                "Alert": p.alert or base.alert,
                "Athletic": p.athletic or base.athletic,
                "NatureStat": p.natureStat or base.natureStat,
                "Stealth": p.stealth or base.stealth,
                "Allure": p.allure or base.allure,
                "Etiquette": p.etiquette or base.etiquette,
                "Intimidate": p.intimidate or base.intimidate,
                "Perform": p.perform or base.perform,

                "ExperiencePoints": p.experiencePoints,
                "IsNpc": p.isNpc,
                "PlayerColor": p.playerColor,

                # ✔ Full move objects returned
                "Moves": moves_data,

                # IDs too (frontend uses these for dropdown)
                "MoveIds": [mc.move.id for mc in p.move_connections],
            }

            result.append(data)

        return {"data": result, "pokemons": result}, 200

class BattleApi(Resource):
    def post(self):
        """
        POST /api/pokemon/batch
        Body: { "guids": ["GUID1", "GUID2"], "gameId": "game123" }
        Returns full Pokémon data for the requested GUIDs in that game.
        Includes full move objects identical to GameApi.
        """
        data = request.get_json()
        if not data:
            return {"message": "No data provided", "data": []}, 400

        guids = data.get("guids")
        game_id = data.get("gameId")
        if not guids or not isinstance(guids, list):
            return {"message": "GUIDs must be a non-empty list", "data": []}, 400
        if not game_id:
            return {"message": "gameId is required", "data": []}, 400

        pokemons = (
            database.session.query(GamePokemon)
            .join(GameEntities, GamePokemon.id == GameEntities.pokemonId)
            .join(Game, GameEntities.gameId == Game.id)
            .filter(Game.gameId == game_id)
            .filter(GamePokemon.Guid.in_(guids))
            .all()
        )

        if not pokemons:
            return {
                "data": [],
                "message": "No Pokémon found for given GUIDs in this game"
            }, 200

        result = []

        for p in pokemons:
            base = p.basePokemon

            nature = Nature.query.get(p.natureId) if p.natureId else None
            ability = Ability.query.get(p.abilityId) if p.abilityId else None
            item = Item.query.get(p.itemId) if p.itemId else None

            # ---------- MOVE PROCESSING (COPIED FROM GameApi) ----------
            moves_data = []

            for mc in p.move_connections:
                move = mc.move

                acc_mods = extract_modifiers_from_group(
                    move.accuracy_modifier_group,
                    "accuracyModifier"
                )

                dmg_mods = extract_modifiers_from_group(
                    move.damage_modifier_group,
                    "damageModifier"
                )

                heal_data = None
                if move.heal_move:
                    heal_data = {
                        "healType": move.heal_move.healType.name
                            if move.heal_move.healType else None,
                        "healAmount": move.heal_move.healAmount
                    }

                effects = []
                for conn in move.effect_connections:
                    me = conn.move_effect
                    effects.append({
                        "effect": me.effect.name,
                        "effectLevel": me.effectLevel.name,
                        "effectLevelDice": me.effectLevelDice
                    })

                move_json = {
                    "id": move.id,
                    "name": move.name,
                    "type": move.type.name if move.type else None,
                    "damageType": move.damageType.name if move.damageType else None,

                    "basePower": move.basePower,
                    "target": move.target.name if move.target else None,
                    "priority": move.priority.name if move.priority else None,

                    "accuracyModifiers": acc_mods,
                    "damageModifiers": dmg_mods,
                    "reducedAccuracy": move.reducedAccuracy,

                    "hasCritical": move.hasCritical,
                    "hasLethal": move.hasLethal,
                    "hasBlock": move.hasBlock,
                    "hasRecoil": move.hasRecoil,
                    "hasWeatherChange": move.hasWeatherChange,
                    "weatherChangeTo": move.weatherChangeTo.name
                        if move.weatherChangeTo else None,
                    "hasModifiedDamage": move.hasModifiedDamage,
                    "alwaysHitEffect": move.alwaysHitEffect,
                    "alwaysFailEffect": move.alwaysFailEffect,
                    "isChargeMove": move.isChargeMove,
                    "isFistBased": move.isFistBased,
                    "isHighCrit": move.isHighCrit,
                    "isNeverFail": move.isNeverFail,
                    "isHealingMove": move.isHealingMove,
                    "isShieldMove": move.isShieldMove,
                    "isSoundBased": move.isSoundBased,
                    "isMultiHit": move.isMultiHit,
                    "multiHitCount": move.multiHitCount.name
                        if move.multiHitCount else None,
                    "isSwitchMove": move.isSwitchMove,
                    "requiresRecharge": move.requiresRecharge,

                    "healMove": heal_data,
                    "effects": effects,
                    "effectText": move.effectText,
                    "flavorText": move.flavorText,
                }

                moves_data.append(move_json)

            # ---------- POKÉMON CORE DATA ----------
            pokemon_data = {
                "GameId": game_id,
                "Guid": p.Guid,
                "Name": p.name,
                "Level": p.level,
                "Gender": p.gender,
                "Age": p.age,

                "Nature": {
                    "name": nature.name,
                    "description": nature.description,
                } if nature else None,

                "Ability": {
                    "name": ability.name,
                    "flavorText": ability.flavorText,
                    "effect": ability.effect,
                } if ability else None,

                "HeldItem": {
                    "name": item.name,
                    "description": item.description,
                    "effect": item.effect,
                } if item else None,

                "Garments": [g.name for g in p.garments] if p.garments else [],
                "Status": p.status,

                "BaseHealth": p.baseHealth or base.baseHealth,
                "Health": p.health,

                "Will": p.will or base.will,
                "Logic": p.logic or base.logic,
                "Instinct": p.instinct or base.instinct,
                "Primal": p.primal or base.primal,

                "PrimaryType": (
                    p.primaryType.name if p.primaryType
                    else base.primaryType.name if base.primaryType
                    else None
                ),
                "SecondaryType": (
                    p.secondaryType.name if p.secondaryType
                    else base.secondaryType.name if base.secondaryType
                    else None
                ),

                # Stats
                "Strength": p.strength if p.strength is not None else base.strength,
                "StrengthPotential": p.strengthPotential if p.strengthPotential is not None else base.strengthPotential,
                "Dexterity": p.dexterity if p.dexterity is not None else base.dexterity,
                "DexterityPotential": p.dexterityPotential if p.dexterityPotential is not None else base.dexterityPotential,
                "Vitality": p.vitality if p.vitality is not None else base.vitality,
                "VitalityPotential": p.vitalityPotential if p.vitalityPotential is not None else base.vitalityPotential,
                "Special": p.special if p.special is not None else base.special,
                "SpecialPotential": p.specialPotential if p.specialPotential is not None else base.specialPotential,
                "Insight": p.insight if p.insight is not None else base.insight,
                "InsightPotential": p.insightPotential if p.insightPotential is not None else base.insightPotential,

                # Skills
                "Fight": p.fight if p.fight is not None else base.fight,
                "Survival": p.survival if p.survival is not None else base.survival,
                "Contest": p.contest if p.contest is not None else base.contest,
                "Brawl": p.brawl if p.brawl is not None else base.brawl,
                "Channel": p.channel if p.channel is not None else base.channel,
                "Clash": p.clash if p.clash is not None else base.clash,
                "Evasion": p.evasion if p.evasion is not None else base.evasion,
                "Alert": p.alert if p.alert is not None else base.alert,
                "Athletic": p.athletic if p.athletic is not None else base.athletic,
                "NatureStat": p.natureStat if p.natureStat is not None else base.natureStat,
                "Stealth": p.stealth if p.stealth is not None else base.stealth,
                "Allure": p.allure if p.allure is not None else base.allure,
                "Etiquette": p.etiquette if p.etiquette is not None else base.etiquette,
                "Intimidate": p.intimidate if p.intimidate is not None else base.intimidate,
                "Perform": p.perform if p.perform is not None else base.perform,

                "ExperiencePoints": p.experiencePoints,
                "IsNpc": p.isNpc,
                "PlayerColor": p.playerColor,

                # ✔ Added full moves (NOW MATCHES GameApi)
                "Moves": moves_data,

                # ✔ Include IDs too
                "MoveIds": [mc.move.id for mc in p.move_connections],
            }

            result.append(pokemon_data)
        return {"data": result, "pokemons": result}, 200

class NatureApi(Resource):
    def post(self):
        data = request.get_json()

        newNature = Nature(
            name=data.get("Name"),
            description=data.get("Description"),
        )
        database.session.add(newNature)
        database.session.commit()
    
    def get(self):
        natures = Nature.query.all()

        data = [{"id": None, "name": "None"}]

        for n in natures:
            data.append({
                "id": n.id,
                "name": n.name
            })

        return jsonify(data)

class AbilityApi(Resource):
    def post(self):
        data = request.get_json()

        newAbility = Ability(
            name=data.get("Name"),
            flavorText=data.get("FlavorText"),
            effect=data.get("Effect")
        )
        database.session.add(newAbility)
        database.session.commit()

    def get(self):
        abilities = Ability.query.all()

        data = [{"id": None, "name": "None"}]

        for a in abilities:
            data.append({
                "id": a.id,
                "name": a.name
            })

        return jsonify(data)

class ItemApi(Resource):
    def post(self):
        data = request.get_json()

        newItem = Item(
            name=data.get("Name"),
            description=data.get("Description"),
            effect=data.get("Effect")
        )
        database.session.add(newItem)
        database.session.commit()
    
    def get(self):
        items = Item.query.all()

        data = [{"id": None, "name": "None"}]

        for i in items:
            data.append({
                "id": i.id,
                "name": i.name
            })

        return jsonify(data)

class GarmentApi(Resource):
    def get(self):
        garments = Garment.query.all()

        data = [{"id": None, "name": "None"}]

        for g in garments:
            data.append({
                "id": g.id,
                "name": g.name
            })

        return jsonify(data)

class MoveApi(Resource):
    def post(self):
        try:
            data = request.get_json()

            # required
            name = data.get("name")
            move_type = data.get("type")
            damage_type = data.get("damageType")

            if not name or not move_type or not damage_type:
                return {"error": "name, type, and damageType are required"}, 400

            move = Move(
                name=name,
                type=TypeEnum[move_type],
                damageType=DamageTypeEnum[damage_type]
            )

            # numeric fields
            move.basePower = data.get("basePower")
            move.reducedAccuracy = data.get("reducedAccuracy")

            # enums
            if data.get("priority"):
                move.priority = PriorityEnum[data["priority"]]

            if data.get("target"):
                move.target = TargetEnum[data["target"]]

            if data.get("multiHitCount"):
                move.multiHitCount = HitCountEnum[data["multiHitCount"]]

            # booleans
            boolean_flags = [
                "hasCritical", "hasLethal", "hasBlock", "hasRecoil", "hasWeatherChange",
                "hasModifiedDamage", "alwaysHitEffect", "alwaysFailEffect",
                "isChargeMove", "isFistBased", "isHighCrit", "isNeverFail",
                "isHealingMove", "isShieldMove", "isSoundBased", "isMultiHit",
                "isSwitchMove", "requiresRecharge"
            ]

            for flag in boolean_flags:
                if flag in data:
                    setattr(move, flag, bool(data[flag]))

            # relations
            move.healingTypeId = data.get("healingTypeId")
            move.accuracyModifiersId = data.get("accuracyModifiersId")
            move.damageModifiersId = data.get("damageModifiersId")
            move.modifiedDamageId = data.get("modifiedDamageId")

            database.session.add(move)
            database.session.commit()

            return {"success": True, "moveId": move.id}, 200

        except Exception as e:
            database.session.rollback()
            return {"error": str(e)}, 500

class AddMove(Resource):
    def get(self):
        data = {
            "types": enum_to_dict_list(TypeEnum),
            "damageTypes": enum_to_dict_list(DamageTypeEnum),
            "priority": enum_to_dict_list(PriorityEnum),
            "targets": enum_to_dict_list(TargetEnum),
            "multiHits": enum_to_dict_list(HitCountEnum),
            "healTypes": enum_to_dict_list(HealMoveTypesEnum),
            "accuracyModifiers": enum_to_dict_list(ModifierEnum),
            "damageModifiers":  enum_to_dict_list(ModifierEnum),
            "booleanFields": getBooleanFields()
        }

        return data, 200
    def post(self):
        data = request.get_json()

        print(data)

        # --- 1. Create AccuracyModifierGroup ---
        accuracy_group = AccuracyModifierGroup(
            accuracyModifier1=ModifierEnum[data["accuracyModifier1"]],
            accuracyModifier2=ModifierEnum[data["accuracyModifier2"]],
            accuracyModifier3=ModifierEnum[data["accuracyModifier3"]],
        )
        database.session.add(accuracy_group)
        database.session.flush()  # Flush to get accuracy_group.id

        # --- 2. Create DamageModifierGroup ---
        damage_group = DamageModifierGroup(
            damageModifier1=ModifierEnum[data["damageModifier1"]],
            damageModifier2=ModifierEnum[data["damageModifier2"]],
            damageModifier3=ModifierEnum[data["damageModifier3"]],
        )
        database.session.add(damage_group)
        database.session.flush()  # Flush to get damage_group.id

        booleanFields = getBooleanFields()
        def parse_bool(key):
            return key in data
        
        boolean_values = {field: parse_bool(field) for field in booleanFields}

        # --- 3. Create Move ---
        move = Move(
            name=data["Name"],
            effectText=data.get("effectText"),
            flavorText=data.get("flavorText"),
            basePower=int(data.get("basePower", 0)),
            reducedAccuracy=int(data.get("reducedAccuracy", 0)),
            type=TypeEnum[data["types"]],
            damageType=DamageTypeEnum[data["damageTypes"]],
            priority=PriorityEnum(int(data.get("priority", 0))),
            target=TargetEnum[data["targets"]],
            multiHitCount=HitCountEnum(int(data.get("multiHits", 1))),
            healingTypeId=None,  # Set if needed
            accuracyModifiersId=accuracy_group.id,
            damageModifiersId=damage_group.id,
            **boolean_values
        )

        database.session.add(move)
        database.session.commit()

        return jsonify({"status": "success", "move_id": move.id})

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
        # REPLACE MOVE
        # ------------------------------------------------------------
        if replace_index is not None:
            replace_index = int(replace_index)

            if replace_index < 0 or replace_index >= 4:
                return {"error": "ReplaceIndex must be 0-3"}, 400

            if replace_index >= move_count:
                return {"error": f"No move exists at index {replace_index}"}, 400

            if any(mc.moveId == move_id for mc in current_moves):
                return {"error": "Pokémon already knows this move"}, 400

            mc = current_moves[replace_index]
            mc.moveId = move_id
            database.session.commit()

            return {
                "message": "Move replaced",
                "slot": replace_index,
                "move": move.name
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

api.add_resource(Register, "/register")
api.add_resource(Login, "/login")
api.add_resource(PullCharacterData, "/PullCharacterData/<string:gameId>/<string:guid>")
api.add_resource(BasePokemonApi, "/basePokemon")
api.add_resource(GamePokemonApi, '/gamePokemon')
api.add_resource(GameApi, "/PullAllPokemon/<string:gameId>")
api.add_resource(BattleApi, '/battleData')
api.add_resource(NatureApi, "/nature")
api.add_resource(AbilityApi, "/ability")
api.add_resource(ItemApi, "/item")
api.add_resource(GarmentApi, "/garment")
api.add_resource(MoveManipulation, "/moveManipulation")

api.add_resource(AddMove, "/addMove")

if __name__ == "__main__":
    with app.app_context():
        database.create_all()
    app.run("0.0.0.0", 9000, debug=True)
