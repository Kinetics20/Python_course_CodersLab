#!/usr/bin/python3

temp = 15
temp_2 = "15"
result = temp * temp_2
print(f"result of multiplication is : {result}")

x = True
print(type(x))

x1 = 42
print(type(x1))

x2 = 4.2
print(type(x2))

x3 = 4j
print(type(x3))

x4 = "Ala ma kota"
print(type(x4))

x5 = {1, 2, 3}
print(type(x5))

x6 = [1, 2, 3]
print(type(x6))

x7 = {"a": 1, "b": 3}
print(type(x7))

x8 = range(10)
print(type(x8))


def check_type(data):
    if type(data) is int:
        return data * 5
    if isinstance(data, float):
        return data / 5
    if type(data) is str:
        return data


print(check_type(5))
print(check_type(5.5))
print(check_type("5"))
