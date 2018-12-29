########################
# 1 ADS - MP 2 - SUPINFO
########################

import pygame
from pygame.locals import *

from sosAlgorithms import *
from sosLauncher import *

WINDOW_width = 900
WINDOW_height = 700

COLOR_black = [0, 0, 0]
COLOR_white = [255, 255, 255]
COLOR_blue = [3, 146, 207]
COLOR_red = [251, 46, 1]

def drawBoard(mySurface, n):
    """
    Dessine le plateau initial
    :param mySurface: Surface pyGame
    :param n: Taille du tableau de jeu
    :return: True si succès, False sinon
    """

    FONT_base = pygame.font.Font('freesansbold.ttf', 25)

    mySurface.fill(COLOR_blue)

    #pygame.draw.rect(mySurface, COLOR_blue, GameMenu)
    button_gamemenu = FONT_base.render("Game Menu", 1, COLOR_blue)
    mySurface.blit(button_gamemenu, (60, 85))

    #pygame.draw.rect(mySurface, COLOR_blue, NewGame)
    button_newgame = FONT_base.render("New Game", 1, COLOR_blue)
    mySurface.blit(button_newgame, (65, 162))

    #pygame.draw.rect(mySurface, COLOR_blue, QuitGame)
    button_quitgame = FONT_base.render("Quit Game", 1, COLOR_blue)
    mySurface.blit(button_quitgame, (65, 237))

    #pygame.draw.rect(mySurface, COLOR_blue, ScoreS)
    label_score_s = FONT_base.render("S Score", 1, COLOR_red)
    mySurface.blit(label_score_s, (90, 387))

    #pygame.draw.rect(mySurface, COLOR_blue, ScoreO)
    label_score_o = FONT_base.render("O Score", 1, COLOR_red)
    mySurface.blit(label_score_o, (90, 462))

    width = 75
    x, y = 250, 75

    for row in range(0, n):
        for col in range(0, n):

            case_background = pygame.Rect(x, y, width, width)
            case_text = FONT_base.render("S/O", 1, COLOR_red)

            pygame.draw.rect(mySurface, COLOR_white, case_background)
            mySurface.blit(case_text, (x + 15, y + 25))

            x = x + width  # Déplacement à droite

        y = y + width  # Déplacement en bas
        x = 250  # Retour au côté gauche

    pygame.display.flip()
    return True


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


def selectSquare(mySurface, board, n):
    """
    Fait choisir une case et une lettre au joueur
    :param mySurface: Surface pyGame
    :param board: Tableau de jeu
    :param n: Taille du tableau de jeu
    :return: (i, j, l)
    """
    return 0, 0, 0


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

    drawBoard(mySurface, n)
    """
    i, j, l = selectSquare(mySurface, board, n)
    lines = []

    drawCell(mySurface, board, i, j, player)
    board, scores, lines = update(board, n, i, j, l, scores, player, lines)
    drawLines(mySurface, lines, player)
    displayScore(mySurface, n, scores)
    """

    while playing:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return 0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass

        clock.tick(30)


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