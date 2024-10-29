#!/usr/bin/python3
from random import randint

size = randint(3, 9)
print('Wielkosc choinki: ', size)

for i in range(1, size + 1):
    for j in range(i):
        print("*", end="")
    print()
