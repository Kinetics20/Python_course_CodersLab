#!/usr/bin/python3
from random import randint

size = randint(3, 9)
print('Wielkosc choinki: ', size)


def christmas_tree(i, j):
    for i in range(1, size + 1):
        for j in range(i):
            print("*", end="")
        print()
    return "|"


# print(f"{christmas_tree(size, size + 1)}")
christmas_tree(size, size + 1)