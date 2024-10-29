#!/usr/bin/python3

def find_short_words(words):
    temp = []
    for word in words:
        if len(word) <5:
            temp.append(word)
    return temp


l = find_short_words(['Litwo', 'ojczyzno', 'moja', 'ty', 'jesteś', 'jak', 'zdrowie'])
print(l)



