def add_reporting(original_function):
    def new_function(a, b):
        print(f'Argumentami są {a} i {b}')
        wynik = original_function(a, b)
        print(f'Wynik to: {wynik}')
        return wynik

    return new_function


@add_reporting
def add(a, b):
    return a + b


@add_reporting
def sub(a, b):
    return a - b


@add_reporting
def mul(a, b):
    return a * b


print(add(5, 7))
print(sub(9, 6))
print(mul(6, 8))
