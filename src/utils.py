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