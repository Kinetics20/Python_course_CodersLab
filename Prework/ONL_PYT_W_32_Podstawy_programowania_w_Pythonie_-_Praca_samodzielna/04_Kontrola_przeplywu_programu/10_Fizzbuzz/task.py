#!/usr/bin/python3

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(f"FizzBuzz")
        continue
    if i % 3 == 0:
        print(f"Fizz")
        continue
    if i % 5 == 0:
        print(f"Buzz")
        continue
    else:
        print(i)
