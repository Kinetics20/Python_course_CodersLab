class Piece:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x = x
        self.y = y

    def _get_diagonal_moves(self, chessboard):
        moves = []
        for i in range(1, 8):
            moves.append(     (self.x+i, self.y+i)     )
            if chessboard.is_enemy(self.x+i, self.y+i, my_color=self.color):
                break
        for i in range(1, 8):
            moves.append(     (self.x-i, self.y+i)     )
            if chessboard.is_enemy(self.x-i, self.y+i, my_color=self.color):
                break
        for i in range(1, 8):
            moves.append(     (self.x-i, self.y-i)     )
            if chessboard.is_enemy(self.x-i, self.y-i, my_color=self.color):
                break
        for i in range(1, 8):
            moves.append(     (self.x+i, self.y-i)     )
            if chessboard.is_enemy(self.x+i, self.y-i, my_color=self.color):
                break
        return only_correct_moves(moves)

    def _get_horizontal_and_vertical_moves(self, chessboard):
        moves = []
        for y in range(self.y + 1, 8):
            moves.append((self.x, y))
            if chessboard.is_enemy(self.x, y, my_color=self.color):
                break

        for x in range(self.x + 1, 8):
            moves.append((x, self.y))
            if chessboard.is_enemy(x, self.y, my_color=self.color):
                break

        for x in range(self.x - 1, -1, -1):
            moves.append((x, self.y))
            if chessboard.is_enemy(x, self.y, my_color=self.color):
                break

        for y in range(self.y - 1, -1, -1):
            moves.append((self.x, y))
            if chessboard.is_enemy(self.x, y, my_color=self.color):
                break

        return moves


def only_correct_moves(all_moves):  # all_moves = [ (4, 6),  (7, 9), ... ]
    correct_moves = []
    for move in all_moves:
        # `move` to tupla intów, np. (4, 6)
        # więc `move[0]` to 4
        # a `move[1]` to 6
        if 0 <= move[0] <= 7 and 0 <= move[1] <= 7:
            correct_moves.append(move)
    return correct_moves
