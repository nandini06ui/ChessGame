from board import board

selected_piece = None


def select_piece(row, col):
    global selected_piece

    if board[row][col] != "":
        selected_piece = (row, col)


def move_piece(row, col):
    global selected_piece

    if selected_piece is None:
        return

    old_row, old_col = selected_piece

    board[row][col] = board[old_row][old_col]
    board[old_row][old_col] = ""

    selected_piece = None