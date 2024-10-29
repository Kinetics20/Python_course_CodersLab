#!/usr/bin/python3
# 01
from random import randint


def create_list(a, b):
    return [a, b] * 4


# print(create_list(5, 6))
# print(create_list(True, False))


# 2

my_dictionary = {
    'apple': 'a fruit',
    'car': 'a vehicle',
    'python': 'a programming language',
    'sun': 'a star',
    'book': 'a written or printed work',
    'mountain': 'a large landform that rises prominently above its surroundings'
}


def list_keys(d):
    my_list = []
    for _ in d:
        my_list.append(_)
    # return my_list
    # return d.keys()
    # return d.values()
    # return d.items()
    return list(d.keys())


# print(list_keys(my_dictionary))

# 3

word_list = ['python', 'programming', 'language', 'code', 'development', 'list', 'variable']


def find_short_words(words):
    my_list = []
    for word in words:
        if len(word) < 5:
            my_list.append(word)
    # pass
    return my_list


l = find_short_words(word_list)
# print(l)

# 4

number_list = [5, 10, 2.5, -8, 15, 0]


def suma(numbers):
    return sum(numbers)


print(suma(number_list))


def mean(numbers):
    return sum(numbers) / len(numbers)


print(round(mean(number_list), 2))
print(mean(number_list))

import statistics


# print(statistics.mean(number_list))

def mean(numbers):
    return statistics.mean(numbers)


print(mean(number_list))

size = randint(3, 9)


def build_tree(rows, columns):
    for rows in range(1, size + 1):
        for columns in range(rows):
            print('#', end='')
        print()
    return '||'
    # print()


print(build_tree(size, size + 1))


# 4_1
def suma(numbers):
    result = 0
    for number in numbers:
        result += number

    return result


print(suma(number_list))


def suma(numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result += number

    return result


print(suma(number_list))
