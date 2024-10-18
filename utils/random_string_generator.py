import random
import string

def generate_random_string(length: int, digits_only: bool = False) -> str:
    if digits_only:
        characters = string.digits
    else:
        characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))
