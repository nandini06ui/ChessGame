import pygame
from board import board
from settings import SQUARE_SIZE
from utils import (
    is_valid_pawn_move,
    is_valid_rook_move,
    is_valid_bishop_move,
    is_valid_knight_move,
    is_valid_queen_move,
    is_valid_king_move,
    is_path_clear,
    is_valid_capture,
    find_king,
    is_in_check,
    has_any_moves
)

selected_piece = None
selected_row = None
selected_col = None

# White moves first
current_turn = "white"


def select_piece(row, col):
    global selected_piece, selected_row, selected_col

    piece = board[row][col]

    if piece == "":
        return

    if current_turn == "white" and piece.startswith("white"):
        selected_piece = (row, col)
        selected_row = row
        selected_col = col

    elif current_turn == "black" and piece.startswith("black"):
        selected_piece = (row, col)
        selected_row = row
        selected_col = col


def move_piece(row, col):
    global selected_piece
    global selected_row
    global selected_col
    global current_turn

    if selected_piece is None:
        return

    old_row, old_col = selected_piece
    piece = board[old_row][old_col]
    target_piece = board[row][col]
 # Check if a king is captured
    if target_piece == "white_king":
        print("🏆 Black Wins!")
        pygame.quit()
        exit()

    if target_piece == "black_king":
        print("🏆 White Wins!")
        pygame.quit()
        exit()   

# Prevent capturing your own pieces
    if not is_valid_capture(piece, target_piece):
        selected_piece = None
        selected_row = None
        selected_col = None
        return

    # Pawn movement
    if piece in ["white_pawn", "black_pawn"]:
        if not is_valid_pawn_move(piece, old_row, old_col, row, col, board):
            selected_piece = None
            selected_row = None
            selected_col = None
            return

    # Rook movement
    if piece in ["white_rook", "black_rook"]:
        if (
            not is_valid_rook_move(old_row, old_col, row, col)
            or not is_path_clear(old_row, old_col, row, col, board)
        ):
            selected_piece = None
            selected_row = None
            selected_col = None
            return

    # Bishop movement
    # Bishop movement
    if piece in ["white_bishop", "black_bishop"]:
        if (
            not is_valid_bishop_move(old_row, old_col, row, col)
            or not is_path_clear(old_row, old_col, row, col, board)
        ):
            selected_piece = None
            selected_row = None
            selected_col = None
            return
        # Knight movement
    if piece in ["white_knight", "black_knight"]:
        if not is_valid_knight_move(old_row, old_col, row, col):
            selected_piece = None
            selected_row = None
            selected_col = None
            return
  # Queen movement
    if piece in ["white_queen", "black_queen"]:
        if (
            not is_valid_queen_move(old_row, old_col, row, col)
            or not is_path_clear(old_row, old_col, row, col, board)
        ):
            selected_piece = None
            selected_row = None
            selected_col = None
            return
# King movement
    if piece in ["white_king", "black_king"]:
        if not is_valid_king_move(old_row, old_col, row, col):
            selected_piece = None
            selected_row = None
            selected_col = None
            return

    # Move the piece
    board[row][col] = piece
    board[old_row][old_col] = ""
    # Pawn Promotion

    if piece == "white_pawn" and row == 0:
        board[row][col] = "white_queen"

    elif piece == "black_pawn" and row == 7:
        board[row][col] = "black_queen"

    selected_piece = None
    selected_row = None
    selected_col = None

    # Change turn
    if current_turn == "white":
        current_turn = "black"
    else:
        current_turn = "white"
        
   
        print("White has pieces:", has_any_moves(board, "white"))
        print("Black has pieces:", has_any_moves(board, "black"))


def draw_selection(screen):
    if selected_row is not None:
        pygame.draw.rect(
            screen,
            (0, 255, 0),
            (
                selected_col * SQUARE_SIZE,
                selected_row * SQUARE_SIZE,
                SQUARE_SIZE,
                SQUARE_SIZE,
            ),
            4,
        )