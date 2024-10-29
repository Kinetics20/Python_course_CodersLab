from piece import Piece
class Bishop(Piece):

    def list_allowed_moves(self, chessboard):
        return self._get_diagonal_moves(chessboard)
