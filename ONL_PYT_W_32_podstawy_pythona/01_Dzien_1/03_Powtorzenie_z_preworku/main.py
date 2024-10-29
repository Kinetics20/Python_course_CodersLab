#!/usr/bin/python3
from random import randint

no_of_stars = randint(1, 20)
# print(no_of_stars)
# print("*"*no_of_stars)

rows = randint(5, 15)
columns = randint(5, 15)
# print(f"Wartosc zmiennej rows : {rows}")
# print(f"Wartosc zmiennej rows : {columns}")
# for x in range(rows):
#     print(f"{'*'* columns}")

size = randint(3, 9)
print('Wielkosc choinki: ', size)

for i in range(1, size + 1):
    for j in range(i):
        print("*", end="")
    print()
