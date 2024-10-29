#!/bin/usr/python3

def safe_get(lista, index):
    try:
        return lista[index]
    except IndexError:
        print('None - bo index nieprawidlowy')
        return None
    except TypeError:
        print('None - bo zly typ index nieprawidlowy')
        return None


print(safe_get(["Hyzio", "Dyzio", "Zyzio"], -3))


def safe_get_2(lista, index):
    if isinstance(index, int):
        if index < len(lista) and index >= -len(lista):
            return lista[index]


print(safe_get_2(["Hyzio", "Dyzio", "Zyzio"], -3))
