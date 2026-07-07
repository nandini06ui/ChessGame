import pygame
import sys

from settings import *
from board import draw_board
from pieces import draw_pieces
from game import select_piece, move_piece, draw_selection
from home import show_home

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
print("Window size:", screen.get_size())
pygame.display.set_caption("Chess King")

clock = pygame.time.Clock()

first_click = True


def run_game():

    global first_click

    running = True

    while running:

        clock.tick(FPS)

        screen.fill((35, 35, 35))

        draw_board(screen)
        draw_selection(screen)
        draw_pieces(screen)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:

                x, y = pygame.mouse.get_pos()

                if (BOARD_X <= x < BOARD_X + BOARD_SIZE and
                    BOARD_Y <= y < BOARD_Y + BOARD_SIZE):

                    col = (x - BOARD_X) // SQUARE_SIZE
                    row = (y - BOARD_Y) // SQUARE_SIZE

                    if first_click:
                        select_piece(row, col)
                        first_click = False
                    else:
                        move_piece(row, col)
                        first_click = True

        pygame.display.flip()


# -------------------------
# MAIN FLOW CONTROLLER
# -------------------------

while True:

    action = show_home(screen)

    if action == "start":
        run_game()

    elif action == "exit":
        pygame.quit()
        sys.exit()