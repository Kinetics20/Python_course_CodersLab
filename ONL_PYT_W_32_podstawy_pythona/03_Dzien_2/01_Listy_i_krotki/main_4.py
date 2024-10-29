#!/usr/bin/python3

def suma(numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result += number

    return result


res = suma([1, 2, 3, 4])
print(res)
