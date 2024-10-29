from random import randint

guessed = False
rnd = randint(1, 10)

while not guessed:
    try:

        str_num = input("Enter number:")
        num = int(str_num)

        if num == rnd:
            print("Great!")
            guessed = True
        else:

            print("Wrong!")
    except ValueError:
        print('it is not int ! try again')
