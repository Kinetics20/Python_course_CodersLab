#!/usr/bin/python3
# 02

osoba = {
    'imie': 'Jan',
    'nazwisko': 'Kowalski',
    'wiek': 30,
    'miasto': 'Warszawa'
}


def list_keys(d):
    my_list = []
    for key in d:
        my_list.append(key)
    return my_list
    # return d.keys()
    # return d.values()
    # return d.items()


print(list_keys(osoba))


# 02_01 zwraca klucze metoda name_dictionary.keys()

def list_keys(d):
    my_list = []
    for key in d:
        my_list.append(key)
    # return my_list
    return d.keys()
    # return d.values()
    # return d.items()


print(list_keys(osoba))


# 02_02 zwraca wartosci metoda name_dictionary.values()

def list_keys(d):
    my_list = []
    for key in d:
        my_list.append(key)
    # return my_list
    # return d.keys()
    return d.values()
    # return d.items()


# 02_03 zwraca w liscie tuple dwu elementowe
# skladajace sie z klucz i wartosc ze slownika
# metoda name_dictionary.items()

print(list_keys(osoba))


def list_keys(d):
    my_list = []
    for key in d:
        my_list.append(key)
    # return my_list
    # return d.keys()
    # return d.values()
    return d.items()


print(list_keys(osoba))


# 02_04 konwersja metody keys na liste list(name_dict.keys())

def list_keys(d):
    my_list = []
    for key in d:
        my_list.append(key)
    # return my_list
    return list(d.keys())
    # return d.values()
    # return d.items()


print(list_keys(osoba))
