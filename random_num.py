# Now we are going to print random number which will be from 1 to 100

# we are going to import random library module
from random import random


def rand_num():
    # this will return the number between 1 to 100
    return ((int)(random()*100))

print(f"Hey Computer can you give me a random number between 1 to 100 - {rand_num()}")
