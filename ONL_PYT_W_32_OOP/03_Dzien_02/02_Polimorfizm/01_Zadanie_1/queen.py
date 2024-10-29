from piece import Piece


class Queen(Piece):

    def list_allowed_moves(self, chessboard):
        return self._get_horizontal_and_vertical_moves(chessboard) + self._get_diagonal_moves(chessboard)