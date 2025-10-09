import cv2
from hand_tracker import HandTracker
from game import TicTacToe
from utils import draw_board

def main():
    cap = cv2.VideoCapture(0)
    tracker = HandTracker()
    game = TicTacToe()

    print("Presss 'q' to quit")

    while True:
        success, img = cap.read()
        if not success:
            print("Couldnt read from camera")
            break

        # Finn hånd og fingre
        lmList, fingers, img = tracker.find_hand(img)

        if fingers:
            cv2.putText(img, f"fingers up: {fingers}", (10, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Tegn Tic Tac Toe-brett
        img = draw_board(img, game.board)

        # Vis bildet
        cv2.imshow("Tic Tac Vision", img)

        # Avslutt ved å trykke q
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            print("quitting")
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
