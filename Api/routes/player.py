from flask_restful import Resource

from Api.extensions import database
from ..models.Pokemon import GameEntities, GamePokemon
from ..models.User import Game
from ..models.Misc import Nature
from ..models.Misc import Ability
from ..models.Items import Item

from ..Utils.utils import extract_modifiers_from_group

class PlayerData(Resource):
    def get(self, gameId, playerGuid):
        pokemon = (
            database.session.query(GamePokemon)
            .join(GameEntities, GamePokemon.id == GameEntities.pokemonId)
            .join(Game, GameEntities.gameId == Game.id)
            .filter(Game.gameId == gameId)
            .filter(GamePokemon.Guid == playerGuid)
            .first()
        )

        if not pokemon:
            return {
                "message": "Pokémon not found for given GUID in this game"
            }, 404

        base = pokemon.basePokemon
        nature = Nature.query.get(pokemon.natureId) if pokemon.natureId else None
        ability = Ability.query.get(pokemon.abilityId) if pokemon.abilityId else None
        item = Item.query.get(pokemon.itemId) if pokemon.itemId else None

        bag_data = None
        if pokemon.bag:
            bag_data = {
                "id": pokemon.bag.id,
                "bagSize": pokemon.bag.bagSize.name if pokemon.bag.bagSize else None,
                "items": [
                    {
                        "id": bag_item.id,
                        "itemId": bag_item.itemId,
                        "name": bag_item.item.name if bag_item.item else None,
                        "itemCategory": bag_item.item.itemCategory.value if bag_item.item else None,
                        "minShopTier": bag_item.item.minShopTier.value if bag_item.item else None,
                        "effect": bag_item.item.effect if bag_item.item else None,
                        "effectKey": bag_item.item.effectKey if bag_item.item else None,
                        "effectData": bag_item.item.effectData if bag_item.item else None,
                        "isUsable": bag_item.item.isUsable if bag_item.item else None,
                        "isEquipable": bag_item.item.isEquipable if bag_item.item else None,
                        "description": bag_item.item.description or "",
                        "buyPrice": bag_item.item.buyPrice if bag_item.item else None,
                        "sellPrice": bag_item.item.sellPrice if bag_item.item else None,
                        "numUses": bag_item.item.numUses if bag_item.item else None,
                    }
                    for bag_item in pokemon.bag.items
                ]
            }

        moves_data = []

        for mc in pokemon.move_connections:
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

            effects = [
                {
                    "effect": conn.move_effect.effect.name,
                    "effectLevel": conn.move_effect.effectLevel.name,
                    "effectLevelDice": conn.move_effect.effectLevelDice
                }
                for conn in move.effect_connections
            ]

            moves_data.append({
                "id": move.id,
                "name": move.name,
                "type": move.type.value if move.type else None,
                "damageType": move.damageType.name if move.damageType else None,
                "basePower": move.basePower,
                "target": move.target.value if move.target else None,
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
            })

        pokemon_data = {
            "GameId": gameId,
            "Guid": pokemon.Guid,
            "Name": pokemon.name,
            "Level": pokemon.level,
            "Gender": pokemon.gender,
            "Age": pokemon.age,
            "Apples": pokemon.apples,

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
                "itemCategory": item.itemCategory.value,
                "minShopTier": item.minShopTier.value
            } if item else None,

            "Garments": [g.name for g in pokemon.garments],
            "Status": pokemon.status,

            "BaseHealth": pokemon.baseHealth or base.baseHealth,
            "Health": pokemon.health,
            "LethalHealth": pokemon.lethalHealth,

            "Will": pokemon.will or base.will,
            "Logic": pokemon.logic or base.logic,
            "Instinct": pokemon.instinct or base.instinct,
            "Primal": pokemon.primal or base.primal,

            "PrimaryType": pokemon.primaryType.value if pokemon.primaryType else base.primaryType.value,
            "SecondaryType": (
                pokemon.secondaryType.value if pokemon.secondaryType
                else base.secondaryType.value if base.secondaryType else None
            ),

            # Stats
            "Strength": pokemon.strength if pokemon.strength is not None else base.strength,
            "StrengthPotential": pokemon.strengthPotential if pokemon.strengthPotential is not None else base.strengthPotential,
            "Dexterity": pokemon.dexterity if pokemon.dexterity is not None else base.dexterity,
            "DexterityPotential": pokemon.dexterityPotential if pokemon.dexterityPotential is not None else base.dexterityPotential,
            "Vitality": pokemon.vitality if pokemon.vitality is not None else base.vitality,
            "VitalityPotential": pokemon.vitalityPotential if pokemon.vitalityPotential is not None else base.vitalityPotential,
            "Special": pokemon.special if pokemon.special is not None else base.special,
            "SpecialPotential": pokemon.specialPotential if pokemon.specialPotential is not None else base.specialPotential,
            "Insight": pokemon.insight if pokemon.insight is not None else base.insight,
            "InsightPotential": pokemon.insightPotential if pokemon.insightPotential is not None else base.insightPotential,

            # Skills
            "Fight": pokemon.fight if pokemon.fight is not None else base.fight,
            "Survival": pokemon.survival if pokemon.survival is not None else base.survival,
            "Contest": pokemon.contest if pokemon.contest is not None else base.contest,
            "Brawl": pokemon.brawl if pokemon.brawl is not None else base.brawl,
            "Channel": pokemon.channel if pokemon.channel is not None else base.channel,
            "Clash": pokemon.clash if pokemon.clash is not None else base.clash,
            "Evasion": pokemon.evasion if pokemon.evasion is not None else base.evasion,
            "Alert": pokemon.alert if pokemon.alert is not None else base.alert,
            "Athletic": pokemon.athletic if pokemon.athletic is not None else base.athletic,
            "NatureStat": pokemon.natureStat if pokemon.natureStat is not None else base.natureStat,
            "Stealth": pokemon.stealth if pokemon.stealth is not None else base.stealth,
            "Allure": pokemon.allure if pokemon.allure is not None else base.allure,
            "Etiquette": pokemon.etiquette if pokemon.etiquette is not None else base.etiquette,
            "Intimidate": pokemon.intimidate if pokemon.intimidate is not None else base.intimidate,
            "Perform": pokemon.perform if pokemon.perform is not None else base.perform,

            "ExperiencePoints": pokemon.experiencePoints,
            "IsNpc": pokemon.isNpc,
            "PlayerColor": pokemon.playerColor,

            "Moves": moves_data,
            "MoveIds": [mc.move.id for mc in pokemon.move_connections],

            "Bag": bag_data
        }

        return {"data": pokemon_data}, 200
