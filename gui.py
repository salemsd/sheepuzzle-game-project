from fltk import *
from os import listdir
from grille import *
from jeu import *
from solveur import *

mainMenuWidth = 800
mainMenuHeight = 600

box_width = 94
box_height = 92

sideMenu_width = box_width * 3


def affiche_menuPrincipal():
    """
    Affiche le menu principal du jeu avec le choix du type de grille et le message de bienvenue
    """
    cree_fenetre(mainMenuWidth, mainMenuHeight)
    rectangle(0, 0, mainMenuWidth, mainMenuHeight,
              couleur='', remplissage='black')

    texte(mainMenuWidth/2, mainMenuHeight/6, 'Ricosheep',
          couleur='white', ancrage='center', taille=35)
    texte(mainMenuWidth/2, (mainMenuHeight/6)*2, 'Bienvenue dans le jeu',
          couleur='white', ancrage='center', taille=20)
    texte(mainMenuWidth/2, (mainMenuHeight/6)*2.7, 'Veuillez choisir un type de grille',
          couleur='white', ancrage='center', taille=20)

    i = 3.5
    rect_coord = []
    for typeGrille in ['Big', 'Square', 'Tests', 'Theme', 'Wide']:
        texte(mainMenuWidth/2, (mainMenuHeight/6)*i, typeGrille,
              couleur='white', ancrage='center', taille=14)
        rect_ax, rect_ay = mainMenuWidth/2 - 40, (mainMenuHeight/6)*i - 20
        rect_bx, rect_by = mainMenuWidth/2 + 40, (mainMenuHeight/6)*i + 15
        rect_coord.append((rect_ax, rect_ay, rect_bx, rect_by))
        rectangle(rect_ax, rect_ay, rect_bx, rect_by,
                  couleur='white', epaisseur=2)
        i = i+0.5

    rectIntervals = []
    for rect in rect_coord:
        rectIntervals.append(
            (getRect_xInterval(rect), getRect_yInterval(rect)))

    quitte = False
    while not quitte:
        ev_souris = attend_ev()
        if type_ev(ev_souris) == 'ClicGauche':
            x, y = abscisse(ev_souris), ordonnee(ev_souris)
            if x in rectIntervals[0][0] and y in rectIntervals[0][1]:
                choix = 'Big'
                break
            elif x in rectIntervals[1][0] and y in rectIntervals[1][1]:
                choix = 'Square'
                break
            elif x in rectIntervals[2][0] and y in rectIntervals[2][1]:
                choix = 'Tests'
                break
            elif x in rectIntervals[3][0] and y in rectIntervals[3][1]:
                choix = 'Theme'
                break
            elif x in rectIntervals[4][0] and y in rectIntervals[4][1]:
                choix = 'Wide'
                break
        elif type_ev(ev_souris) == 'Quitte':
            quitte = True
            ferme_fenetre()

    if not quitte:
        affiche_menuGrille(choix)


def getRect_xInterval(rect):
    return list(range(int(rect[0]), int(rect[2])+1, 1))


def getRect_yInterval(rect):
    return list(range(int(rect[1]), int(rect[3])+1, 1))


def affiche_menuGrille(choix):
    """
    Affiche le menu du choix de la grille après le menu principal

    :param string choix: Le choix du type de grille effectué par l'utilisateur
    """
    rectangle(0, 0, mainMenuWidth, mainMenuHeight,
              couleur='', remplissage='black')

    texte(mainMenuWidth/2, mainMenuHeight/6,
          f'Vous avez choisi le type {choix}', couleur='white', ancrage='center', taille=35)
    texte(mainMenuWidth/2, (mainMenuHeight/6)*2, f'Choisir une grille (appuyer sur la touche correspondante)',
          couleur='white', ancrage='center', taille=22)
    texte(mainMenuWidth/1.27, (mainMenuHeight/6)*5.88,
          'Appuyez sur Esc pour revenir en arriere', couleur='white', ancrage='center', taille=13)

    if choix == 'Big':
        listeGrilles = listdir('./maps/big')
    elif choix == 'Square':
        listeGrilles = listdir('./maps/square')
    elif choix == 'Tests':
        listeGrilles = listdir('./maps/tests')
    elif choix == 'Theme':
        listeGrilles = listdir('./maps/theme')
    elif choix == 'Wide':
        listeGrilles = listdir('./maps/wide')

    alphabet = list(map(chr, range(97, 97+len(listeGrilles))))
    i = 0
    j = 3.5
    for grille in listeGrilles:
        texte(mainMenuWidth/2, (mainMenuHeight/6)*j,
              f'{alphabet[i]}. {grille}', couleur='white', ancrage='center', taille=35)
        i = i + 1
        j = j + 0.5

    back, quitte = False, False
    while not(back or quitte):
        ev_choixGrille = attend_ev()
        if type_ev(ev_choixGrille) == 'Touche':
            if touche_pressee('Escape'):
                back = True
                ferme_fenetre()
            elif touche(ev_choixGrille) in alphabet:
                plateau, moutons = charger(
                    f'maps/{choix.lower()}/{listeGrilles[alphabet.index(touche(ev_choixGrille))]}')
                ferme_fenetre()
                break
        elif type_ev(ev_choixGrille) == 'Quitte':
            ferme_fenetre()
            quitte = True

    if not (back or quitte):
        affiche_jeuMenu(plateau, moutons)
    elif back:
        affiche_menuPrincipal()


