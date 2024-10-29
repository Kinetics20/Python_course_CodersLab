#!/usr/bin/python3

size = 3

for row in range(1, size + 1):
    for columns in range(row):
        print("*", end="")
    print()

for row in range(size + 1, 0, -1):
    for columns in range(row):
        print("*", end="")
    print()

# my_str = ""
# for row in range(size + 1, 0, -1):
#     for columns in range(row):
#         my_str += "*"
#     my_str += "\n"
# print(my_str)
