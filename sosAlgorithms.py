########################
# 1 ADS - MP 2 - SUPINFO
########################


def newBoard(n):
    """
    Retourne une liste à deux dimension représentant l'état initial du plateau
    :param n: Nombre de lignes et de colonnes du tableau de jeu
    :return: Tableau de jeu
    """
    pass


def possibleSquare(board, n, i, j):
    """
    Retourne True si (i, j) sont les coordonnées d'une case où un joueur peut poser une lettre
    :param board: Tableau de jeu
    :param n: Taille du tableau de jeu
    :param i:
    :param j:
    :return: True | False
    """
    pass


def updateScoreS(board, n, i, j, scores, player, lines):
    """
    Appelée après que le joueur a posé un S, cherche les alignements créés et met à jour le score
    du joueur et la variable lines
    :param board: Tableau de jeu
    :param n: Taille du tableau de jeu
    :param i:
    :param j:
    :param scores: Tableau des scores
    :param player: Joueur en cours
    :param lines: Tableau des nouvelles lignes
    :return: (scores, lines)
    """
    pass


def updateScoreO(board, n, i, j, scores, player, lines):
    """
    Appelée après que le joueur a posé un O, cherche les alignements créés et met à jour le score
    du joueur et la variable lines
    :param board: Tableau de jeu
    :param n: Taille du tableau de jeu
    :param i:
    :param j:
    :param scores: Tableau des scores
    :param player: Joueur en cours
    :param lines: Tableau des nouvelles lignes
    :return: (scores, lines)
    """
    pass


def update(board, n, i, j, l, scores, player, lines):
    """
    Met à jour le plateau de jeu en affectant l à la case (i,j)
    Recherche les éventuels alignements et met à jour scores et lines en conséquence
    :param board: Tableau de jeu
    :param n: Taille du tableau de jeu
    :param i:
    :param j:
    :param l:
    :param scores: Tableau des scores
    :param player: Joueur en cours
    :param lines: Tableau des nouvelles lignes
    :return:
    """
    pass


def winner(scores):
    """
    :param scores: Tableau des scores
    :return: Chaîne de caractère indiquant le résultat de la partie
    """
    pass
