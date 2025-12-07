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