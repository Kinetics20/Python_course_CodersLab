#!/usr/bin/python3
from random import choice
from coderslab import coderslab_welcome, words

message = coderslab_welcome()
print(message)


def random_word(words_collection):
    return choice(words_collection)


print(random_word(words))
