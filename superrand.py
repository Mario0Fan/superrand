from random import random
from random import randint
def superrand():
    return ((randint(1,10) + randint(1,10)) + random())
def ultrarand():
    return ((randint(1,10) + randint(1,20)) + random()) * randint(1,10)
