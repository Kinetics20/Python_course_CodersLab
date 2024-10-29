#!/usr/bin/python3

# function_01
def mult_s(s):
    return s * s


print(f"square of {mult_s(5)} ")


# function_02
def mult_s_1(s):
    return s ** s


print(f"square of {mult_s_1(5)} ")

# function_03

import random

random_number = random.randint(1, 20)


def draw_numbers(i):
    return "*" * random_number


print(f"number is :{random_number}\nthe score is : {draw_numbers(random_number)}")

# function_04

rows = random.randint(5, 15)
columns = random.randint(5, 15)


def rows_columns(i, j):
    for x in range(i):
        print(f"{'*' * j}")
    return "|"


print(f"number of rows : {rows},number of columns : {columns}")
print(f"{rows_columns(rows, columns)}")

# function_05
num = random.randint(0, 10000)


def even_or_odd(number):
    return "type of number is : Odd" if number % 2 else "type of number is : Even"


print(even_or_odd(num))

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


print(build_tree(size, size + 1))


# function_07

def check_num(i):
    return "Odd" if i % 2 else "Even"


print(f'number is : {size}', check_num(size))
