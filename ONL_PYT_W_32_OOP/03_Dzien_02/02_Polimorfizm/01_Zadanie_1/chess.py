from pawn import Pawn
from knight import Knight
from king import King
from rook import Rook
from bishop import Bishop
from queen import Queen


def show(chessboard):
    """Shows the chessboard in the console.
    DOES NOT WORK UNTIL ALL CLASES: Pawn, Knight, Queen, King, Rook, Bishop ARE CREATED!!!
    """
    WHITE = {
        Pawn: chr(9817),
        Knight: chr(9816),
        Queen: chr(9813),
        King: chr(9812),
        Rook: chr(9814),
        Bishop: chr(9815),
    }
    BLACK = {
        Pawn: chr(9823),
        Knight: chr(9818),
        Queen: chr(9819),
        King: chr(9812),
        Rook: chr(9820),
        Bishop: chr(9821),
    }
    for y in range(7, -1, -1):
        print(y, end='\t')
        for x in range(8):
            if chessboard.board[x][y] is not None:
                if chessboard.board[x][y].color == 'white':
                    print(WHITE[type(chessboard.board[x][y])], end='\t')
                else:
                    print(BLACK[type(chessboard.board[x][y])], end='\t')
            else:
                print('\t', end='')
        print('\n')
    print('\t', end='')
    for x in range(8):
        print(x, end='\t')
    print()


class Chessboard:
    def __init__(self):
        self.color = "white"
        self.board = [
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
        ]

    def setup(self):
        for x in range(8):  # 0, 1 ... 6, 7
            self.board[x][1] = Pawn("white", x, 1)
            self.board[x][6] = Pawn("black", x, 6)
        self.board[0][0] = Rook("white", 0, 0)
        self.board[1][0] = Knight("white", 1, 0)
        self.board[2][0] = Bishop("white", 2, 0)
        self.board[3][0] = Queen("white", 3, 0)
        self.board[4][0] = King("white", 4, 0)
        self.board[5][0] = Bishop("white", 5, 0)
        self.board[6][0] = Knight("white", 6, 0)
        self.board[7][0] = Rook("white", 7, 0)

        self.board[0][7] = Rook("black", 0, 7)
        self.board[1][7] = Knight("black", 1, 7)
        self.board[2][7] = Bishop("black", 2, 7)
        self.board[3][7] = Queen("black", 3, 7)
        self.board[4][7] = King("black", 4, 7)
        self.board[5][7] = Bishop("black", 5, 7)
        self.board[6][7] = Knight("black", 6, 7)
        self.board[7][7] = Rook("black", 7, 7)

    def list_allowed_moves(self, x, y):
        if self.board[x][y] is None:
            return None
        if self.board[x][y].color != self.color:
            return None
        return self.board[x][y].list_allowed_moves(self)

    def move(self, from_x, from_y, to_x, to_y):
        allowed_moves = self.list_allowed_moves(from_x, from_y)
        if allowed_moves is None:  # pole (from_x, from_y) jest puste albo pionek ma zły kolor
            raise ValueError("Niedozwolony ruch")
        else:  # jakieś ruchy z tego pola są dostępne
            desired_move = (to_x, to_y)
            if desired_move in allowed_moves:

                # pionek który nas interesuje
                piece = self.board[from_x][from_y]

                # ściągamy go z planszy - jego pole jest teraz puste
                self.board[from_x][from_y] = None

                # informujemy pionek, gdzie będzie zaraz stał
                piece.move(to_x, to_y)

                # i kładziemy go na tym polu
                self.board[to_x][to_y] = piece

                if self.color == "white":
                    self.color = "black"
                else:  # color == "black"
                    self.color = "white"
            else:
                raise ValueError("Niedozwolony ruch")

    def is_enemy(self, x, y, my_color):
        if x < 0 or x > 7 or y < 0 or y > 7:
            return False  # nie ma takiego pola - i na pewno nie ma tam wroga!
        if self.board[x][y] is None:
            return False  # jest puste pole - nie ma wroga
        if self.board[x][y].color != my_color:
            return True  # jest pionek, i jest innego koloru niż mój - wróg!
        else:
            return False  # jest pionek, ale ma taki sam kolor - przyjaciel
    def is_empty(self, x, y):
        if x < 0 or x > 7 or y < 0 or y > 7:
            return False
        if self.board[x][y] is None:
            return True
        else:
            return False
