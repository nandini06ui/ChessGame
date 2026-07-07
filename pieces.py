import pygame
import os

from settings import *
from board import board

# -----------------------------
# Image Path
# -----------------------------

IMAGE_PATH = os.path.join("..", "assets", "images")

# -----------------------------
# Load Pieces
# -----------------------------

pieces = {}

piece_names = [
    "white_pawn",
    "white_rook",
    "white_knight",
    "white_bishop",
    "white_queen",
    "white_king",
    "black_pawn",
    "black_rook",
    "black_knight",
    "black_bishop",
    "black_queen",
    "black_king"
]

for piece in piece_names:

    image = pygame.image.load(
        os.path.join(IMAGE_PATH, piece + ".png")
    )

    image = pygame.transform.smoothscale(
        image,
        (SQUARE_SIZE, SQUARE_SIZE)
    )

    pieces[piece] = image


# -----------------------------
# Draw Pieces
# -----------------------------

def draw_pieces(screen):

    for row in range(ROWS):

        for col in range(COLS):

            piece = board[row][col]

            if piece != "":

                screen.blit(
                    pieces[piece],
                    (
                        BOARD_X + col * SQUARE_SIZE,
                        BOARD_Y + row * SQUARE_SIZE
                    )
                )