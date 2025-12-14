import random
import string

from sqlalchemy import Boolean
from .models import Move 

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

def serialize_move(m):
    return {
        "id": m.id,
        "name": m.name,
        "type": m.type.name,
        "basePower": m.basePower,
        "damageType": m.damageType.name if m.damageType else None,
        "priority": m.priority.name if m.priority else None,
        "target": m.target.name if m.target else None,
        "flavorText": m.flavorText,
        "effectText": m.effectText,
        "hasCritical": m.hasCritical,
        "hasLethal": m.hasLethal,
        "hasBlock": m.hasBlock,
        "hasRecoil": m.hasRecoil,
        "isMultiHit": m.isMultiHit,
        "multiHitCount": m.multiHitCount.name if m.multiHitCount else None,
    }

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
