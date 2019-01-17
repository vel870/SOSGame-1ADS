########################
# 1 ADS - MP 2 - SUPINFO
########################
import pygame
from time import sleep

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


def drawRect(mySurface, x, y, width, height, color):
    """
    Dessine un rectangle à l'écran
    :param mySurface: pygame.Surface
    :param x: coordonnée x du haut gauche du rectangle
    :param y: coordonnée y du haut gauche du rectangle
    :param width: Largeur du rectangle
    :param height: Hauteur du rectangle
    :param color:  Couleur de fond
    :return: pygame.Rect
    """
    rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(mySurface, color, rect)

    return rect


def drawText(mySurface, text, x, y, font, color, background = None):
    """
    Ecrit du texte à l'écran
    :param mySurface: pygame.Surface
    :param text: Texte à écrire
    :param x: coordonnée x du haut gauche du texte
    :param y: coordonnée y du haut gauche du texte
    :param font: Police d'écriture
    :param color: Couleur
    :param background: (optionnel) Couleur de fond
    :return: pygame.Rect
    """
    surface = font.render(text, 1, color, background)
    rect = mySurface.blit(surface, (x, y))

    return rect


def drawBoard(mySurface, n, board, cells = False):
    """
    Dessine le plateau initial
    :param mySurface: Surface pyGame
    :param n: Taille du tableau de jeu
    :param board: Tableau de jeu
    :param cells: Liste de cellules, optionnel, uniquement si chargement d'une partie enregistrée
    :return: Dictionnaire d'objets pygame.Rect cliquables
    """
    global updatedRects

    mySurface.fill(colors['lightgrey'])

    # Dessin des rectangles nécessaires au jeu
    gamemenu_rect = drawRect(mySurface, 50, 75, 180, 50, colors['lightblue'])
    newgame_rect = drawRect(mySurface, 50, 150, 180, 50, colors['lightblue'])
    quit_rect = drawRect(mySurface, 50, 225, 180, 50, colors['lightblue'])
    savegame_rect = drawRect(mySurface, 50, 545, 180, 50, colors['lightblue'])
    cellsbackground_rect = drawRect(mySurface, 250, 70, 530, 530, colors['lightblue'])

    # Ecriture des textes nécessaires au jeu
    drawText(mySurface, "Game Menu", 82, 85, fonts['base'], colors['darkblue'])
    drawText(mySurface, "New Game", 89, 162, fonts['base'], colors['darkblue'])
    drawText(mySurface, "Quit Game", 92, 237, fonts['base'], colors['darkblue'])
    drawText(mySurface, "P1 Score :", 65, 367, fonts['base'], colors['blue'])
    drawText(mySurface, "P2 Score :", 65, 442, fonts['base'], colors['red'])
    drawText(mySurface, "Save Game", 84, 557, fonts['base'], colors['darkblue'])

    new_cells = []

    if not cells:
        # Génération de toutes les cellules à l'état par défaut (nouveau jeu)
        for i in range(0, n):
            for j in range(0, n):

                new_cells.append({
                    'i': i,
                    'j': j,
                    'player': -1,
                    'rect': drawCell(mySurface, board, i, j, -1)
                })
    else:
        # Génération de toutes les cellules selon le contenu de la variable cells (chargement de sauvegarde)
        for cell in cells:
            new_cells.append({
                    'i': cell['i'],
                    'j': cell['j'],
                    'player' : cell['player'],
                    'rect' : drawCell(mySurface, board, cell['i'], cell['j'], cell['player'])
            })

    # Mise à jour de l'entièreté de l'écran (voir la fin de gamePlay())
    updatedRects.append(
        pygame.Rect(0, 0, options['window']['width'], options['window']['height'])
    )

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

    updatedRects += [
        drawText(mySurface, str(scores[0])+"  ", 200, 367, fonts['base'], colors['darkblue'], colors['lightgrey']),
        drawText(mySurface, str(scores[1])+"  ", 200, 442, fonts['base'], colors['darkblue'], colors['lightgrey']),
    ]

    return True


def drawArrow(mySurface, player):
    """
    Draw the arrow pointing to currently playing player
    :param mySurface: Game surface
    :param player: Current Player
    :return:
    """
    if player == 0:
        arrow = pygame.draw.aalines(mySurface, colors['blue'], 1, [[10, 385], [10, 375], [40, 380]])
        previous = pygame.Rect(10, 450, 31, 11)
    elif player == 1:
        arrow = pygame.draw.aalines(mySurface, colors['red'], 1, [[10, 460], [10, 450], [40, 455]])
        previous = pygame.Rect(10, 375, 31, 11)

    pygame.draw.rect(mySurface, colors['lightgrey'], previous)
    updatedRects.append(arrow)
    updatedRects.append(previous)


