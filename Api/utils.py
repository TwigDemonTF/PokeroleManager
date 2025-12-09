import random
import string

from sqlalchemy import Boolean
from .models import Move 

def generate_game_id(length=10):
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))

def enum_to_dict_list(enum_cls):
    return [{"id": e.name, "value": e.value} for e in enum_cls]

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