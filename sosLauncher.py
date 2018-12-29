import pygame
from pygame.locals import *


def launcher(mySurface):

    playing = 1
    clock = pygame.time.Clock()

    FONT_base = pygame.font.Font('freesansbold.ttf', 25)

    image_logo = pygame.image.load('assets/logo.png')

    launch_button = pygame.Rect(450, 400, 200, 50)
    launch_button.centerx = 450

    launch_button_text = FONT_base.render("Start Game", 1, (0, 0, 0))

    mySurface.fill([179, 205, 224])
    mySurface.blit(image_logo, ((mySurface.get_width() / 2) -300, 20))
    pygame.draw.rect(mySurface, [3, 146, 207], launch_button)
    mySurface.blit(launch_button_text, (380, 410))

    pygame.display.flip()

    while playing:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return 0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if launch_button.collidepoint(event.pos):
                    return 2

        clock.tick(30)
