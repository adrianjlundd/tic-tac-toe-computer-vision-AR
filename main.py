import cv2
from game.tic_tac_toe import TicTacToe
from tracker.hand_tracker import HandTracker
from gui.board_drawer import draw_board
from gui.ui_helpers import get_cell_from_pos

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
    last_finger_count = 0
    selection_cooldown = 0
    start_cooldown = 150

    print("Press 'q' to quit")

    while True:
        success, img = cap.read()
        if not success:
            print("Couldn't read from camera")
            break

        img = cv2.flip(img, 1)
        
        # Find hand and fingers
        lmList, fingers, img = tracker.find_hand(img)

        # Display fingers list
        if fingers is not None:
            cv2.putText(img, f"Fingers: {fingers}", (img.shape[1] - 300, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        # Cooldown for selection
        if selection_cooldown > 0:
            selection_cooldown -= 1

        # Game state machine
        if game_state == GameState.SELECTING_PLAYERS:
            if start_cooldown > 0:
                start_cooldown -= 1
                cv2.putText(img, f"Starting in: {start_cooldown//30 + 1}s", 
                            (img.shape[1]//2 - 300, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            
            cv2.putText(img, "Select number of players:", (50, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            cv2.putText(img, "1 finger = 1 player (vs AI)", (50, 150),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            cv2.putText(img, "2 fingers = 2 players", (50, 200),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            
            if fingers and selection_cooldown == 0 and start_cooldown == 0:
                num_fingers = sum(fingers)
                if num_fingers in [1, 2] and num_fingers != last_finger_count:
                    num_players = num_fingers
                    game_state = GameState.PLAYING
                    print(f"Selected {num_players} player game")
                    selection_cooldown = 60
                    last_finger_count = num_fingers

        elif game_state == GameState.PLAYING:
            img = draw_board(img, game.board)
            
            if num_players == 1:
                player_text = "Your turn (X)" if game.current_player == 1 else "AI's turn (O)"
            else:
                player_text = "Player 1 (X)" if game.current_player == 1 else "Player 2 (O)"
            
            cv2.putText(img, player_text, (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
            # Handle player moves
            if (game.current_player == 1 or num_players == 2) and lmList and fingers and selection_cooldown == 0:
                hand_palm = lmList[9]
                x, y = hand_palm[0], hand_palm[1]
                cv2.circle(img, (x, y), 10, (255, 0, 0), -1)
                
                if fingers == [1, 1, 1, 1, 1]:
                    row, col = get_cell_from_pos(x, y, img.shape)
                    if row is not None and col is not None and game.board[row, col] == 0 and not game.winner:
                        game.make_move(row, col)
                        selection_cooldown = 30
            
            # AI move
            elif num_players == 1 and game.current_player == 2 and not game.winner and selection_cooldown == 0:
                game.ai_move()
                selection_cooldown = 30
            
            if game.winner is not None:
                game_state = GameState.GAME_OVER
                selection_cooldown = 60

        elif game_state == GameState.GAME_OVER:
            img = draw_board(img, game.board)
            
            if game.winner == 0:
                winner_text = "It's a draw!"
            elif num_players == 1:
                winner_text = "You win!" if game.winner == 1 else "AI wins!"
            else:
                winner_text = f"Player {game.winner} wins!"
            
            cv2.putText(img, winner_text, (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
            cv2.putText(img, "Show 1 finger to play again", (50, 150),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            cv2.putText(img, "Show 2 fingers to quit", (50, 200),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            
            if fingers and selection_cooldown == 0:
                num_fingers = sum(fingers)
                if num_fingers == 1:
                    game.reset()
                    game_state = GameState.SELECTING_PLAYERS
                    num_players = None
                    start_cooldown = 150
                    selection_cooldown = 60
                elif num_fingers == 2:
                    break

        cv2.imshow("Tic Tac Toe Vision", img)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            print("Farvel")
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()