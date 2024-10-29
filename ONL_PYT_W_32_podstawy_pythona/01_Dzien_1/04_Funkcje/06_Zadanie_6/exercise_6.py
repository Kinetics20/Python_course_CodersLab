def calculate_net(gross, vat):
    return gross / (1 + vat)

print(calculate_net(100, 0.5))

def is_even(number):
    if number %2 == 0:
        return True
    return False

def is_event_2(number):
    # return not number % 2
    return number % 2 == 0

result = is_even(42)
# print(result)
# print(is_even(42))

def iterate_through(number):
    for digit in range(1, number + 1):
        print('Liczba: ', digit, ' Czy jest parzysta?', is_even(digit))
    counter = 1

    # while counter <= number:
    #     # print('Liczba: ', counter, ' Czy jest parzysta?', 'parzysta' if is_even(counter) else 'nieparzysta')
    #     print('Liczba: ', counter, ' Czy jest parzysta?', is_even(counter))
    #     counter += 1


iterate_through(42)