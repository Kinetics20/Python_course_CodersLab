def divide(a, b):

    try:
        return a / b
    except TypeError:
        return None
    except ZeroDivisionError:
        return None

    # if b == 0:
    #     return None
    # if isinstance(a, str) or isinstance(b, str):
    #     return None
    # else:
    #     return a / b



print(divide(5, 0))
print(divide(5, 2))
print(divide('STH', 2))
print(divide(6, 'Home'))
