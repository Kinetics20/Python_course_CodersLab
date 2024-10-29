#!/usr/bin/python3
# 03

word_list = ['python', 'programming', 'language', 'code', 'development', 'list', 'variable']


def find_short_words(words):
    my_list = []
    for word in words:
        if len(word) < 5:
            my_list.append(word)
    return my_list


l = find_short_words(word_list)
print(l)
