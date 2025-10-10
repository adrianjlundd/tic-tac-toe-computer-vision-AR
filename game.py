import numpy as np

class TicTacToe:
    def __init__(self):
        self.board = np.zeros((3, 3), dtype=int)  # 0 = tom, 1 = X, 2 = O
        self.current_player = 1
        self.winner = None

    def make_move(self, row, col):
        if self.board[row, col] == 0 and not self.winner:
            self.board[row, col] = self.current_player
            if self.check_winner():
                self.winner = self.current_player
            self.current_player = 3 - self.current_player  # change player

    def check_winner(self):
        b = self.board
        for i in range(3):
            if b[i, 0] == b[i, 1] == b[i, 2] != 0: return True
            if b[0, i] == b[1, i] == b[2, i] != 0: return True
        if b[0, 0] == b[1, 1] == b[2, 2] != 0: return True
        if b[0, 2] == b[1, 1] == b[2, 0] != 0: return True
        return False

    def reset(self):
        self.board.fill(0)
        self.current_player = 1
        self.winner = None
