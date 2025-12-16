from flask import jsonify
from sqlalchemy import Boolean

from ..models.Moves import Move
from ..models.User import Game
from ..models.Pokemon import GamePokemon

from ..Enums.StatusTypes import StatusTypes

from Api.extensions import database

import random
import string

clients = {}

STAT_COST_RULES = {
    "core": lambda v: v * 10,
    "skills": lambda v: 6 if v == 0 else v * 8,
    "general": lambda v: 6 if v == 0 else v * 6,
    "will": lambda v: v * 3,
    "static50": lambda _: 50
}

STAT_TYPE = {
    # Core
    "Strength": "core",
    "Dexterity": "core",
    "Vitality": "core",
    "Insight": "core",
    "Special": "core",

    # Skills
    "Fight": "skills",
    "Survival": "skills",
    "Contest": "skills",

    # General
    "Brawl": "general",
    "Channel": "general",
    "Clash": "general",
    "Evasion": "general",
    "Alert": "general",
    "Athletic": "general",
    "Nature": "general",
    "Stealth": "general",
    "Allure": "general",
    "Etiquette": "general",
    "Intimidate": "general",
    "Perform": "general",

    # Will
    "Will": "will",

    # Static
    "Logic": "static50",
    "Instinct": "static50",
    "Primal": None,  # not buyable
}


def broadcast_player_update(pokemonGuid, **fields):
    payload = {
        "type": "update",
        "payload": fields
    }

    for q in clients.get(pokemonGuid, []):
        q.put(payload)

def generate_game_id(length=10):
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))

def enum_to_dict_list(enum_cls):
    return [{"id": e.name, "value": e.value} for e in enum_cls]

def enum_from_string(enum_class, value):
    if not value:
        raise ValueError("Enum value is required")
    
    # Try to match by name (case-insensitive)
    for member in enum_class:
        if member.name.lower() == value.lower() or member.value.lower() == value.lower():
            return member
    
    # If nothing matches, raise an error
    valid = ", ".join([f"{e.name} ('{e.value}')" for e in enum_class])
    raise ValueError(f"Invalid {enum_class.__name__}: {value}. Valid options: {valid}")

def getBooleanFields():
    boolean_fields = [
        column.name
        for column in Move.__table__.columns
        if isinstance(column.type, Boolean)
    ]
    return boolean_fields

def extract_modifiers_from_group(group, prefix):
    """
    Extracts modifiers from group.accuracyModifier1/2/3 or damageModifier1/2/3.
    prefix = 'accuracyModifier' or 'damageModifier'
    """
    if not group:
        return []

    fields = [f"{prefix}{i}" for i in (1,2,3)]
    mods = []

    for field in fields:
        value = getattr(group, field, None)
        if value is not None:
            mods.append(value.name)

    return mods

def updatePokemonHealth(game_id, guid, new_health):
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

def serialize_move(move):
    # ---- Accuracy & Damage Modifiers ----
    accuracy_mods = extract_modifiers_from_group(
        move.accuracy_modifier_group,
        "accuracyModifier"
    )

    damage_mods = extract_modifiers_from_group(
        move.damage_modifier_group,
        "damageModifier"
    )

    # ---- Heal Move ----
    heal_data = None
    if move.heal_move:
        heal_data = {
            "healType": move.heal_move.healType.name
                if move.heal_move.healType else None,
            "healAmount": move.heal_move.healAmount
        }

    # ---- Effects ----
    effects = [
        {
            "effect": conn.move_effect.effect.name,
            "effectLevel": conn.move_effect.effectLevel.name,
            "effectLevelDice": conn.move_effect.effectLevelDice
        }
        for conn in move.effect_connections
    ]

    # ---- Final Serialized Move ----
    return {
        "id": move.id,
        "name": move.name,
        "type": move.type.value if move.type else None,
        "damageType": move.damageType.name if move.damageType else None,
        "basePower": move.basePower,
        "target": move.target.value if move.target else None,
        "priority": move.priority.name if move.priority else None,
        "accuracyModifiers": accuracy_mods,
        "damageModifiers": damage_mods,
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
        "effectText": move.effectText or "",
        "flavorText": move.flavorText or "",
    }



