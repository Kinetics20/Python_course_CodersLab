#!/usr/bin/python3
from random import randint

no_of_stars = randint(2, 5)
sth_stars = randint(2, 5)


def n_stars(x):
    return "*" * x


print(f"amount of stars : {no_of_stars}")
z = n_stars(no_of_stars)
print(z)


def n2_stars(x, y):
    for i in range(x):
        print(y * "*")


print(f"amount of stars : {no_of_stars}")
print(f"amount of sth : {sth_stars}")
z1 = n2_stars(no_of_stars, sth_stars)
# # print(z1)


size = randint(3, 9)
print(f'capacity of tree : {size}')

for row in range(1, size + 1):
    for col in range(row):
        print("*", end="")
    print()
