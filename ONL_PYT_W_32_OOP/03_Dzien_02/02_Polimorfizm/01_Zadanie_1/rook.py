from piece import Piece


class Rook(Piece):

    def list_allowed_moves(self, chessboard):
        return self._get_horizontal_and_vertical_moves(chessboard)
