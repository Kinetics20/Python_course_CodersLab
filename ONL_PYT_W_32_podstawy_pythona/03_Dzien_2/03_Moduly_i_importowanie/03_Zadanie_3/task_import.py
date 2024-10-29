#!/usr/bin/python3
import random
from random import randint

# 01
amount = randint(1, 6)


# my version
def d6_1(num):
    return num


print(d6_1(amount))


# 01

def d6(num):
    result = 0
    for _ in range(num):
        result += randint(1, 6)
    return result


print(d6(50))

# 02
# dla importu zlej paczki
# import random


def d6_3(num):
    result = 0
    for _ in range(num):
        result += random.randint(1, 6)
    return result


print(d6_3(50))
