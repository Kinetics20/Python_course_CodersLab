#!/usr/bin/python3
# pierwsze cwiczenie

def create_list(a, b):
    return [a, b] * 4

print(create_list(1, 2))
print(create_list(True, False))

# drugie cwiczenie

moj_slownik = {
    "klucz1": "wartosc1",
    "klucz2": "wartosc2",
    "klucz3": "wartosc3"
}
def list_keys(d):
    temp = []
    # domyslny iterrator w slowniku jedzie po kluczach
    for key in d:
        temp.append(key)
    return temp
    # return list(d.keys()) - zwraca liste wypelniona kluczami
    # return d.keys() - zwraca wszystkie klucze
    # return d.values() - zwraca wszystkie
    # return d.items() - zraca wszystkie wartosci

print(list_keys(moj_slownik))


