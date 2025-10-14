import numpy as np
import random

class TicTacToe:
    def __init__(self):
        self.board = np.zeros((3, 3), dtype=int)  # 0 = empty, 1 = X, 2 = O
        self.current_player = 1
        self.winner = None
        self.difficulty = "random"  # "random" or "minimax"

    def make_move(self, row, col):
        if self.board[row, col] == 0 and not self.winner:
            self.board[row, col] = self.current_player
            if self.check_winner():
                self.winner = self.current_player
            elif self.is_board_full():
                self.winner = 0  # Draw
            else:
                self.current_player = 3 - self.current_player  # change player

    def ai_move(self):
        """AI makes a random move"""
        return self.random_move()
        
    def random_move(self):
        """AI makes a random valid move"""
        empty_cells = [(r, c) for r in range(3) for c in range(3) if self.board[r, c] == 0]
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.make_move(row, col)
            return True
        return False

    def check_winner(self):
        b = self.board
        for i in range(3):
            if b[i, 0] == b[i, 1] == b[i, 2] != 0: return True
            if b[0, i] == b[1, i] == b[2, i] != 0: return True
        if b[0, 0] == b[1, 1] == b[2, 2] != 0: return True
        if b[0, 2] == b[1, 1] == b[2, 0] != 0: return True
        return False

    def is_board_full(self):
        return np.all(self.board != 0)

    def reset(self):
        self.board.fill(0)
        self.current_player = 1
        self.winner = None