
import string
import random

def random_string(panjang:int)-> str:
    hasi_string = ''.join(random.choice(string.ascii_letters)for i in range(6))
    return hasi_string