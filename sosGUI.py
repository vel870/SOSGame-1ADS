########################
# 1 ADS - MP 2 - SUPINFO
########################

import pygame
from pygame.locals import *

from sosAlgorithms import *
from sosLauncher import *

WINDOW_width = 900
WINDOW_height = 700

Black = (0, 0, 0)
White = (255, 255, 255)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
Blue0 = (36, 103, 141)
Blue1 = (36, 48, 81)
Blue2 = (194, 204, 231)
Red0 = (206, 25, 25)
Green0 = (49, 175, 73)

def drawBoard(mySurface, n):
    """
    Dessine le plateau initial
    :param mySurface: Surface pyGame
    :param n: Taille du tableau de jeu
    :return: True si succès, False sinon
    """

    FONT_base = pygame.font.Font('freesansbold.ttf', 25)

    mySurface.fill(Blue0)

    GameMenu = pygame.Rect(50, 75, 180, 50)
    NewGame = pygame.Rect(50, 150, 180, 50)
    QuitGame = pygame.Rect(50, 225, 180, 50)
    ScoreS = pygame.Rect(50, 375, 180, 50)
    ScoreO = pygame.Rect(50, 450, 180, 50)

    pygame.draw.rect(mySurface, Blue1, GameMenu)
    button_gamemenu = FONT_base.render("Game Menu", 1, Blue2)
    mySurface.blit(button_gamemenu, (60, 85))

    pygame.draw.rect(mySurface, Blue1, NewGame)
    button_newgame = FONT_base.render("New Game", 1, Blue2)
    mySurface.blit(button_newgame, (65, 162))

    pygame.draw.rect(mySurface, Blue1, QuitGame)
    button_quitgame = FONT_base.render("Quit Game", 1, Blue2)
    mySurface.blit(button_quitgame, (65, 237))

    pygame.draw.rect(mySurface, Blue1, ScoreS)
    label_score_s = FONT_base.render("S Score", 1, Blue2)
    mySurface.blit(label_score_s, (90, 387))

    pygame.draw.rect(mySurface, Blue1, ScoreO)
    label_score_o = FONT_base.render("O Score", 1, Blue2)
    mySurface.blit(label_score_o, (90, 462))

    width = 75
    x, y = 250, 75

    cells = []

    for row in range(0, n):
        for col in range(0, n):

            cell_background = pygame.Rect(x, y, width, width)
            cell_text = FONT_base.render("S/O", 1, Red0)

            pygame.draw.rect(mySurface, White, cell_background)
            mySurface.blit(cell_text, (x + 15, y + 25))

            x = x + width  # Déplacement à droite

            cells.append({
                'x': row,
                'y': col,
                'rect': cell_background
            })

        y = y + width  # Déplacement en bas
        x = 250  # Retour au côté gauche

    pygame.display.flip()

    return {
        'newGame': NewGame,
        'quitGame': QuitGame,
        'mainMenu': GameMenu,
        'cells': cells
    }


def displayScore(mySurface, n, scores):
    """
    Affiche le score des deux joueurs
    :param mySurface: Surface pyGame
    :param n: Taille du tableau de jeu
    :param scores: Tableau des scores
    :return: True si succès, False sinon
    """
    pass


def displayPlayer(mySurface, n, player):
    """
    Affiche au joueur "player" que c'est son tour
    :param mySurface: Surface pyGame
    :param n: Taille du tableau de jeu
    :param player: Joueur en cours
    :return: True si succès, False sinon
    """
    pass


def drawCell(mySurface, board, i, j, player):
    """
    Dessine le contenu de la case (i,j) de la couleur de player
    :param mySurface: Surface pyGame
    :param board: Tableau de jeu
    :param i: Ligne de la case
    :param j: Colonne de la case
    :param player: Joueur en cours
    :return: True si succès, False sinon
    """
    pass


def drawLines(mySurface, lines, player):
    """
    Dessine les nouvelles lignes contenues dans lines de la couleur de player
    :param mySurface: Surface pyGame
    :param lines: Tableau des nouvelles lignes
    :param player: Joueur en cours
    :return: True si succès, False sinon
    """
    pass


def displayWinner(mySurface, n, scores):
    """
    Dessine le résultat de la partie à l'écran
    :param mySurface: Surface pyGame
    :param n: Taille du tableau de jeu
    :param scores: Tableau des scores
    :return: True si succès, False sinon
    """
    pass


def gamePlay(mySurface, board, n, scores):
    """
    Gère une partie SOS Complète
    :param mySurface: Surface pyGame
    :param board: Tableau de jeu
    :param n: Taille du tableau de jeu
    :param scores: Tableau des scores
    :return:
    """
    playing = 1
    player = 0
    clock = pygame.time.Clock()

    rects = drawBoard(mySurface, n)

    while playing:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return 0
            elif event.type == pygame.MOUSEBUTTONDOWN:

                if rects['quitGame'].collidepoint(event.pos):
                    return 0
                elif rects['newGame'].collidepoint(event.pos):
                    print('Not implemented!!') #TODO Implement new game
                elif rects['mainMenu'].collidepoint(event.pos):
                    return 1
                else:

                    for cell in rects['cells']:
                        if cell['rect'].collidepoint(event.pos):

                            i = cell['x']
                            j = cell['y']

                            if board[i][j] == 0:

                                if event.button == 1:
                                    l = 1
                                elif event.button == 3:
                                    l = 2
                                else:
                                    break

                                lines = []

                                board, scores, lines = update(board, n, i, j, l, scores, player, lines)

                                drawCell(mySurface, board, i, j, player)
                                drawLines(mySurface, lines, player)
                                displayScore(mySurface, n, scores)

                                player = togglePlayer(player)

        clock.tick(60)
    return 0


def SOS(n):
    """
    Crée une fenêtre graphique, initialise les structures de données et gère une partie complète.
    :param n: Taille du tableau de jeu
    :return:
    """
    gameState = 1

    board = newBoard(n)
    scores = [0, 0]

    pygame.init()
    pygame.font.init()

    mySurface = pygame.display.set_mode((WINDOW_width, WINDOW_height))
    pygame.display.set_caption('SOS Game')

    while gameState != 0:

        if gameState == 1:
            print('Lancher...')
            gameState = launcher(mySurface)

        elif gameState == 2:
            print('Game...')
            gameState = gamePlay(mySurface, board, n, scores)


SOS(7)