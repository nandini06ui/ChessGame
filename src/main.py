import pygame
import sys

from settings import WIDTH, HEIGHT, FPS, SQUARE_SIZE
from board import draw_board
from pieces import draw_pieces
from game import select_piece, move_piece, draw_selection
running=True
from home import show_home

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Game")

clock = pygame.time.Clock()
show_home()

running = True
first_click = True

while running:

    clock.tick(FPS)

    draw_board(screen)
    draw_selection(screen)
    draw_pieces(screen)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:

            x, y = pygame.mouse.get_pos()

            col = x // SQUARE_SIZE
            row = y // SQUARE_SIZE

            if first_click:
                select_piece(row, col)
                first_click = False
            else:
                move_piece(row, col)
                first_click = True

    pygame.display.flip()

pygame.quit()
sys.exit()