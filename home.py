import pygame
import sys
import os

from instructions import show_instructions
from settings import WIDTH, HEIGHT
from player import show_player_screen

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess King")

# Background
image_path = os.path.join("..", "assets", "images", "logo.png")

background = pygame.image.load(image_path)
background = pygame.transform.smoothscale(background, (WIDTH, HEIGHT))

# Buttons
# Buttons (for a 600x600 window)
# Buttons
START_BUTTON = pygame.Rect(520, 400, 350, 60)

INSTRUCTION_BUTTON = pygame.Rect(520, 475, 350, 60)

SETTINGS_BUTTON = pygame.Rect(520, 550, 350, 60)

EXIT_BUTTON = pygame.Rect(520, 625, 350, 60)


def show_home(screen):

    while True:

        screen.blit(background, (0, 0))

        pygame.display.flip()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return "exit"

            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)

                if START_BUTTON.collidepoint(event.pos):
                    player1, player2 = show_player_screen(screen)

                    if player1 is None:
                        continue

                    print("White Player:", player1)
                    print("Black Player:", player2)

                    return "start"

                    

                elif INSTRUCTION_BUTTON.collidepoint(event.pos):

                    show_instructions(screen)

                elif SETTINGS_BUTTON.collidepoint(event.pos):

                    print("Settings Page Coming Soon...")

                elif EXIT_BUTTON.collidepoint(event.pos):

                    return "exit"