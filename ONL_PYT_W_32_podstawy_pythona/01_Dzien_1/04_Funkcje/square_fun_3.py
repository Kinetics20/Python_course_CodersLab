#!/usr/bin/python3

# tu dziala z dwoma petlami:

# def chessboard(n):
#     # line = ('# ' * n)
#     idx = 0
#
#     for _ in range(n):
#         for _ in range(n):
#             if not idx % 2:
#                 print('# ' * (n // 2))
#             else:
#                 print(' #' * (n // 2))
#
#             idx += 1
#
#
# chessboard(8)


def chessboard(n):
    # line = ('# ' * n)
    idx = 0

    for _ in range(n):
        # dummy name (under score ) czyli _ jest zeby byla jakas zmienna
        # ktora nie jest nigdzie wykorzystywana
        # for _ in range(n):
        if not idx % 2:
            print('# ' * (n // 2))
        else:
            print(' #' * (n // 2))
        idx += 1


chessboard(8)