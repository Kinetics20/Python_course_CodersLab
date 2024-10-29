def div():
    while True:
        try:
            num_1 = int(input('Enter first number : '))
            num_2 = int(input('Enter first number : '))
            if isinstance(num_1, (int, float)) and isinstance(num_2, (int, float)):
                print(num_1 / num_2)
                break
        except ZeroDivisionError:
            return print('number num_2 is zero , enter number again')
        except ValueError:
            return print('wrong type of data , enter number again')
    return " "
