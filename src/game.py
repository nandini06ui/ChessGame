import pygame
from board import board
from settings import SQUARE_SIZE
from utils import (
    is_valid_pawn_move,
    is_valid_rook_move,
    is_valid_bishop_move,
    is_valid_knight_move
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

    # Pawn movement
    if piece in ["white_pawn", "black_pawn"]:
        if not is_valid_pawn_move(piece, old_row, old_col, row, col, board):
            selected_piece = None
            selected_row = None
            selected_col = None
            return

    # Rook movement
    if piece in ["white_rook", "black_rook"]:
        if not is_valid_rook_move(old_row, old_col, row, col):
            selected_piece = None
            selected_row = None
            selected_col = None
            return

    # Bishop movement
    if piece in ["white_bishop", "black_bishop"]:
        if not is_valid_bishop_move(old_row, old_col, row, col):
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

    # Move the piece
    board[row][col] = piece
    board[old_row][old_col] = ""

    selected_piece = None
    selected_row = None
    selected_col = None

    # Change turn
    if current_turn == "white":
        current_turn = "black"
    else:
        current_turn = "white"


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