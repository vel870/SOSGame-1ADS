########################
# 1 ADS - MP 2 - SUPINFO
########################
import pygame
import random

from sosAlgorithms import *
from sosLauncher import launcher

# Options catalog
options = {
    'window' : {
        'height' : 700,
        'width'  : 900,
    },
    'savepath' : 'savegame.json'
}

# Colors Catalog
colors = {
    'black'      : (0, 0, 0),
    'white'      : (255, 255, 255),
    'lightgrey'       : (179, 205, 224),
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


def drawBoard(mySurface, n, board, cells = False):
    """
    Dessine le plateau initial
    :param mySurface: Surface pyGame
    :param n: Taille du tableau de jeu
    :param board: Tableau de jeu
    :param cells: Liste de cellules, optionnel, uniquement si chargement d'une partie enregistrée
    :return: Liste d'objets Pygame.Rect cliquables
    """
    global updatedRects

    mySurface.fill(colors['lightgrey'])

    gamemenu_rect = pygame.Rect(50, 75, 180, 50)
    newgame_rect = pygame.Rect(50, 150, 180, 50)
    quit_rect = pygame.Rect(50, 225, 180, 50)
    savegame_rect = pygame.Rect(50, 545, 180, 50)
    cellsbackground_rect = pygame.Rect(250, 70, 530, 530)

    gamemenu_label = fonts['base'].render("Game Menu", 1, colors['darkblue'])
    newgame_label = fonts['base'].render("New Game", 1, colors['darkblue'])
    quit_label = fonts['base'].render("Quit Game", 1, colors['darkblue'])
    score_p1_label = fonts['base'].render("P1 Score : ", 1, colors['blue'])
    score_p2_label = fonts['base'].render("P2 Score : ", 1, colors['red'])
    savegame_label = fonts['base'].render("Save Game", 1, colors['darkblue'])

    pygame.draw.rect(mySurface, colors['lightblue'], gamemenu_rect)
    mySurface.blit(gamemenu_label, (82, 85))

    pygame.draw.rect(mySurface, colors['lightblue'], newgame_rect)
    mySurface.blit(newgame_label, (89, 162))

    pygame.draw.rect(mySurface, colors['lightblue'], quit_rect)
    mySurface.blit(quit_label, (92, 237))

    mySurface.blit(score_p1_label, (65, 367))

    mySurface.blit(score_p2_label, (65, 442))

    pygame.draw.rect(mySurface, colors['lightblue'], savegame_rect)
    mySurface.blit(savegame_label, (84, 557))

    pygame.draw.rect(mySurface, colors['lightblue'], cellsbackground_rect)

    new_cells = []

    if not cells:

        for i in range(0, n):
            for j in range(0, n):

                new_cells.append({
                    'i': i,
                    'j': j,
                    'player': -1,
                    'rect': drawCell(mySurface, board, i, j, -1)
                })

    else:

        for cell in cells:
            new_cells.append({
                    'i': cell['i'],
                    'j': cell['j'],
                    'player' : -1,
                    'rect' : drawCell(mySurface, board, cell['i'], cell['j'], cell['player'])
            })

    updatedRects.append(pygame.Rect(0, 0, options['window']['width'], options['window']['height']))

    return {
        'newGame': newgame_rect,
        'quitGame': quit_rect,
        'mainMenu': gamemenu_rect,
        'saveGame': savegame_rect,
        'cells': new_cells
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

    mySurface.fill(colors['lightgrey'], rect=score_player1_results.get_rect(topleft=(200, 367)))
    updatedRects.append(mySurface.blit(score_player1_results, (200, 367)))

    mySurface.fill(colors['lightgrey'], rect=score_player2_results.get_rect(topleft=(200, 442)))
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

    mySurface.fill(colors['lightgrey'], rect=playerTextRect)
    mySurface.blit(playerText, (265, 635))
    updatedRects.append(playerTextRect)

    return True


def drawCell(mySurface, board, i, j, player = -1):
    """
    Dessine le contenu de la case (i,j) de la couleur de player
    :param mySurface: Surface pyGame
    :param board: Tableau de jeu
    :param i: Ligne de la case
    :param j: Colonne de la case
    :param player: Joueur en cours
    :return: Objet PyGame.rect de la surface de la cellule
    """
    global updatedRects

    x = 255 + 75 * j
    y = 75 + 75 * i

    if board[i][j] == 1:
        text_str = "S"
        text_pos = (x + 25, y + 18)
    elif board[i][j] == 2:
        text_str = "O"
        text_pos = (x + 25, y + 18)
    else:
        text_str = "S/O"
        text_pos = (x + 20, y + 24)

    if player == -1:
        text_color = colors['darkblue']
    elif player == 0:
        text_color = colors['blue']
    elif player == 1:
        text_color = colors['red']
    else:
        text_color = colors['green'] # On ne devrait jamais être ici.

    cell_background = pygame.Rect(x, y, 70, 70)
    cell_text = fonts['base'].render(text_str, 1, text_color)

    pygame.draw.rect(mySurface, colors['white'], cell_background)
    mySurface.blit(cell_text, text_pos)

    updatedRects.append(cell_background)
    return cell_background


def drawLines(mySurface, lines):
    """
    Dessine les nouvelles lignes contenues dans lines de la couleur de player
    :param mySurface: Surface pyGame
    :param lines: Tableau des nouvelles lignes
    :return: Liste d'objets PyGame.rect des surfaces à mettre à jour
    """
    global updatedRects

    toUpdate = []

    for line in lines:

        x_start = 285 + 75 * line['start'][1]
        y_start = 110 + 75 * line['start'][0]
        x_stop = 285 + 75 * line['end'][1]
        y_stop = 110 + 75 * line['end'][0]

        line_color = colors['blue'] if line['player'] == 0 else colors['red']

        toUpdate.append(pygame.draw.line(mySurface, line_color, (x_start, y_start), (x_stop, y_stop), 3))

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
    updatedRects.append(mySurface.fill(colors['lightgrey'], rect=WhoWin.get_rect(topleft=(265, 20))))
    updatedRects.append(mySurface.blit(WhoWin, (265, 20)))

    return True


def saveGame(gamestate, player, board, cells, lines, scores):

    writable_cells = []

    for cell in cells:
        cell.pop('rect')
        writable_cells.append(cell)

    data = {
        'gamestate': gamestate,
        'player': player,
        'board': board,
        'cells': writable_cells,
        'lines': lines,
        'scores': scores
    }

    saveData(data, options['savepath'])
    return True


def gamePlay(mySurface, board, n, scores, savedata = False):
    """
    Gère une partie SOS Complète
    :param mySurface: Surface pyGame
    :param board: Tableau de jeu
    :param n: Taille du tableau de jeu
    :param scores: Tableau des scores
    :param savedata
    :return: Nouveau gamestate
    """
    global updatedRects

    playing = 1
    clock = pygame.time.Clock()

    if not savedata:
        player = 0
        clickable_rects = drawBoard(mySurface, n, board)
        all_lines = []

    else:
        player = savedata['player']
        board = savedata['board']
        scores = savedata['scores']
        clickable_rects = drawBoard(mySurface, n, board, savedata['cells'])
        all_lines = savedata['lines']
        drawLines(mySurface, all_lines)


    displayPlayer(mySurface, n, player)
    displayScore(mySurface, n, scores)

    while playing:

        if won(board):
            displayWinner(mySurface, n, scores)

        else:
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

                    elif clickable_rects['saveGame'].collidepoint(event.pos):
                        #TODO Dynamic gamestate
                        saveGame(2, player, board, clickable_rects['cells'], all_lines, scores)
                        return 1

                    else:

                        for cell in clickable_rects['cells']:

                            if not cell['rect'].collidepoint(event.pos):
                                continue

                            if not possibleSquare(board, n, cell['i'], cell['j']):
                                continue

                            l = 1 if event.button == 1 else 2

                            # Mise à jour des données de jeu
                            board, scores, lines = update(board, n, cell['i'], cell['j'], l, scores, player, [])
                            cell['player'] = player

                            # Mise à jour de l'affichage
                            drawCell(mySurface, board, cell['i'], cell['j'], player)
                            drawLines(mySurface, lines)
                            all_lines += lines
                            displayScore(mySurface, n, scores)

                            # Changement de joueur conditionnel
                            player = togglePlayer(player) if not lines else player
                            displayPlayer(mySurface, n, player)

                            # On considère qu'on ne peut cliquer qu'une cellule à la fois, on sort du "for"
                            break

        if updatedRects:
            # Si la variable updatedRects n'est pas vide, on met à jour l'affichage en conséquence
            # en faisant attention de ne mettre à jour que les parties de l'écran qui ont été modifiées
            pygame.display.update(updatedRects)
            updatedRects = []

        clock.tick(60)

    return 1  # Nouveau game state : 1, retour au menu principal


def gamePlayIA(mySurface, board, n, scores):
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
    displayPlayer(mySurface, n, player)
    displayScore(mySurface, n, scores)

    while playing:

        if won(board):
            displayWinner(mySurface, n, scores)

        else:

            if player == 0:
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
                                displayPlayer(mySurface, n, player)

                            # On considère qu'on ne peut cliquer qu'une cellule à la fois, on sort du "for"
                            break

            else:
                for cell in clickable_rects['cells']:

                    if not cell['rect'].collidepoint(event.pos):
                        continue

                    i = random.randint(0, n)
                    j = random.randint(0, n)
                    while not possibleSquare(board, n, i, j):
                        i = random.randint(0, n-1)
                        j = random.randint(0, n-1)

                    l = random.randint(1, 2)
                    board, scores, lines = update(board, n, i, j, l, scores, player, lines)
                    drawCell(mySurface, board, i, j, player)
                    displayScore(mySurface, n, scores)

                    player = 0
                    displayPlayer(mySurface, n, player)

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

    fonts['base'] = pygame.font.Font('assets/font2.otf', 25)
    savedata = False

    while game_state != 0:

        if game_state == 1:
            # GameState 1 : Launcher
            game_state = launcher(mySurface)

        elif game_state == 2:
            # GameState 2 : Normal Game
            board = newBoard(n)
            scores = [0, 0]
            game_state = gamePlay(mySurface, board, n, scores, savedata)
            savedata = False

        elif game_state == 3:
            # GameState 3 : Random IA Game
            board = newBoard(n)
            scores = [0, 0]
            game_state = gamePlayIA(mySurface, board, n, scores)

        elif game_state == 4:
            # GameState 4 : Hard IA Game
            pass

        elif game_state == 5:
            # GameState 5 : Load Game
            savedata = loadData(options['savepath'])
            game_state = savedata['gamestate']

        else:
            game_state = 0


SOS(7)
