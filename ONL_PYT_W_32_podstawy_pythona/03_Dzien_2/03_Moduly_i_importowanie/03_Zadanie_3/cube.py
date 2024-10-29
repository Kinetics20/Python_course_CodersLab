#!/usr/bin/python3
# from random import randint
# from random import randint
import random


def d6(num):
    result = 0

    for _ in range(num):
        result += random.randint(1, 6)

    return result

print(d6(100))