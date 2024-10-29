from random import randint

guessed = False
rnd = randint(1, 10)

while not guessed:
    try:
        str_num = input("Enter number:")
        num = int(str_num)
    except ValueError:
        print('Please use intiger number!')
        continue
    if num == rnd:
        print("Great!")
        guessed = True
    else:
        print("Wrong!")
