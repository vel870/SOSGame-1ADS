########################
# 1 ADS - MP 2 - SUPINFO
########################


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
    :param i:
    :param j:
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
    pass


def gamePlay(mySurface, board, n, scores):
    """
    Gère une partie SOS Complète
    :param mySurface: Surface pyGame
    :param board: Tableau de jeu
    :param n: Taille du tableau de jeu
    :param scores:
    :return:
    """
    pass


def SOS(n):
    """
    Crée une fenêtre graphique, initialise les structures de données et gère une partie complète.
    :param n: Taille du tableau de jeu
    :return:
    """
    pass
