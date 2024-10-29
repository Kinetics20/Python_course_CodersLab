#!/usr/bin/python3

num = float(input("Enter dog's age : "))


def dogs_age(age):
    if age <= 2:
        return age * 10.5
    if age > 2:
        return 21 + (age - 2) * 4


print(dogs_age(num))
