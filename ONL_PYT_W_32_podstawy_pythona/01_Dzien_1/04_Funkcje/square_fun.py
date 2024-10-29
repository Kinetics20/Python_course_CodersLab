#!/usr/bin/python3

def square(size):
    output = ""
    for row in range(size):
        for column in range(size):
            output += "#"
        output += "\n"
    return output


print(square(5))

