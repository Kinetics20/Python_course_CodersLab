#!/usr/bin/python3

num = float(input("Enter the number : "))


def is_divisible_by_4(g):
    if g % 4 == 0:
        return True
    if g % 4 != 0:
        return False


print(f"{is_divisible_by_4(num)}")
