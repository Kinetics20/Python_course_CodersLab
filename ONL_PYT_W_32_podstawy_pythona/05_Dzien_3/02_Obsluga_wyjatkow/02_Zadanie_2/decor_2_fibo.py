import time


def fibo(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


start = time.time()
print(fibo(10))
print('Working time', time.time() - start, 'second')

from functools import lru_cache


@lru_cache
def fibo_2(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


start = time.time()
print(fibo_2(200))
print('Czas działania:', time.time() - start, 'sekund')

# def fibo(n):
#     if not isinstance(n, int) or n <= 0:
#         return "Enter the natural number."
#
#     fib_numbers = [0, 1]
#
#     for i in range(1, n):
#         fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
#
#     return fib_numbers[n-1]
