########################
# 1 ADS - MP 2 - SUPINFO
########################
import json
import random

def newBoard(n):
    """
    Retourne une liste à deux dimension représentant l'état initial du plateau
    :param n: Nombre de lignes et de colonnes du tableau de jeu
    :return: Tableau de jeu
    """
    # TODO Rewrite
    board = []
    for i in range(0, n):
        board_line = []
        for j in range(0, n):
            board_line.append(0)

        board.append(board_line)
    return board


def possibleSquare(board, n, i, j):
    """
    Retourne True si (i, j) sont les coordonnées d'une case où un joueur peut poser une lettre
    :param board: Tableau de jeu
    :param n: Taille du tableau de jeu
    :param i: Ligne de la case
    :param j: Colonne de la case
    :return: True | False
    """
    if isCellOnBoard(n, i, j) and board[i][j] == 0:
        return True

    return False


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

    """
    Tableau contenant toutes les combinaisons de "S - O - S" après avoir posé un S 
    Chaque combinaison comprends les coordonnées du S et du O possiblement déjà posé sur le plateau.
    Les coordonnées sont relatives à celles du S qui vient d'être posé
    """
    cellsToCheck = [
        [(i-2, j-2), (i-1, j-1)],
        [(i-2, j), (i-1, j)],
        [(i-2, j+2), (i-1, j+1)],
        [(i, j-2), (i, j-1)],
        [(i, j+2), (i, j+1)],
        [(i+2, j-2), (i+1, j-1)],
        [(i+2, j), (i+1, j)],
        [(i+2, j+2), (i+1, j+1)],
    ]

    for cell in cellsToCheck:

        # On vérifie si les coordonnées calculées sont sur le plateau
        if isCellOnBoard(n, cell[0][0], cell[0][1]) and isCellOnBoard(n, cell[1][0], cell[1][1]):

            # On incrémente le score si on a bien un S dans cells[0] et un O dans cells[1]
            if board[cell[0][0]][cell[0][1]] == 1 and board[cell[1][0]][cell[1][1]] == 2:

                # On ajoute une ligne entre les deux "S"
                lines.append({
                    'start' : (i, j),
                    'end'   : cell[0],
                    'player': player
                })
                scores[player] += 1

    return scores, lines


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
    Tableau contenant toutes les combinaisons possibles de S-O-S après avoir posé un O. 
    Chaque combinaison comprends les coordonnées relatives des deux "S" potentiellement déjà sur le plateau.
    """
    cellsToCheck = [
        [(i, j-1), (i, j+1)],
        [(i-1, j-1), (i+1, j+1)],
        [(i-1, j), (i+1, j)],
        [(i-1, j+1), (i+1, j-1)]
    ]

    for cell in cellsToCheck:

        # On vérifie si les coordonnées calculées sont sur le plateau
        if isCellOnBoard(n, cell[0][0], cell[0][1]) and isCellOnBoard(n, cell[1][0], cell[1][1]):

            # On incrémente le score si les deux cases sont bien des S
            if board[cell[0][0]][cell[0][1]] == 1 and board[cell[1][0]][cell[1][1]] == 1:

                lines.append({
                    'start' : cell[0],
                    'end'   : cell[1],
                    'player': player
                })
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
    :return: board, scores, lines
    """
    board[i][j] = l

    if l == 1:
        scores, lines = updateScoreS(board, n, i, j, scores, player, lines)
    else:
        scores, lines = updateScoreO(board, n, i, j, scores, player, lines)

    return board, scores, lines


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
    Change le joueur actuel
    TODO: marche seulement dans une configuration deux jouers classique
    :param player: actual player
    :return: new player
    """
    return 1 if not player else 0


def winner(scores):
    """
    :param scores: Tableau des scores
    :return: Chaîne de caractère indiquant le résultat de la partie
    """
    if scores[0] > scores[1]:
        return " Le joueur 1 a gagné ! "
    elif scores[0] < scores[1]:
        return " Le joueur 2 a gagné ! "
    else:
        return " Il y a égalité entre les joueurs ! "


def playDumbAI(board, n):
    """
    Fait choisir une case à l'intelligence artificielle aléatoire
    :param board: Tableau de jeu
    :param n: Taille du tableau de jeu
    :return: i, j, l
    """
    i = -1
    j = -1

    while not possibleSquare(board, n, i, j):
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)

    l = random.randint(1, 2)

    return i, j, l


def saveData(data, path):
    """
    Enregistrement des données contenues dans "data" dans le fichier au chemin "path" au format json
    :param data: Tableau de données Python
    :param path: Chemin du fichier
    :return:
    """
    try:
        with open(path, 'w') as savefile:
            json.dump(data, savefile)
        return True

    except Exception:
        return False


def loadData(path):
    """
    Chargement des données contenues dans la sauvegarde json dans le chemin "path"
    :param path: Chemin du fichier de sauvegarde
    :return: Données de sauvegarde, ou False
    """
    try:
        with open(path) as savefile:
            return json.load(savefile)

    except Exception:
        return False