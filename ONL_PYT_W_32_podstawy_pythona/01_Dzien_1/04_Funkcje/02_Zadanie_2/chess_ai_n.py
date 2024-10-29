#!/usr/bin/python3
num = int(input("Enter numbers of chessboar's rows : "))
def chessboard(n):
    szachownica = ""
    for i in range(n):
        for j in range(n):
            # Jeśli suma indeksów jest parzysta, to wstawiamy '#', w przeciwnym razie spacje.
            if (i + j) % 2 == 0:
                szachownica += "#"
            else:
                szachownica += " "
        szachownica += "\n"  # Dodaj nową linię na koniec każdego wiersza
    return szachownica
print(chessboard(num))
