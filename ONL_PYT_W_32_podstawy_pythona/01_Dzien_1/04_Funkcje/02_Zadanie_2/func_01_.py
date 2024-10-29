#!/usr/bin/python3

a = "What should I have to do "
y = list(a)
b = set(y)
n = 1
z = range(n)


# print(a, type(a))
# print(y, type(y))
# print(b, type(b))
# print(n, type(n))
# print(z, type(z))

def my_range_2(start, stop=None,step=1):
    if stop is None:
        stop = start
        start = 0

    temp = []
    item = start

    while len(temp) < (stop - start) // step:
        temp.append(item)
        item += step

    return temp


print(my_range_2(6))
print(my_range_2(2, 10))
print(my_range_2(2, 10, 2))
print(my_range_2(10, 2, -2))

