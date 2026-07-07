def is_valid_pawn_move(piece, old_row, old_col, new_row, new_col, board):

    target = board[new_row][new_col]

    # White pawn
    if piece == "white_pawn":

        # One step forward
        if new_col == old_col and new_row == old_row - 1:
            return target == ""

        # Two steps from starting position
        if old_row == 6 and new_col == old_col and new_row == 4:
            return board[5][old_col] == "" and board[4][old_col] == ""

        # Capture diagonally
        if abs(new_col - old_col) == 1 and new_row == old_row - 1:
            return target.startswith("black")

    # Black pawn
    elif piece == "black_pawn":

        # One step forward
        if new_col == old_col and new_row == old_row + 1:
            return target == ""

        # Two steps from starting position
        if old_row == 1 and new_col == old_col and new_row == 3:
            return board[2][old_col] == "" and board[3][old_col] == ""

        # Capture diagonally
        if abs(new_col - old_col) == 1 and new_row == old_row + 1:
            return target.startswith("white")

    return False
def is_valid_rook_move(old_row, old_col, new_row, new_col):
    # Same row (horizontal move)
    if old_row == new_row:
        return True

    # Same column (vertical move)
    if old_col == new_col:
        return True

    return False
def is_valid_bishop_move(old_row, old_col, new_row, new_col):

    row_difference = abs(new_row - old_row)
    col_difference = abs(new_col - old_col)

    return row_difference == col_difference
def is_valid_knight_move(old_row, old_col, new_row, new_col):

    row_difference = abs(new_row - old_row)
    col_difference = abs(new_col - old_col)

    return (
        (row_difference == 2 and col_difference == 1) or
        (row_difference == 1 and col_difference == 2)
    )
def is_valid_queen_move(old_row, old_col, new_row, new_col):

    # Horizontal move
    if old_row == new_row:
        return True

    # Vertical move
    if old_col == new_col:
        return True

    # Diagonal move
    row_difference = abs(new_row - old_row)
    col_difference = abs(new_col - old_col)

    if row_difference == col_difference:
        return True

    return False
def is_valid_king_move(old_row, old_col, new_row, new_col):

    row_difference = abs(new_row - old_row)
    col_difference = abs(new_col - old_col)

    return row_difference <= 1 and col_difference <= 1
def is_path_clear(old_row, old_col, new_row, new_col, board):

    row_step = 0
    col_step = 0

    if new_row > old_row:
        row_step = 1
    elif new_row < old_row:
        row_step = -1

    if new_col > old_col:
        col_step = 1
    elif new_col < old_col:
        col_step = -1

    current_row = old_row + row_step
    current_col = old_col + col_step

    while (current_row, current_col) != (new_row, new_col):

        if board[current_row][current_col] != "":
            return False

        current_row += row_step
        current_col += col_step

    return True
def is_valid_capture(piece, target_piece):

    # Empty square is always allowed
    if target_piece == "":
        return True

    # White piece cannot capture white piece
    if piece.startswith("white") and target_piece.startswith("white"):
        return False

    # Black piece cannot capture black piece
    if piece.startswith("black") and target_piece.startswith("black"):
        return False

    # Opponent piece can be captured
    return True
def find_king(board, color):

    king = color + "_king"

    for row in range(8):
        for col in range(8):
            if board[row][col] == king:
                return row, col

    return None
def is_in_check(board, color):

    king_position = find_king(board, color)

    if king_position is None:
        return False

    king_row, king_col = king_position

    enemy_color = "black" if color == "white" else "white"

    # Check every enemy piece
    for row in range(8):
        for col in range(8):

            piece = board[row][col]

            if piece.startswith(enemy_color):

                # Queen attack
                if piece.endswith("queen"):
                    if is_valid_queen_move(row, col, king_row, king_col):
                        return True

                # Rook attack
                elif piece.endswith("rook"):
                    if is_valid_rook_move(row, col, king_row, king_col):
                        return True

                # Bishop attack
                elif piece.endswith("bishop"):
                    if is_valid_bishop_move(row, col, king_row, king_col):
                        return True

                # Knight attack
                elif piece.endswith("knight"):
                    if is_valid_knight_move(row, col, king_row, king_col):
                        return True

    return False
def has_any_moves(board, color):

    for row in range(8):
        for col in range(8):

            piece = board[row][col]

            if piece.startswith(color):
                return True

    return False