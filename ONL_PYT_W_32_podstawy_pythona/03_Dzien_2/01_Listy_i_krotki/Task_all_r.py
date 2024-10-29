#!/usr/bin/python3
# 01
import statistics


def create_list(i, j):
    return [i, j] * 4


print(create_list(1, 2))
print(create_list(True, False))

# 02

couples_dict = {
    'Alice': 28,
    'Bob': 30,
    'Charlie': 25,
    'Diana': 22,
    'Eve': 35,
    'Frank': 32
}


def list_keys(d):
    temp = []
    for key in d:
        temp.append(key)
    # return temp
    return list(d.keys())
    # return d.values()
    # return d.items()


print(list_keys(couples_dict))

# 03

word_list = ['cat', 'banana', 'carrot', 'dog', 'elephant']


def find_short_words(words):
    temp = []
    for word in words:
        if len(word) < 5:
            temp.append(word)

    return temp


l = find_short_words(word_list)
print(l)

# 04

a_list = [1, 2, 3, 4, 5]


def suma(numbers):
    result = 0
    for number in numbers:
        result += number

    return result


print(suma(a_list))


# 05
def suma_2(numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result += number

    return result


print(suma_2(a_list))


# 06
def mean(numbers):
    return statistics.mean(numbers)


print(mean(a_list))


# 07
def mean_2(numbers):
    return sum(numbers) / len(numbers)


print(mean_2(a_list))

size = 5

# 08

for row in range(1, size + 1):
    for columns in range(row):
        print("*", end="")
    print()

for row in range(1, size + 1)[::-1]:
    for columns in range(row):
        print("*", end="")
    print()


# 09

def check_odd(number):
    return 'Odd' if number % 2 else 'Even'


print(check_odd(2))

# 10

mixed_list = [42, 3.14, "hello", 7, 2.718, "world", 10]


def check_val_list(items):
    new_list = []
    new_list_str = []
    new_list_int = []
    for item in items:
        if isinstance(item, float):
            new_list.append(item)
        if isinstance(item, str):
            new_list_str.append(item)
        else:
            new_list_int.append(item)
    return new_list, new_list_str, new_list_int


print(check_val_list(mixed_list))

# 11

mixed_list_2 = [42, 3.14, "hello", True, [1, 2, 3], {'key': 'value'}, None, (4, 5), 'world', False]


def create_list_last_3_index(items):
    new_list = []
    for item in items[:-4:-1]:
        new_list.append(item)
    return new_list


print(f'The new list made up of last three indexes of mixed list :\n{create_list_last_3_index(mixed_list_2)}')
