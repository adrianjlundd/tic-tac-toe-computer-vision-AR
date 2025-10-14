import numpy as np

def minimax(board, depth, is_maximizing):
    """Minimax algorithm for Tic Tac Toe"""
    # Check for terminal states
    winner = check_winner_board(board)
    if winner == 2:  # AI wins
        return 10 - depth
    elif winner == 1:  # Human wins
        return depth - 10
    elif is_board_full_board(board):  # Draw
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for row in range(3):
            for col in range(3):
                if board[row, col] == 0:
                    board[row, col] = 2  # AI
                    score = minimax(board, depth + 1, False)
                    board[row, col] = 0  # Undo
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row, col] == 0:
                    board[row, col] = 1  # Human
                    score = minimax(board, depth + 1, True)
                    board[row, col] = 0  # Undo
                    best_score = min(score, best_score)
        return best_score

def check_winner_board(board):
    """Check winner for a given board state"""
    for i in range(3):
        if board[i, 0] == board[i, 1] == board[i, 2] != 0: return board[i, 0]
        if board[0, i] == board[1, i] == board[2, i] != 0: return board[0, i]
    if board[0, 0] == board[1, 1] == board[2, 2] != 0: return board[0, 0]
    if board[0, 2] == board[1, 1] == board[2, 0] != 0: return board[0, 2]
    return None

def is_board_full_board(board):
    """Check if board is full for a given board state"""
    return np.all(board != 0)