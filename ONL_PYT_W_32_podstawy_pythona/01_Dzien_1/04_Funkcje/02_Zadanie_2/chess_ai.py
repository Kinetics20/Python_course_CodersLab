#!/usr/bin/python3
def chessboard(n=8):
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

# Przykład użycia z domyślną wartością n=8
szachownica_8x8 = chessboard()
print(szachownica_8x8)
