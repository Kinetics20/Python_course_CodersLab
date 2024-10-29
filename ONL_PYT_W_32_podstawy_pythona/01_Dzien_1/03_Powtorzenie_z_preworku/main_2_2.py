#!/usr/bin/python3
from random import randint

num = randint(2, 100)
print(num)


def check_num(i):
    if not i % 2:
        return True
    else:
        return False


print(check_num(num))


def insert_name(name='name', age=None):
    if not age is None:
        print(f'hello , {name} , You are {age} years')
    else:
        print(f'Hello , {name}')


insert_name(name='John', age='49')
insert_name(name='Alice')
