#!/usr/bin/python3

# Day_1_Task_review_from_prework_Exercise_03
import random

size = random.randint(3, 9)
print(f"Size of christmas tree : {size}")


def build_tree(i, j):
    for i in range(1, size + 1):
        for j in range(i):
            print("*", end="")
        print()
    return "|"


print(build_tree(size, size + 1))
