import pygame
import os
from settings import *
from board import board

IMAGE_PATH = os.path.join("..", "assets", "images")

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
    image = pygame.image.load(os.path.join(IMAGE_PATH, piece + ".png"))
    image = pygame.transform.scale(image, (SQUARE_SIZE, SQUARE_SIZE))
    pieces[piece] = image


def draw_pieces(screen):

    for row in range(8):
        for col in range(8):

            piece = board[row][col]

            if piece != "":
                screen.blit(
                    pieces[piece],
                    (col * SQUARE_SIZE, row * SQUARE_SIZE)
                )