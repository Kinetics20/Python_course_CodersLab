from random import randint


def random_average(n):
    my_list = [randint(1, 100) for _ in range(n)]
    return sum(my_list), sum(my_list) / len(my_list)


print(random_average(10))
