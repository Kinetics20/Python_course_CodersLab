#!/usr/bin/python3

print("Equation a*x**2 + b*x + c == 0")
a = float(input("Enter a number : "))
b = float(input("Enter b number : "))
c = float(input("Enter c number : "))
delta = b**2 - 4*a*c
x_1 = (-b - delta**0.5) / (2 * a)
x_2 = (-b + delta**0.5) / (2 * a)
if delta > 0:
    print(f"Roots of the quadratic equation:\nx_1 = {x_1}\nx_2 = {x_2}")
if delta == 0:
    print(f"Roots of the quadratic equation:\nx_1 = x_2 = {x_1}")
if delta < 0:
    print("no solution")
