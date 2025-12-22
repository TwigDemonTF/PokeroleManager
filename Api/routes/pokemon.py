from flask import jsonify, request
from flask_restful import Resource

from ..models.Pokemon import BasePokemon, GamePokemon, GameEntities
from ..models.Items import PokemonBag, Garment
from ..models.User import Game

from ..Enums.BagSize import BagSizeEnum

from Api.extensions import database

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

                # User-input fields
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
                lethalHealth=0,
                will=raw.get("will"),
                logic=raw.get("logic"),
                instinct=raw.get("instinct"),
                primal=raw.get("primal"),

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

            # 4.5 Create and Attach Bag to Pokemon
            pokemonBag = PokemonBag(
                pokemonId=gamePokemon.id,
                bagSize=BagSizeEnum.size5
            )

            database.session.add(pokemonBag)
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
