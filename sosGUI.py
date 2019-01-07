########################
# 1 ADS - MP 2 - SUPINFO
########################

import pygame
from pygame.locals import *

from sosAlgorithms import *
from sosLauncher import launcher

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
Green1 = (173, 255, 0)

# Font Catalog
# Fonts are defined in SOS(), as they can't be defined before PyGame init.
fonts = {}


def drawBoard(mySurface, n):
    """
    Dessine le plateau initial
    :param mySurface: Surface pyGame
    :param n: Taille du tableau de jeu
    :return: Objet PyGame.rect de la surface à mettre à jour, liste d'objets Pygame.Rect cliquables
    """
    mySurface.fill(Blue0)

    gamemenu_rect = pygame.Rect(50, 75, 180, 50)
    newgame_rect = pygame.Rect(50, 150, 180, 50)
    quit_rect = pygame.Rect(50, 225, 180, 50)
    ScoreP1 = pygame.Rect(50, 355, 180, 50)
    ScoreP2 = pygame.Rect(50, 430, 180, 50)
    SaveGame = pygame.Rect(50, 545, 180, 50)

    gamemenu_label = fonts['base'].render("Game Menu", 1, Blue2)
    newgame_label = fonts['base'].render("New Game", 1, Blue2)
    quit_label = fonts['base'].render("Quit Game", 1, Blue2)
    score_p1_label = fonts['base'].render("P1 Score : ", 1, Blue2)
    score_p2_label = fonts['base'].render("P2 Score : ", 1, Blue2)
    SaveGame_label = fonts['base'].render("Save Game", 1, Blue2)

    pygame.draw.rect(mySurface, Blue1, gamemenu_rect)
    mySurface.blit(gamemenu_label, (60, 85))

    pygame.draw.rect(mySurface, Blue1, newgame_rect)
    mySurface.blit(newgame_label, (65, 162))

    pygame.draw.rect(mySurface, Blue1, quit_rect)
    mySurface.blit(quit_label, (65, 237))

    pygame.draw.rect(mySurface, Blue1, ScoreP1)
    mySurface.blit(score_p1_label, (65, 367))

    pygame.draw.rect(mySurface, Blue1, ScoreP2)
    mySurface.blit(score_p2_label, (65, 442))

    pygame.draw.rect(mySurface, Blue1, SaveGame)
    mySurface.blit(SaveGame_label, (65, 557))

    width = 75
    x, y = 250, 75

    cells = []

    for row in range(0, n):
        for col in range(0, n):

            cell_background = pygame.Rect(x, y, width, width)
            cell_text = fonts['base'].render("S/O", 1, Red0)

            pygame.draw.rect(mySurface, Blue1, cell_background, 5)
            mySurface.blit(cell_text, (x + 15, y + 25))

            x = x + width  # Déplacement à droite

            cells.append({
                'i': row,
                'j': col,
                'rect': cell_background
            })

        y = y + width  # Déplacement en bas
        x = 250  # Retour au côté gauche

    return pygame.Rect(0, 0, WINDOW_width, WINDOW_height), {
        'newGame': newgame_rect,
        'quitGame': quit_rect,
        'mainMenu': gamemenu_rect,
        'cells': cells
    }


def displayScore(mySurface, n, scores):
    """
    Affiche le score des deux joueurs
    :param mySurface: Surface pyGame
    :param n: Taille du tableau de jeu
    :param scores: Tableau des scores
    :return: Liste d'objets PyGame.rect des surfaces à mettre à jour
    """
    score_player1_results = fonts['base'].render(str(scores[0]), 1, Blue2)
    score_player2_results = fonts['base'].render(str(scores[1]), 1, Blue2)

    mySurface.fill(Blue1, rect=score_player1_results.get_rect(topleft=(200, 367)))
    mySurface.blit(score_player1_results, (200, 367))

    mySurface.fill(Blue1, rect=score_player2_results.get_rect(topleft=(200, 442)))
    mySurface.blit(score_player2_results, (200, 442))

    pygame.display.update()


def displayPlayer(mySurface, n, player):
    """
    Affiche au joueur "player" que c'est son tour
    :param mySurface: Surface pyGame
    :param n: Taille du tableau de jeu
    :param player: Joueur en cours
    :return: Liste d'objets PyGame.rect des surfaces à mettre à jour
    """
    WhoPLaying = fonts['base'].render("C'est au joueur " + str(player + 1), 1, Blue2)
    mySurface.fill(Blue0, rect=WhoPLaying.get_rect(topleft=(265, 635)))
    mySurface.blit(WhoPLaying, (265, 635))


