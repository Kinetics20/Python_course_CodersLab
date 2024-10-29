#!/usr/bin/python3


# function_06
import random

size = random.randint(3, 9)
print(f"Size of christmas tree : {size}")


def build_tree(i, j):
    for i in range(1, size + 1):
        for j in range(i):
            print("*", end="")
        print()
    return "|"


# print(build_tree(size, size + 1))
build_tree(size, size + 1)