def displayPlayer(mySurface, n, player):
    """
    Affiche au joueur "player" que c'est son tour
    :param mySurface: Surface pyGame
    :param n: Taille du tableau de jeu
    :param player: Joueur en cours
    :return: True si succès, False sinon
    """
    global updatedRects

    updatedRects.append(
        drawText(mySurface, "C'est au joueur " + str(player + 1) + "   ", 265, 635, fonts['base'], colors['darkblue'], colors['lightgrey']),
    )

    drawArrow(mySurface, player),

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

    # Choix du texte en fonction de board[i][j]
    # L'utilisation de dictionnaires ici sert simplement à éviter un longue chaîne de if...
    celltext_dict = {
        0: {
            'text': 'S | 0',
            'x': x + 14,
            'y': y + 21,
        },
        1 : {
            'text' : 'S',
            'x' : x + 28,
            'y' : y + 21,
        },
        2: {
            'text': 'O',
            'x': x + 29,
            'y': y + 21,
        },
    }
    celltext = celltext_dict[board[i][j]]

    # Choix de la couleur du texte en fonction de player
    # Même remarque que plus haut.
    cellcolor_dict = {
        -1: colors['darkblue'],
        0: colors['blue'],
        1: colors['red']
    }
    cellcolor = cellcolor_dict[player]

    # Dessin de la cellule
    cell_rect = drawRect(mySurface, x, y, 70, 70, colors['white'])
    drawText(mySurface, celltext['text'], celltext['x'], celltext['y'], fonts['base'], cellcolor)

    updatedRects.append(cell_rect)
    return cell_rect


def drawLines(mySurface, lines):
    """
    Dessine les nouvelles lignes contenues dans lines de la couleur de player
    :param mySurface: Surface pyGame
    :param lines: Tableau des nouvelles lignes
    :return: True si succès, False sinon
    FIXME: Il semble que pygame.draw.line retourne un pygame.rect qui ne prends pas en compte l'épaisseur de la ligne
           et donc ne permet pas de mettre à jour l'affichage correctement
    """
    global updatedRects

    for line in lines:

        # Calcul des coordonnées des lignes
        x_start = 290 + 75 * line['start'][1]
        y_start = 110 + 75 * line['start'][0]
        x_stop = 290 + 75 * line['end'][1]
        y_stop = 110 + 75 * line['end'][0]

        line_color = colors['blue'] if line['player'] == 0 else colors['red']

        updatedRects.append(
            pygame.draw.line(mySurface, line_color, (x_start, y_start), (x_stop, y_stop), 3)
        )

    return True


def displayWinner(mySurface, n, scores):
    """
    Dessine le résultat de la partie à l'écran
    :param mySurface: Surface pyGame
    :param n: Taille du tableau de jeu
    :param scores: Tableau des scores
    :return: True si succès, False sinon
    """
    global updatedRects

    updatedRects.append(
        drawText(mySurface, str(winner(scores)), 265, 20, fonts['base'], colors['darkblue'], colors['lightgrey'])
    )

    return True


def saveGame(gamestate, player, board, cells, lines, scores):
    """
    Enregistrement des données de jeu
    :param gamestate: Variable d'état de jeu
    :param player: Joueur en cours
    :param board: Tableau de jeu actuel
    :param cells: Tableau des cellules
    :param lines: Tableau des lignes
    :param scores: Scores actuels
    :return: True si succès, False sinon
    """

    # On veut enregistrer les données de cellules sans leur valeur "pygame.Rect"
    for cell in cells:
        cell.pop('rect')

    # Creation du dictionnaire de données à enregistrer complet
    data = {
        'gamestate': gamestate,
        'player': player,
        'board': board,
        'cells': cells,
        'lines': lines,
        'scores': scores
    }

    # Vérification du bon déroulement de la sauvegarde
    if saveData(data, options['savepath']):
        return True

    return False


