import random
import string

def generate_game_id(length=10):
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))
