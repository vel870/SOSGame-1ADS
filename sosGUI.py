########################
# 1 ADS - MP 2 - SUPINFO
########################

import pygame
from pygame.locals import *
from sosAlgorithms import *


WINDOW_width = 900
WINDOW_height = 600

COLOR_black = (0, 0, 0)
COLOR_white = (255, 255, 255)


def drawBoard(mySurface, n):
    """
    Dessine le plateau initial
    :param mySurface: Surface pyGame
    :param n: Taille du tableau de jeu
    :return: True si succès, False sinon
    """
    pass


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