from piece import Piece

class Pawn(Piece):
    def list_allowed_moves(self, chessboard):
        if self.y == 0 or self.y == 7:
            return []

        moves = []
        if self.color == "white":
            if chessboard.is_empty(self.x, self.y+1):
                moves.append(   (self.x, self.y+1)   )
            if self.y == 1:  # to będzie mój pierwszy ruch w grze
                if chessboard.is_empty(self.x, self.y+2):
                    moves.append(   (self.x, self.y+2)   )
            if chessboard.is_enemy(self.x+1, self.y+1, my_color="white"):
                moves.append(   (self.x+1, self.y+1)    )
            if chessboard.is_enemy(self.x-1, self.y+1, my_color="white"):
                moves.append(   (self.x-1, self.y+1)    )

        else:  # color == "black"
            if chessboard.is_empty(self.x, self.y-1):
                moves.append(   (self.x, self.y-1)   )
            if self.y == 6:  # to będzie mój pierwszy ruch w grze
                if chessboard.is_empty(self.x, self.y-2):
                    moves.append(   (self.x, self.y-2)   )
            if chessboard.is_enemy(self.x+1, self.y-1, my_color="black"):
                moves.append(   (self.x+1, self.y-1)    )
            if chessboard.is_enemy(self.x-1, self.y-1, my_color="black"):
                moves.append(   (self.x-1, self.y-1)    )

        return moves