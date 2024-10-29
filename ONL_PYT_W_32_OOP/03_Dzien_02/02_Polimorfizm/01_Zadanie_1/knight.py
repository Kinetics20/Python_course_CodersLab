from piece import Piece, only_correct_moves




class Knight(Piece):


    def list_allowed_moves(self, chessboard):
        return only_correct_moves([
            (self.x + 1, self.y + 2),
            (self.x + 2, self.y + 1),
            (self.x - 1, self.y + 2),
            (self.x - 2, self.y + 1),
            (self.x + 1, self.y - 2),
            (self.x + 2, self.y - 1),
            (self.x - 1, self.y - 2),
            (self.x - 2, self.y - 1),
        ])
