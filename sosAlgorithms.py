########################
# 1 ADS - MP 2 - SUPINFO
########################


def newBoard(n):
    """
    Retourne une liste à deux dimension représentant l'état initial du plateau
    :param n: Nombre de lignes et de colonnes du tableau de jeu
    :return: Tableau de jeu
    """
    return [[0]*n]*n


def possibleSquare(board, n, i, j):
    """
    Retourne True si (i, j) sont les coordonnées d'une case où un joueur peut poser une lettre
    :param board: Tableau de jeu
    :param n: Taille du tableau de jeu
    :param i: Ligne de la case
    :param j: Colonne de la case
    :return: True | False
    """
    pass


def updateScoreS(board, n, i, j, scores, player, lines):
    """
    Appelée après que le joueur a posé un S, cherche les alignements créés et met à jour le score
    du joueur et la variable lines
    :param board: Tableau de jeu
    :param n: Taille du tableau de jeu
    :param i: Ligne de la case
    :param j: Colonne de la case
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
    :param i: Ligne de la case
    :param j: Colonne de la case
    :param scores: Tableau des scores
    :param player: Joueur en cours
    :param lines: Tableau des nouvelles lignes
    :return: (scores, lines)
    """

    """
    Tableau contenant toutes les combinaisons possibles de combinaisons après avoir posé un O. 
    Chaque combinaison comprends les coordonnées relatives des deux "S" potentiels
    """
    cellsToCheck = [
        [[i, j-1], [i, j+1]],
        [[i-1, j-1], [i+1, j+1]],
        [[i-1, j], [i+1, j]],
        [[i-1, j+1], [i+1, j-1]]
    ]

    for cells in cellsToCheck:

        # On vérifie si les coordonnées calculées sont sur le plateau
        if isCellOnBoard(n, cells[0][0], cells[0][1]) and isCellOnBoard(n, cells[1][0], cells[1][0]):

            # On incrémente le score si les deux cases sont bien des S
            if board[cells[0][0]][cells[0][1]] == 1 and board[cells[1][0]][cells[1][1]] == 1:

                lines += cells
                scores[player] += 1

    return scores, lines


def update(board, n, i, j, l, scores, player, lines):
    """
    Met à jour le plateau de jeu en affectant l à la case (i,j)
    Recherche les éventuels alignements et met à jour scores et lines en conséquence
    :param board: Tableau de jeu
    :param n: Taille du tableau de jeu
    :param i: Ligne de la case
    :param j: Colonne de la case
    :param l:
    :param scores: Tableau des scores
    :param player: Joueur en cours
    :param lines: Tableau des nouvelles lignes
    :return:
    """
    pass


def won(board):
    """
    :param board: Tableau de jeu
    :return: True si un joueur a gagné, False sinon
    """
    for i in board:
        for j in i:
            if j == 0:
                return False

    return True


def isCellOnBoard(n, i, j):
    """
    Vérifie la présence de la case (i,j) sur le plateau de taille n
    :param n: Taille du tableau de jeu
    :param i: Ligne de la case
    :param j: Colonne de la case
    :return: bool
    """
    if i in range(0, n) and j in range(0, n):
        return True

    return False


def togglePlayer(player):
    """
    Toggle player
    :param player: actual player
    :return: new player
    """
    return 1 if not player else 0


def winner(scores):
    """
    :param scores: Tableau des scores
    :return: Chaîne de caractère indiquant le résultat de la partie
    """
    pass
