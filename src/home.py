import pygame
import sys
import os
from instructions import show_instructions
from settings import WIDTH, HEIGHT

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess King")

image_path = os.path.join("..", "assets", "images", "logo.png")

background = pygame.image.load(image_path)
background = pygame.transform.smoothscale(background, (WIDTH, HEIGHT))


def show_home():

    while True:

        screen.blit(background, (0, 0))
        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                x, y = pygame.mouse.get_pos()

                # START GAME
                if 220 <= x <= 390 and 315 <= y <= 355:
                    return

                # INSTRUCTIONS
                elif 220 <= x <= 390 and 370 <= y <= 410:
                    show_instructions()

                # SETTINGS
                elif 220 <= x <= 390 and 420 <= y <= 460:
                    print("Settings")

                # EXIT
                elif 220 <= x <= 390 and 470 <= y <= 510:
                    pygame.quit()
                    sys.exit()      