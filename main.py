import cv2
from hand_tracker import HandTracker
from game import TicTacToe
from utils import draw_board, get_cell_from_pos
import numpy as np

class GameState:
    SELECTING_PLAYERS = 0
    PLAYING = 1
    GAME_OVER = 2

def main():
    cap = cv2.VideoCapture(0)
    tracker = HandTracker()
    game = TicTacToe()
    
    game_state = GameState.SELECTING_PLAYERS
    num_players = None

    print("Press 'q' to quit")

    while True:
        success, img = cap.read()
        if not success:
            print("Couldn't read from camera")
            break

        # Flip image horizontally for more intuitive interaction
        img = cv2.flip(img, 1)
        
        # Find hand and fingers
        lmList, fingers, img = tracker.find_hand(img)

        # Display fingers count
        if fingers:
            num_fingers = sum(fingers)
            cv2.putText(img, f"Fingers: {num_fingers}", (10, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Game state machine
        if game_state == GameState.SELECTING_PLAYERS:
            # Draw player selection screen
            cv2.putText(img, "Select number of players:", (50, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            cv2.putText(img, "1 finger = 1 player", (50, 150),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            cv2.putText(img, "2 fingers = 2 players", (50, 200),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            
            # Check for player selection
            if fingers and sum(fingers) in [1, 2]:
                num_players = sum(fingers)
                game_state = GameState.PLAYING
                print(f"Selected {num_players} player game")
                # Small delay to avoid multiple detections
                cv2.waitKey(500)

        elif game_state == GameState.PLAYING:
            # Draw the game board
            img = draw_board(img, game.board)
            
            # Display current player
            player_text = "X's turn" if game.current_player == 1 else "O's turn"
            cv2.putText(img, player_text, (10, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
            # Handle player moves (for now, just basic detection)
            if lmList and fingers:
                # Get index finger tip position (landmark 8)
                index_finger_tip = lmList[8]
                x, y = index_finger_tip[0], index_finger_tip[1]
                
                # Draw cursor
                cv2.circle(img, (x, y), 10, (255, 0, 0), -1)
                
                # Check if finger is pointing (index finger up, others down)
                if fingers == [0, 1, 0, 0, 0]:  # Only index finger up
                    row, col = get_cell_from_pos(x, y, img.shape)
                    if row is not None and col is not None:
                        # Make move if cell is empty
                        if game.board[row, col] == 0 and not game.winner:
                            game.make_move(row, col)
                            # Small delay to avoid multiple moves
                            cv2.waitKey(300)
            
            # Check for game over
            if game.winner:
                game_state = GameState.GAME_OVER
            elif np.all(game.board != 0):  # Board is full (draw)
                game_state = GameState.GAME_OVER

        elif game_state == GameState.GAME_OVER:
            # Draw game over screen
            img = draw_board(img, game.board)
            
            if game.winner:
                winner_text = f"Player {game.winner} wins!"
            else:
                winner_text = "It's a draw!"
            
            cv2.putText(img, winner_text, (50, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
            cv2.putText(img, "Show 1 finger to play again", (50, 150),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            cv2.putText(img, "Show 2 fingers to quit", (50, 200),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            
            # Check for restart or quit
            if fingers and sum(fingers) == 1:
                game.reset()
                game_state = GameState.SELECTING_PLAYERS
                num_players = None
                cv2.waitKey(500)
            elif fingers and sum(fingers) == 2:
                break

        # Display current game state
        state_text = f"State: {['Selecting', 'Playing', 'Game Over'][game_state]}"
        cv2.putText(img, state_text, (10, img.shape[0] - 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

        # Show image
        cv2.imshow("Tic Tac Toe Vision", img)

        # Quit with 'q' key
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            print("Quitting")
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()