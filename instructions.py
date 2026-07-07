import pygame
import sys

from settings import WIDTH, HEIGHT

pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (40, 110, 255)
DARK_BG = (20, 35, 65)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Instructions")

# Fonts
title_font = pygame.font.SysFont("Arial", 48, True)
font = pygame.font.SysFont("Arial", 26)

def show_instructions(screen):

    while True:

        screen.fill(DARK_BG)

        # ---------------- Title ----------------
        title = title_font.render("HOW TO PLAY", True, WHITE)
        screen.blit(title, (520, 80))

        # ---------------- Instructions Text ----------------

        lines = [
            "♟ White moves first",
            "♟ Click a piece to select it",
            "♟ Click a square to move",
            "♟ Follow chess rules for each piece",
            "♟ Capture opponent king to win",
            "♟ Game ends when king is captured"
        ]

        y = 200

        for line in lines:
            text = font.render(line, True, WHITE)
            screen.blit(text, (420, y))
            y += 60

        # ---------------- Back Button ----------------

        back_button = pygame.Rect(560, 620, 240, 60)

        pygame.draw.rect(screen, BLUE, back_button, border_radius=12)

        back_text = font.render("BACK", True, WHITE)
        screen.blit(back_text, (back_button.x + 85, back_button.y + 18))

        pygame.display.flip()

        # ---------------- Events ----------------

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:

                if back_button.collidepoint(event.pos):
                    return