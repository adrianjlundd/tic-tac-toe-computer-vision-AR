import cv2

def draw_board(img, board):
    h, w, _ = img.shape
    size = min(h, w)
    cell = size // 3

    # Make grid lines
    for i in range(1, 3):
        cv2.line(img, (0, i * cell), (size, i * cell), (255, 255, 255), 2)
        cv2.line(img, (i * cell, 0), (i * cell, size), (255, 255, 255), 2)

    #  X and O on board
    for r in range(3):
        for c in range(3):
            x_center = c * cell + cell // 2
            y_center = r * cell + cell // 2
            if board[r, c] == 1:
                cv2.line(img, (x_center - 40, y_center - 40), (x_center + 40, y_center + 40), (0, 255, 0), 3)
                cv2.line(img, (x_center + 40, y_center - 40), (x_center - 40, y_center + 40), (0, 255, 0), 3)
            elif board[r, c] == 2:
                cv2.circle(img, (x_center, y_center), 45, (0, 0, 255), 3)

    return img

#detecting hand position (x,y)
def get_cell_from_pos(x, y, frame_shape):
    
    h, w, _ = frame_shape
    size = min(h, w)
    cell_size = size // 3
    col = int(x / cell_size)
    row = int(y / cell_size)
    if 0 <= row < 3 and 0 <= col < 3:
        return row, col
    return None, None
