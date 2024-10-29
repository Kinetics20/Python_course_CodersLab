#!/usr/bin/python3

def chessboard(n):
    line = ('# ' * n)[:n]

    for idx, _ in enumerate(range(n)):
        if idx % 2:
            # print(line)
            print((' ' + line)[:n])
        else:
            # print((' ' + line)[:n])
            print(line)


chessboard(8)
