import pygame
from pygame.locals import *

black = [0, 0, 0]
blue = [3, 146, 255]
grey = [133, 214, 251]

def launcher(mySurface):
    """
    Affiche et gère le menu principal
    :param mySurface: Surface pyGame
    :return: Nouveau gamestate
    """

    playing = 1
    clock = pygame.time.Clock()

    FONT_base = pygame.font.Font('freesansbold.ttf', 25)
    FONT_small = pygame.font.Font('freesansbold.ttf', 15)

    image_logo = pygame.image.load('assets/logo.png')

    normalgame_button = pygame.Rect(450, 350, 300, 50)
    normalgame_button.centerx = 450
    normalgame_text = FONT_base.render("2 Players", 1, (0, 0, 0))

    dumbiagame_button = pygame.Rect(450, 410, 300, 50)
    dumbiagame_button.centerx = 450
    dumbiagame_text = FONT_base.render("Player vs Random AI", 1, (0, 0, 0))

    hardiagame_button = pygame.Rect(450, 470, 300, 50)
    hardiagame_button.centerx = 450
    hardiagame_text = FONT_base.render("Player vs Hard AI", 1, (0, 0, 0))

    multiplayergame_button = pygame.Rect(450, 530, 300, 50)
    multiplayergame_button.centerx = 450
    multiplayergame_text = FONT_base.render("Multiplayer", 1, (0, 0, 0))

    loadgame_button = pygame.Rect(300, 590, 145, 50)
    loadgame_text = FONT_base.render("Load", 1, (0, 0, 0))

    quitgame_button = pygame.Rect(455, 590, 145, 50)
    quitgame_text = FONT_base.render("Quit", 1, (0, 0, 0))

    mySurface.fill([179, 205, 224])
    mySurface.blit(image_logo, ((mySurface.get_width() / 2) -300, 20))

    pygame.draw.rect(mySurface, blue, normalgame_button)
    pygame.draw.rect(mySurface, blue, dumbiagame_button)
    pygame.draw.rect(mySurface, grey, hardiagame_button)
    pygame.draw.rect(mySurface, grey, multiplayergame_button)
    pygame.draw.rect(mySurface, grey, loadgame_button)
    pygame.draw.rect(mySurface, blue, quitgame_button)

    mySurface.blit(normalgame_text, (390, 365))
    mySurface.blit(dumbiagame_text, (320, 425))
    mySurface.blit(hardiagame_text, (340, 485))
    mySurface.blit(multiplayergame_text, (380, 545))
    mySurface.blit(loadgame_text, (340, 605))
    mySurface.blit(quitgame_text, (495, 605))

    mySurface.blit(FONT_small.render("Credits: Swann Excoffon & Simon Van Accoleyen", 1, black), (530, 675))

    pygame.display.flip()

    while playing:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return 0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if normalgame_button.collidepoint(event.pos):
                    return 2
                elif dumbiagame_button.collidepoint(event.pos):
                    return 3
                elif hardiagame_button.collidepoint(event.pos):
                    #return 4
                    pass
                elif multiplayergame_button.collidepoint(event.pos):
                    #return 0
                    pass
                elif loadgame_button.collidepoint(event.pos):
                    #return 0
                    pass
                elif quitgame_button.collidepoint(event.pos):
                    return 0

        clock.tick(30)
