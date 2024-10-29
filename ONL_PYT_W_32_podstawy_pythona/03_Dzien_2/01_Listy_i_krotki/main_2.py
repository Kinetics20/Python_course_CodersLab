#!/usr/bin/python3
my_dict= {
    "klucz1": "wartosc1",
    "klucz2": "wartosc2",
    "klucz3": "wartosc3"
}

def list_keys(d):
    # temp = []
    #
    # # domyślny iterator w słowniku jedzie po kluczach
    # for key in d:
    #     temp.append(key)
    #
    # return temp
    return list(d.keys())  # zwraca klucze słownika
    # return d.values()  # zwraca wartości słownika
    # return d.items()  # zwraca tuple 2 elementowe, gdzie pierwszy element tupli to klucz, a drugi to wartość
print(list_keys(my_dict))