def gamePlay(mySurface, board, n, scores, gamestate, savedata = False):
    """
    Gère une partie SOS Complète
    :param mySurface: Surface pyGame
    :param board: Tableau de jeu
    :param n: Taille du tableau de jeu
    :param scores: Tableau des scores
    :param gamestate: (int) Etat du jeu
    :param savedata: Données de sauvegarde (optionnel)
    :return: Nouveau gamestate
    """
    global updatedRects

    playing = 1
    cellChanged = False
    clock = pygame.time.Clock()

    if not savedata:
        # Si savedata n'est pas initialisé, on charge une partie vide
        player = 0
        clickable_rects = drawBoard(mySurface, n, board)
        all_lines = []

    else:
        # Sinon on met en place la partie sauvegardée précédemment
        player = savedata['player']
        board = savedata['board']
        scores = savedata['scores']
        clickable_rects = drawBoard(mySurface, n, board, savedata['cells'])
        all_lines = savedata['lines']
        drawLines(mySurface, all_lines)

    # Affichage du joueur et du score initiaux
    displayPlayer(mySurface, n, player)
    displayScore(mySurface, n, scores)

    while playing:

        if (gamestate == 3 or gamestate == 4) and player == 1:
            # Tour d'une IA

            i, j, l = playDumbAI(board, n)

            for cell in clickable_rects['cells']:
                if cell['i'] == i and cell['j'] == j:
                    cell['player'] = 1
                    break

            cellChanged = True

        else:
            # Tour d'un joueur réel
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    return 0
                elif event.type == pygame.MOUSEBUTTONDOWN:

                    if clickable_rects['quitGame'].collidepoint(event.pos):
                        # Nouveau game state : 0, fermeture de l'application
                        return 0

                    elif clickable_rects['newGame'].collidepoint(event.pos):
                        # Initialisation d'une nouvelle partie du même type
                        board = newBoard(n)
                        scores = [0, 0]
                        return gamePlay(mySurface, board, n, scores, gamestate, False)

                    elif clickable_rects['mainMenu'].collidepoint(event.pos):
                        # Nouveau game state : 1, retour au menu principal
                        return 1

                    elif clickable_rects['saveGame'].collidepoint(event.pos):
                        # Enregistrement des données de jeu sur le disque et retour au menu principal
                        saveGame(gamestate, player, board, clickable_rects['cells'], all_lines, scores)
                        return 1

                    else:

                        for cell in clickable_rects['cells']:

                            if not cell['rect'].collidepoint(event.pos):
                                continue

                            if not possibleSquare(board, n, cell['i'], cell['j']):
                                continue

                            i = cell['i']
                            j = cell['j']

                            l = 1 if cell['rect'].centerx >= event.pos[0] else 2

                            cell['player'] = player
                            cellChanged = True

                            # On considère qu'on ne peut cliquer qu'une cellule à la fois, on sort du "for"
                            break

        if cellChanged:
            # ... Si un joueur ou une IA a choisi une case

            board, scores, lines = update(board, n, i, j, l, scores, player, [])

            # Mise à jour de l'affichage
            drawCell(mySurface, board, i, j, player)
            drawLines(mySurface, lines)
            all_lines += lines
            displayScore(mySurface, n, scores)

            # Changement de joueur conditionnel
            player = togglePlayer(player) if not lines else player
            displayPlayer(mySurface, n, player)
            cellChanged = False

        if updatedRects:
            # Si la variable updatedRects n'est pas vide, on met à jour l'affichage en conséquence
            # en faisant attention de ne mettre à jour que les parties de l'écran qui ont été modifiées
            pygame.display.update(updatedRects)
            updatedRects = []

        if won(board):
            # Si on détecte la victoire
            displayWinner(mySurface, n, scores)
            pygame.display.update(updatedRects)
            sleep(5)
            playing = False

        clock.tick(25)

    return 1  # Nouveau game state : 1, retour au menu principal


def SOS(n):
    """
    Crée une fenêtre graphique, initialise les structures de données et gère une partie complète.
    :param n: Taille du tableau de jeu
    :return: True
    """
    game_state = 1

    pygame.init()
    pygame.font.init()

    image_icon = pygame.image.load('assets/icon.png')

    mySurface = pygame.display.set_mode((options['window']['width'], options['window']['height']))
    pygame.display.set_caption('SOS Game')
    pygame.display.set_icon(image_icon)

    fonts['base'] = pygame.font.Font('assets/font2.otf', 25)
    savedata = False

    while game_state != 0:

        if game_state == 1:
            # GameState 1 : Launcher
            game_state = launcher(mySurface)

        elif game_state == 2:
            # GameState 2 : Jeu normal
            board = newBoard(n)
            scores = [0, 0]
            game_state = gamePlay(mySurface, board, n, scores, game_state, savedata)
            savedata = False

        elif game_state == 3:
            # GameState 3 : Jeu avec IA aléatoire (dumb_ai)
            board = newBoard(n)
            scores = [0, 0]
            game_state = gamePlay(mySurface, board, n, scores, game_state, savedata)
            savedata = False

        elif game_state == 4:
            # GameState 4 : Jeu avec IA Intelligente (hard_ai)
            pass

        elif game_state == 5:
            # GameState 5 : Chargement du jeu
            savedata = loadData(options['savepath'])
            game_state = savedata['gamestate']

        else:
            game_state = 0

    return True

SOS(7)
