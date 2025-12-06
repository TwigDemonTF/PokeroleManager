from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash

from .database import database
from .models import BasePokemon, GamePokemon, User, Game, GameEntities, Nature, Ability, Item, Garment
from .utils import generate_game_id

import secrets

# Set app
app = Flask(__name__)
CORS(app)
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
            .filter(GamePokemon.isNpc == False)
            .all()
        )

        if not allPokemon:
            return {"data": [], "message": "No characters found"}, 200

        result = []

        for p in allPokemon:

            base = p.basePokemon  # FK relationship

            # Resolve readable names for FK ids
            nature = Nature.query.get(p.natureId) if p.natureId else None
            ability = Ability.query.get(p.abilityId) if p.abilityId else None
            item = Item.query.get(p.itemId) if p.itemId else None

            # Get garments names as a list
            garments = [g.name for g in p.garments] if p.garments else []

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

                "BaseHealth": p.baseHealth or base.baseHealth,
                "Will": p.will or base.will,
                "Logic": p.logic or base.logic,
                "Instinct": p.instinct or base.instinct,
                "Primal": p.primal or base.primal,

                "PrimaryType": (p.primaryType.name if p.primaryType else (base.primaryType.name if base.primaryType else None)),
                "SecondaryType": (p.secondaryType.name if p.secondaryType else (base.secondaryType.name if base.secondaryType else None)),

                # Stats
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
            }

            result.append(data)

        return {"data": result}, 200


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

api.add_resource(Register, "/register")
api.add_resource(Login, "/login")
api.add_resource(PullCharacterData, "/PullCharacterData/<string:gameId>/<string:guid>")
api.add_resource(BasePokemonApi, "/basePokemon")
api.add_resource(GamePokemonApi, '/gamePokemon')
api.add_resource(GameApi, "/PullAllPokemon/<string:gameId>")
api.add_resource(NatureApi, "/nature")
api.add_resource(AbilityApi, "/ability")
api.add_resource(ItemApi, "/item")
api.add_resource(GarmentApi, "/garment")

if __name__ == "__main__":
    with app.app_context():
        database.create_all()
    app.run("0.0.0.0", 9000, debug=True)
