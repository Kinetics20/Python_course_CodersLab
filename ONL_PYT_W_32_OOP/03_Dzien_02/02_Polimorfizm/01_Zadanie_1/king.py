from piece import Piece, only_correct_moves


class King(Piece):


    def list_allowed_moves(self, chessboard):
        return only_correct_moves([
            (self.x + 1, self.y ),
            (self.x - 1, self.y ),
            (self.x , self.y + 1),
            (self.x , self.y - 1),
            (self.x - 1, self.y + 1),
            (self.x - 1, self.y - 1),
            (self.x + 1, self.y + 1),
            (self.x + 1, self.y - 1),
        ])

