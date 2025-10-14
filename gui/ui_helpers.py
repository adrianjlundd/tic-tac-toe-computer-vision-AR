def get_cell_from_pos(x, y, frame_shape):
    h, w, _ = frame_shape
    size = min(h, w)
    cell_size = size // 3
    col = int(x / cell_size)
    row = int(y / cell_size)
    if 0 <= row < 3 and 0 <= col < 3:
        return row, col
    return None, None