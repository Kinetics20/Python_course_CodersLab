#!/usr/bin/python3


import random

size = random.randint(0, 30)
a = random.randint(0, 10)
b = random.randint(0, 10)
c = random.randint(0, 10)
d = random.randint(0, 10)
h = random.randint(0, 10)

print(" ")


# function_01
def check_num(i):
    return "Odd" if i % 2 else "Even"


print(size, "\n", check_num(size))
print(" ")


# function_02
def cals_triangle_area(i, d):
    return 0.5 * i * d


print(f'Triangle area for a = {a} and h = {h} is {cals_triangle_area(a, h)}')


# function_02
def cals_square_area(i):
    return i * i


print(f'square area is {cals_square_area(a)}', a)


# function_03
def cals_rectangle_area(i, z):
    return i * z


print(f'square area is {cals_rectangle_area(a, b)}', a, b)


# function_04
def cals_parall_area(i, z):
    return i * z


print(f'square area is {cals_parall_area(a, h)}', a, h)


# function_05
def cals_rhombus_area(i, z):
    return i * z


print(f'square area is {cals_rhombus_area(a, h)}', a, h)


# function_06
def cals_trapezoid_area(i, j, z):
    return 0.5 * (i + j) * h


print(f'square area is {cals_trapezoid_area(a, b, h)}', a, b, h)


# function_07
def cals_circle_area(z):
    return (z / 2) * 3.14


print(f'square area is {cals_circle_area(d)}', d)


def multi_test(a, b, c=20):
    return (a + b) / c


print(multi_test(a, b))
print(f'a = {a} , b = {b} , c = {c} , score is : {multi_test(a, b)}')


def say_hello(user_name):
    print("Hello", user_name)


say_hello("Mr.Johns")
