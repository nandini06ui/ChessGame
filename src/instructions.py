import pygame
import sys

from settings import WIDTH, HEIGHT

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Instructions")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (40, 110, 255)

title_font = pygame.font.SysFont("Arial", 40, True)
text_font = pygame.font.SysFont("Arial", 24)

back_button = pygame.Rect(20, 20, 100, 40)


def show_instructions():

    running = True

    while running:

        screen.fill((230, 230, 230))

        title = title_font.render("Chess Instructions", True, BLACK)
        screen.blit(title, (150, 40))

        instructions = [
            "1. White moves first.",
            "2. Click a piece to select it.",
            "3. Click another square to move.",
            "4. Capture opponent pieces.",
            "5. Protect your king.",
            "6. Have fun!"
        ]

        y = 120

        for line in instructions:
            text = text_font.render(line, True, BLACK)
            screen.blit(text, (60, y))
            y += 40

        pygame.draw.rect(screen, BLUE, back_button, border_radius=8)
        back = text_font.render("Back", True, WHITE)
        screen.blit(back, (45, 28))

        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if back_button.collidepoint(event.pos):
                    running = False