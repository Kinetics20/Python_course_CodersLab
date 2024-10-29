#!/usr/bin/python3
from random import randint

# dog's age

dogs_age = randint(1, 15)


def dogs_age_(i):
    if i < 2:
        return i * 10.5
    return 21 + (i - 3) * 4


print(dogs_age, dogs_age_(dogs_age))
# 01

input_dict = {
    "name": "Han Solo",
    "role": "smuggler",
    "movie": "Star Wars"
}

input_dict_2 = {
    "name": "Bilbo Baggins",
    "role": "burglar"
}


def message(actor):
    if 'movie' not in actor or 'role' not in actor or 'name' not in actor:
        return None
    return f'In movie {actor["movie"]}, {actor["name"]} is a {actor["role"]}.'


print(message(input_dict))
print(message(input_dict_2))


def generate_list(actor):
    new_list = []
    for item in actor.values():
        new_list.append(item)
    return new_list


print(generate_list(input_dict))
