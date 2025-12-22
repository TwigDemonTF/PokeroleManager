from flask import request
from flask_restful import Resource

from ..models.Pokemon import GameEntities, GamePokemon
from ..models.Items import Item
from ..models.Misc import Ability, Nature
from ..models.User import Game

from ..Utils.utils import extract_modifiers_from_group

from Api.extensions import database

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
            
            bag_data = None

            if p.bag:
                bag_data = {
                    "bagId": p.bag.id,
                    "bagSize": p.bag.bagSize.value,
                    "items": [
                        {
                            "bagItemId": bi.id,
                            "item": bi.item.to_dict()
                        }
                        for bi in p.bag.items
                    ]
                }
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
                "Bag": bag_data,
                "Moves": moves_data,

                # ✔ Include IDs too
                "MoveIds": [mc.move.id for mc in p.move_connections],
            }

            result.append(pokemon_data)
        return {"data": result, "pokemons": result}, 200