def drawCell(mySurface, board, i, j, player):
    """
    Dessine le contenu de la case (i,j) de la couleur de player
    :param mySurface: Surface pyGame
    :param board: Tableau de jeu
    :param i: Ligne de la case
    :param j: Colonne de la case
    :param player: Joueur en cours
    :return: Objet PyGame.rect de la surface à mettre à jour
    """
    x = 255 + 75 * j
    y = 80 + 75 * i

    text = "S" if board[i][j] == 1 else "O"

    cell_background = pygame.Rect(x, y, 65, 65)
    if text == "S":
        cell_text = fonts['base'].render(text, 1, Blue)
    else:
        cell_text = fonts['base'].render(text, 1, Red)

    pygame.draw.rect(mySurface, White, cell_background)
    mySurface.blit(cell_text, (x + 23, y + 22))

    return cell_background


def drawLines(mySurface, lines, player):
    """
    Dessine les nouvelles lignes contenues dans lines de la couleur de player
    :param mySurface: Surface pyGame
    :param lines: Tableau des nouvelles lignes
    :param player: Joueur en cours
    :return: Liste d'objets PyGame.rect des surfaces à mettre à jour
    """
    toUpdate = []

    for line in lines:

        x_start = 285 + 75 * line[0][1]
        y_start = 110 + 75 * line[0][0]
        x_stop = 285 + 75 * line[1][1]
        y_stop = 110 + 75 * line[1][0]

        color = Blue1 if player == 1 else Green1

        toUpdate.append(pygame.draw.aaline(mySurface, color, (x_start, y_start), (x_stop, y_stop)))

    return toUpdate


def displayWinner(mySurface, n, scores):
    """
    Dessine le résultat de la partie à l'écran
    :param mySurface: Surface pyGame
    :param n: Taille du tableau de jeu
    :param scores: Tableau des scores
    :return: True si succès, False sinon
    """
    WhoWin = fonts['base'].render(str(winner(scores)), 1, Blue2)
    mySurface.fill(Blue0, rect=WhoWin.get_rect(topleft=(265, 20)))
    mySurface.blit(WhoWin, (265, 20))


def gamePlay(mySurface, board, n, scores):
    """
    Gère une partie SOS Complète
    :param mySurface: Surface pyGame
    :param board: Tableau de jeu
    :param n: Taille du tableau de jeu
    :param scores: Tableau des scores
    :return: Nouveau gamestate
    """
    playing = 1
    player = 0
    clock = pygame.time.Clock()

    rects_to_update, clickable_rects = drawBoard(mySurface, n)

    while playing:
        if won(board):
            displayWinner(mySurface, n, scores)
            pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return 0
            elif event.type == pygame.MOUSEBUTTONDOWN:

                if clickable_rects['quitGame'].collidepoint(event.pos):
                    # Nouveau game state : 0, fermeture de l'application
                    return 0

                elif clickable_rects['newGame'].collidepoint(event.pos):
                    print('Not implemented!!')

                elif clickable_rects['mainMenu'].collidepoint(event.pos):
                    # Nouveau game state : 1, retour au menu principal
                    return 1

                else:

                    for cell in clickable_rects['cells']:

                        if not cell['rect'].collidepoint(event.pos):
                            continue

                        if not possibleSquare(board, n, cell['i'], cell['j']):
                            continue

                        l = 1 if event.button == 1 else 2
                        lines = []

                        # Mise à jour des données de jeu
                        board, scores, lines = update(board, n, cell['i'], cell['j'], l, scores, player, lines)

                        # Mise à jour de l'affichage
                        rects_to_update.append(drawCell(mySurface, board, cell['i'], cell['j'], player))
                        rects_to_update += drawLines(mySurface, lines, player)
                        displayScore(mySurface, n, scores)

                        # Changement de joueur conditionnel
                        player = togglePlayer(player) if not lines else player
                        displayPlayer(mySurface, n, player)

                        # On considère qu'on ne peut cliquer qu'une cellule à la fois, on sort du "for"
                        break

        if rects_to_update:
            # Si la variable rects_to_update n'est pas vide, on met à jour l'affichage en conséquence
            # en faisant attention de ne mettre à jour que les parties de l'écran qui ont été modifiées
            pygame.display.update(rects_to_update)
            rects_to_update = []

        clock.tick(60)

    return 1  # Nouveau game state : 1, retour au menu principal


def SOS(n):
    """
    Crée une fenêtre graphique, initialise les structures de données et gère une partie complète.
    :param n: Taille du tableau de jeu
    :return:
    """
    game_state = 1

    pygame.init()
    pygame.font.init()

    mySurface = pygame.display.set_mode((WINDOW_width, WINDOW_height))
    pygame.display.set_caption('SOS Game')

    fonts['base'] = pygame.font.Font('freesansbold.ttf', 25)

    while game_state != 0:

        if game_state == 1:
            # GameState 1 : Launcher
            game_state = launcher(mySurface)

        elif game_state == 2:
            # GameState 2 : Normal Game
            board = newBoard(n)
            scores = [0, 0]
            game_state = gamePlay(mySurface, board, n, scores)

        elif game_state == 3:
            # GameState 3 : Random IA Game
            pass

        elif game_state == 4:
            # GameState 4 : Hard IA Game
            pass

        else:
            game_state = 0


SOS(7)
