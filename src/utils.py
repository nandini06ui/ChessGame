def is_valid_pawn_move(piece, old_row, old_col, new_row, new_col, board):

    # White pawn
    if piece == "white_pawn":

        # One step forward
        if new_col == old_col and new_row == old_row - 1:
            return board[new_row][new_col] == ""

        # Two steps from starting position
        if old_row == 6 and new_col == old_col and new_row == 4:
            return (
                board[5][old_col] == ""
                and board[4][old_col] == ""
            )

    # Black pawn
    elif piece == "black_pawn":

        # One step forward
        if new_col == old_col and new_row == old_row + 1:
            return board[new_row][new_col] == ""

        # Two steps from starting position
        if old_row == 1 and new_col == old_col and new_row == 3:
            return (
                board[2][old_col] == ""
                and board[3][old_col] == ""
            )

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