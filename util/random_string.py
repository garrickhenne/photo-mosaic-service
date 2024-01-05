import random
import string

def create_random_string():
    """
    Create a random string of length 8.
    """
    return ''.join(random.choice(string.ascii_lowercase) for i in range(8))