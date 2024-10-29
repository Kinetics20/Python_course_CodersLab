def phone(number):
    number = str(number)
    sum_of_digits = 0
    for digit in number:
        try:
            sum_of_digits += int(digit)
        except ValueError:
            raise Exception('Numer jest niepoprawny')
    if sum_of_digits == 50:
        return number
    else:
        raise Exception('Nie ma takiego numeru')

print(phone("5544444123482"))
print(phone(999995))
print(phone(111122223333))
print(phone("5544444123482"))
