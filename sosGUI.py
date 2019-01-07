########################
# 1 ADS - MP 2 - SUPINFO
########################
import pygame

from sosAlgorithms import *
from sosLauncher import launcher

# Options catalog
options = {
    'window' : {
        'height' : 700,
        'width'  : 900,
    }
}

# Colors Catalog
colors = {
    'black'      : (0, 0, 0),
    'white'      : (255, 255, 255),
    'grey'       : (179, 205, 224),
    'red'        : (255, 0, 0),
    'darkred'    : (206, 25, 25),
    'blue'       : (0, 0, 255),
    'darkblue' : (36, 48, 81),
    'lightblue'  : (3, 146, 255),
    'green'      : (0, 255, 0),
}

# Font Catalog
# Fonts are defined in SOS(), as they can't be defined before PyGame init.
fonts = {}

# PyGame.rect List
# Defines the surfaces that needs to be updated on a specific frame
# (see end of gamePlay())
updatedRects = []


def drawBoard(mySurface, n):
    """
    Dessine le plateau initial
    :param mySurface: Surface pyGame
    :param n: Taille du tableau de jeu
    :return: Liste d'objets Pygame.Rect cliquables
    """
    global updatedRects

    mySurface.fill(colors['grey'])

    gamemenu_rect = pygame.Rect(50, 75, 180, 50)
    newgame_rect = pygame.Rect(50, 150, 180, 50)
    quit_rect = pygame.Rect(50, 225, 180, 50)
    ScoreP1 = pygame.Rect(50, 355, 180, 50)
    ScoreP2 = pygame.Rect(50, 430, 180, 50)
    SaveGame = pygame.Rect(50, 545, 180, 50)

    gamemenu_label = fonts['base'].render("Game Menu", 1, colors['darkblue'])
    newgame_label = fonts['base'].render("New Game", 1, colors['darkblue'])
    quit_label = fonts['base'].render("Quit Game", 1, colors['darkblue'])
    score_p1_label = fonts['base'].render("P1 Score : ", 1, colors['blue'])
    score_p2_label = fonts['base'].render("P2 Score : ", 1, colors['red'])
    SaveGame_label = fonts['base'].render("Save Game", 1, colors['darkblue'])

    pygame.draw.rect(mySurface, colors['lightblue'], gamemenu_rect)
    mySurface.blit(gamemenu_label, (60, 85))

    pygame.draw.rect(mySurface, colors['lightblue'], newgame_rect)
    mySurface.blit(newgame_label, (65, 162))

    pygame.draw.rect(mySurface, colors['lightblue'], quit_rect)
    mySurface.blit(quit_label, (65, 237))

    pygame.draw.rect(mySurface, colors['lightblue'], ScoreP1)
    mySurface.blit(score_p1_label, (65, 367))

    pygame.draw.rect(mySurface, colors['lightblue'], ScoreP2)
    mySurface.blit(score_p2_label, (65, 442))

    pygame.draw.rect(mySurface, colors['lightblue'], SaveGame)
    mySurface.blit(SaveGame_label, (65, 557))

    width = 75
    x, y = 250, 75

    cells = []

    for row in range(0, n):
        for col in range(0, n):

            cell_background = pygame.Rect(x, y, width, width)
            cell_text = fonts['base'].render("S/O", 1, colors['darkred'])

            pygame.draw.rect(mySurface, colors['darkblue'], cell_background, 5)
            mySurface.blit(cell_text, (x + 15, y + 25))

            x = x + width  # Déplacement à droite

            cells.append({
                'i': row,
                'j': col,
                'rect': cell_background
            })

        y = y + width  # Déplacement en bas
        x = 250  # Retour au côté gauche

    updatedRects.append(pygame.Rect(0, 0, options['window']['width'], options['window']['height']))

    return {
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
    :return: True si succès, False sinon
    """
    global updatedRects

    score_player1_results = fonts['base'].render(str(scores[0]), 1, colors['darkblue'])
    score_player2_results = fonts['base'].render(str(scores[1]), 1, colors['darkblue'])

    mySurface.fill(colors['lightblue'], rect=score_player1_results.get_rect(topleft=(200, 367)))
    updatedRects.append(mySurface.blit(score_player1_results, (200, 367)))

    mySurface.fill(colors['lightblue'], rect=score_player2_results.get_rect(topleft=(200, 442)))
    updatedRects.append(mySurface.blit(score_player2_results, (200, 442)))

    return True


def displayPlayer(mySurface, n, player):
    """
    Affiche au joueur "player" que c'est son tour
    :param mySurface: Surface pyGame
    :param n: Taille du tableau de jeu
    :param player: Joueur en cours
    :return: True si succès, False sinon
    """
    global updatedRects

    playerText = fonts['base'].render("C'est au joueur " + str(player + 1), 1, colors['darkblue'])
    playerTextRect = playerText.get_rect(topleft=(265, 635))

    mySurface.fill(colors['grey'], rect=playerTextRect)
    mySurface.blit(playerText, (265, 635))
    updatedRects.append(playerTextRect)

    return True


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
    global updatedRects

    x = 255 + 75 * j
    y = 80 + 75 * i

    text = "S" if board[i][j] == 1 else "O"

    cell_background = pygame.Rect(x, y, 65, 65)
    if player == 0:
        cell_text = fonts['base'].render(text, 1, colors['blue'])
    else:
        cell_text = fonts['base'].render(text, 1, colors['red'])

    pygame.draw.rect(mySurface, colors['white'], cell_background)
    mySurface.blit(cell_text, (x + 23, y + 22))

    updatedRects.append(cell_background)


def drawLines(mySurface, lines, player):
    """
    Dessine les nouvelles lignes contenues dans lines de la couleur de player
    :param mySurface: Surface pyGame
    :param lines: Tableau des nouvelles lignes
    :param player: Joueur en cours
    :return: Liste d'objets PyGame.rect des surfaces à mettre à jour
    """
    global updatedRects

    toUpdate = []

    for line in lines:

        x_start = 285 + 75 * line[0][1]
        y_start = 110 + 75 * line[0][0]
        x_stop = 285 + 75 * line[1][1]
        y_stop = 110 + 75 * line[1][0]

        line_color = colors['blue'] if player == 0 else colors['red']

        toUpdate.append(pygame.draw.aaline(mySurface, line_color, (x_start, y_start), (x_stop, y_stop)))

    updatedRects += toUpdate


def displayWinner(mySurface, n, scores):
    """
    Dessine le résultat de la partie à l'écran
    :param mySurface: Surface pyGame
    :param n: Taille du tableau de jeu
    :param scores: Tableau des scores
    :return: True si succès, False sinon
    """
    global updatedRects

    WhoWin = fonts['base'].render(str(winner(scores)), 1, colors['darkblue'])
    updatedRects.append(mySurface.fill(colors['grey'], rect=WhoWin.get_rect(topleft=(265, 20))))
    updatedRects.append(mySurface.blit(WhoWin, (265, 20)))

    return True


def gamePlay(mySurface, board, n, scores):
    """
    Gère une partie SOS Complète
    :param mySurface: Surface pyGame
    :param board: Tableau de jeu
    :param n: Taille du tableau de jeu
    :param scores: Tableau des scores
    :return: Nouveau gamestate
    """
    global updatedRects

    playing = 1
    player = 0
    clock = pygame.time.Clock()

    clickable_rects = drawBoard(mySurface, n)

    while playing:

        if won(board):
            displayWinner(mySurface, n, scores)

        displayPlayer(mySurface, n, player)

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
                        drawCell(mySurface, board, cell['i'], cell['j'], player)
                        drawLines(mySurface, lines, player)
                        displayScore(mySurface, n, scores)

                        # Changement de joueur conditionnel
                        player = togglePlayer(player) if not lines else player
                        # On considère qu'on ne peut cliquer qu'une cellule à la fois, on sort du "for"
                        break

        if updatedRects:
            # Si la variable updatedRects n'est pas vide, on met à jour l'affichage en conséquence
            # en faisant attention de ne mettre à jour que les parties de l'écran qui ont été modifiées
            pygame.display.update(updatedRects)
            updatedRects = []

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

    mySurface = pygame.display.set_mode((options['window']['width'], options['window']['height']))
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
