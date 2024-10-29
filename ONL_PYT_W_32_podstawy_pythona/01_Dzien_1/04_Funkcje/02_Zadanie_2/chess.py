#!/usr/bin/python3

# def chesssboard(n):
#
#     for digit in range(0, 8):
#         if n % 2 == 0:
#             print(" #" * n)
#         if n % 2 != 0:
#             print("# " * n)

num = int(input("Enter the number : "))
for d in range(1, num):
    if d % 2 == 0:
        print(" #"*num)
    if d % 2 != 0:
        print("# "*num)