def affiche_jeuMenu(plateau, moutons, first_execution=True):
    """
    Affiche la grille du jeu choisie par l'utilisateur

    :param list plateau: La grille du jeu
    :param list moutons: La liste des moutons
    """
    window_width = box_width * len(plateau[0]) + sideMenu_width
    window_height = box_height * len(plateau)

    if first_execution:
        cree_fenetre(window_width, window_height)

    rectangle(0, 0, window_width, window_height, remplissage='grey')

    sideMenu_x = window_width - sideMenu_width
    rectangle(sideMenu_x, 0, window_width, window_height, remplissage='black')

    texte(sideMenu_x + sideMenu_width/2, window_height/11.5,
          'Contrôles du jeu', couleur='white', ancrage='center', taille=20)
    texte(sideMenu_x + sideMenu_width/2, (window_height/11.5)*2.4,
          'Touches directionnelles', couleur='white', ancrage='center', taille=13)
    texte(sideMenu_x + sideMenu_width/2, (window_height/11.5)*3.4,
          'Déplacer les moutons', couleur='white', ancrage='center', taille=10)
    texte(sideMenu_x + sideMenu_width/2, (window_height/11.5)*4.5,
          'Touche \'S\'', couleur='white', ancrage='center', taille=13)
    texte(sideMenu_x + sideMenu_width/2, (window_height/11.5)*5.5,
          'Solver la grille', couleur='white', ancrage='center', taille=10)
    texte(sideMenu_x + sideMenu_width/2, (window_height/11.5)*6.6,
          'Touche \'R\'', couleur='white', ancrage='center', taille=13)
    texte(sideMenu_x + sideMenu_width/2, (window_height/11.5)*7.6,
          'Rejouer', couleur='white', ancrage='center', taille=10)
    texte(sideMenu_x + sideMenu_width/2, (window_height/11.5)*8.7,
          'Touche \'Esc\'', couleur='white', ancrage='center', taille=13)
    texte(sideMenu_x + sideMenu_width/2, (window_height/11.5)*9.7,
          'Revenir au menu', couleur='white', ancrage='center', taille=10)

    if first_execution:
        affiche_jeu(plateau, moutons)


def affiche_jeu(plateau, moutons):
    dessine_grille(plateau, moutons)

    moutons_base = moutons[:]
    back = False
    victoire_gui = victoire(plateau, moutons)
    while not(back or victoire_gui):
        appui_touche = attend_ev()
        if type_ev(appui_touche) == 'Touche':
            if touche(appui_touche) in ['Left', 'Right', 'Up', 'Down']:
                # efface_grille(grid_width, window_height)
                efface_tout()
                affiche_jeuMenu(plateau, moutons, False)
                jouer(plateau, moutons, touche(appui_touche))
                dessine_grille(plateau, moutons)
            elif touche_pressee('r'):
                moutons = moutons_base[:]
                efface_tout()
                affiche_jeuMenu(plateau, moutons, False)
                dessine_grille(plateau, moutons)
            elif touche_pressee('s'):
                print(
                    f'La solution de cette grille est : {solutions(plateau, moutons)}')
                moutons = moutons_base[:]
            elif touche_pressee('Escape'):
                back = True
                ferme_fenetre()
            victoire_gui = victoire(plateau, moutons)
        elif type_ev(appui_touche) == 'Quitte':
            ferme_fenetre()
            break

    if victoire_gui:
        affiche_menuVictoire()
    elif back:
        affiche_menuPrincipal()


def dessine_grille(plateau, moutons):
    """
    Dessine la grille du jeu dans la fenêtre

    :param list plateau: La grille du jeu
    :param list moutons: La liste des moutons
    """

    for i in range(len(plateau)):
        for j in range(len(plateau[0])):
            x_case = j * box_width
            y_case = i * box_height

            rectangle(x_case, y_case, x_case + box_width,
                      y_case + box_height, epaisseur=2)

            if plateau[i][j] == 'G':
                if (i, j) in moutons:
                    image(x_case + box_width/2, y_case +
                          box_height/2, "./media/sheep_grass.png")
                else:
                    image(x_case + box_width/2, y_case +
                          box_height/2, "./media/grass.png")
            elif plateau[i][j] == 'B':
                image(x_case + box_width/2, y_case +
                      box_height/2, "./media/bush.png")
            else:
                if (i, j) in moutons:
                    image(x_case + box_width/2, y_case +
                          box_height/2, "./media/sheep.png")


def affiche_menuVictoire():
    print('Vous avez gagné!')
    attente(2)
    ferme_fenetre()
    cree_fenetre(mainMenuWidth, mainMenuHeight)
    rectangle(0, 0, mainMenuWidth, mainMenuHeight, remplissage='black')
    texte(mainMenuWidth/2, mainMenuHeight/6, 'Bien joué!',
          couleur='white', ancrage='center', taille=30)
    texte(mainMenuWidth/2, (mainMenuHeight/6)*3, 'Appuyer sur \'R\' pour rejouer',
          couleur='white', ancrage='center', taille=20)
    texte(mainMenuWidth/2, (mainMenuHeight/6)*4, 'Appuyer sur \'Q\' pour quitter',
          couleur='white', ancrage='center', taille=20)

    back = False
    while not back:
        choix = attend_ev()
        if type_ev(choix) == 'Touche':
            if touche_pressee('r'):
                ferme_fenetre()
                back = True
            elif touche_pressee('q'):
                ferme_fenetre()
                break
        elif type_ev(choix) == 'Quitte':
            ferme_fenetre()
            break

    if back:
        affiche_menuPrincipal()
