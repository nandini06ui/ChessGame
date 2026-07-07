import pygame
import os

from settings import WIDTH, HEIGHT

pygame.init()


def show_player_screen(screen):

    image_path = os.path.join("..", "assets", "images", "player_background.png")

    background = pygame.image.load(image_path)
    background = pygame.transform.smoothscale(background, (WIDTH, HEIGHT))

    font = pygame.font.SysFont("timesnewroman", 32)
    error_font = pygame.font.SysFont("arial", 24)

    white_name = ""
    black_name = ""

    active_box = None
    
    white_box = pygame.Rect(485, 330, 640, 65)
    black_box = pygame.Rect(485, 505, 640, 65)
    
 

   

    start_button = pygame.Rect(420, 650, 520, 90)

    back_button = pygame.Rect(35, 35, 70, 70)

    error_message = ""

    while True:

        screen.blit(background, (0, 0))

        white_text = font.render(white_name, True, (255, 255, 255))
        black_text = font.render(black_name, True, (255, 255, 255))

        screen.blit(white_text, (white_box.x + 15, white_box.y + 15))
        screen.blit(black_text, (black_box.x + 15, black_box.y + 15))

        if error_message:
            error_surface = error_font.render(
                error_message,
                True,
                (255, 50, 50)
            )
            screen.blit(error_surface, (500, 620))
            pygame.draw.rect(screen, (255, 0, 0), white_box, 2)
            pygame.draw.rect(screen, (0, 255, 0), black_box, 2)

        pygame.display.flip()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return None, None

            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)

                if white_box.collidepoint(event.pos):
                    active_box = "white"

                elif black_box.collidepoint(event.pos):
                    active_box = "black"

                elif start_button.collidepoint(event.pos):

                    if white_name.strip() == "" or black_name.strip() == "":
                        error_message = "Enter both player names"
                    else:
                        return white_name, black_name

                elif back_button.collidepoint(event.pos):
                    return None, None

                else:
                    active_box = None

            if event.type == pygame.KEYDOWN:

                if active_box == "white":

                    if event.key == pygame.K_BACKSPACE:
                        white_name = white_name[:-1]

                    elif len(white_name) < 15:
                        white_name += event.unicode

                elif active_box == "black":

                    if event.key == pygame.K_BACKSPACE:
                        black_name = black_name[:-1]

                    elif len(black_name) < 15:
                        black_name += event.unicode