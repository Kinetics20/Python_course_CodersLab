#!/usr/bin/python3


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
