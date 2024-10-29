#!/usr/bin/python3
from random import randint

rows = randint(5, 15)
columns = randint(5, 15)
print(f"Wartosc zmiennej rows : {rows}")
print(f"Wartosc zmiennej rows : {columns}")
for x in range(rows):
    print(f"{'*'* columns}")
