#!/usr/bin/python3
from random import randint

rows = randint(5, 10)
columns = randint(5, 10)


def print_start_pattern(rows, columns):
    for i in range(rows):
        print("*" * columns)


print_start_pattern(rows, columns)
