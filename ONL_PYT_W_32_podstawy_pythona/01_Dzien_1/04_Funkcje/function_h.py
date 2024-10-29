#!/usr/bin/python3
# write the function from exercise 1 here
print("Task_01\n")


def square(i):
    return i ** 2


# the lines below will test your function:


print("2 squared is:", square(2))  # should be 4
print("16^2=", square(16))  # should be 256
print("256 to the 2nd power =", square(256))  # should be 65536
print("Task_01_2\n")
a = square(10) + 10
print(a)

print("Task_02\n")


def multiply(subject, times):
    return subject * times


print(multiply(5, 8))
print(multiply(5, "STH"))

print("Task_03\n")


def power(base, exponent=2):
    return base ** exponent


print(power(5))

print("Task_04\n")


def convert_to_usd(euros):
    return euros * 0.82


print(convert_to_usd(100))

print("Task_05\n")


def to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


print(to_celsius(75))

print("Task_06\n")


def calculate_net(gross, vat):
    return gross / (1 + vat / 100)


print(calculate_net(123, 23))

print("Task_06\n")


# num = float(input("Enter the number : "))


# def is_even(i):
#     return False if i % 2 else True

def is_even(i):
    if i % 2 == 0:
        return True
    return False  # jak sie wykona pierwszy return to
    # bedzie koniec dzialania  funkcji , a jak pierwszy nie spelni warunku
    # to nie bedzie to parzysta liczba i przejdzie do drugiego , tam wystarczy
    # ze return zwroci tylko False bo bedzie to napeno liczba nieparzysta


# _second_way_is_even

def is_even_2(i):
    return not i % 2


result = is_even(10)
print(result)
print(is_even_2(10))

print("Task_07\n")


def iterate_through(number):
    for i in range(1, number + 1):
        if is_even(i):
            print(f"Liczba : {i} Liczba jest : {is_even(i)}")
        else:
            print(f"Liczba : {i} Liczba jest : {is_even(i)}")


# second_way

def iterate_through_2(number):
    for i in range(1, number + 1):
        print(f"Number is : {i} is it even ? : {is_even(i)}")


# dla petli While
def iterate_through_3(number):
    counter = 1
    while counter <= number:
        counter += 1
        print(f"Number is : {counter} is it even ? : {is_even(counter)}")
        # print(f"Number is : {counter} is it even ? : ,  {'even' if is_even(counter) else 'Odd'} ")


def iterate_through_4(number):
    counter = 1
    while counter <= number:
        counter += 1
        # print(f"Number is : {counter} is it even ? : {is_even(counter)}")
        print(f"Number is : {counter} is it even ? : ,  {'even' if is_even(counter) else 'Odd'} ")


iterate_through(10)
print("second way\n")
iterate_through_2(10)
print("third way while loop\n")
iterate_through_3(10)
print("third way while loop with ternary operator\n")
iterate_through_4(10)
