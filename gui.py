from fltk import *
from os import listdir
from grille import *

mainMenuWidth = 800
mainMenuHeight = 600

    
def affiche_menuPrincipal():
    """
    Affiche le menu principal du jeu avec le choix du type de grille et le message de bienvenue
    """
    cree_fenetre(mainMenuWidth, mainMenuHeight)
    rectangle(0, 0, mainMenuWidth, mainMenuHeight, couleur='', remplissage='black')
    
    texte(mainMenuWidth/2, mainMenuHeight/6, 'Ricosheep', couleur='white', ancrage='center', taille=35)
    texte(mainMenuWidth/2, (mainMenuHeight/6)*2, 'Bienvenue dans le jeu', couleur='white', ancrage='center', taille=20)
    texte(mainMenuWidth/2, (mainMenuHeight/6)*2.7, 'Veuillez choisir un type de grille', couleur='white', ancrage='center', taille=20)
    
    i = 3.5
    rect_coord = []
    for typeGrille in ['Big', 'Square', 'Tests', 'Theme', 'Wide']:
        texte(mainMenuWidth/2, (mainMenuHeight/6)*i, typeGrille, couleur='white', ancrage='center', taille=14)
        rect_ax, rect_ay = mainMenuWidth/2 - 40, (mainMenuHeight/6)*i - 20
        rect_bx, rect_by = mainMenuWidth/2 + 40, (mainMenuHeight/6)*i + 15
        rect_coord.append((rect_ax, rect_ay, rect_bx, rect_by))
        rectangle(rect_ax, rect_ay, rect_bx, rect_by, couleur='white', epaisseur=2)
        i = i+0.5
    
    rectIntervals = []
    for rect in rect_coord:
        rectIntervals.append((getRect_xInterval(rect), getRect_yInterval(rect)))
  
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
    rectangle(0, 0, mainMenuWidth, mainMenuHeight, couleur='', remplissage='black')
    
    texte(mainMenuWidth/2, mainMenuHeight/6, f'Vous avez choisi le type {choix}', couleur='white', ancrage='center', taille=35)
    texte(mainMenuWidth/2, (mainMenuHeight/6)*2, f'Choisir une grille (appuyer sur la touche correspondante)', couleur='white', ancrage='center', taille=22)
    texte(mainMenuWidth/1.27, (mainMenuHeight/6)*5.88, 'Appuyez sur Esc pour revenir en arriere', couleur='white', ancrage='center', taille=13)


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
    print(alphabet)
    i = 0
    j = 3.5
    for grille in listeGrilles:
        texte(mainMenuWidth/2, (mainMenuHeight/6)*j, f'{alphabet[i]}. {grille}', couleur='white', ancrage='center', taille=35)
        i = i + 1
        j = j + 0.5

    back_quitte = False
    while not back_quitte:
        ev_choixGrille = attend_ev()
        if type_ev(ev_choixGrille) == 'Touche':
            print(ev_choixGrille)
            if touche_pressee('Escape'):
                back_quitte = True
                ferme_fenetre()
                affiche_menuPrincipal()
            else:
                for i in range(len(alphabet)):
                    if touche_pressee(alphabet[i]):
                        print(alphabet[i])
                        plateau, moutons = charger(f'maps/{choix.lower()}/{listeGrilles[i]}')
                        break
                break

        elif type_ev(ev_choixGrille) == 'Quitte':
            back_quitte = True
            ferme_fenetre()
    
    if not back_quitte:
        affiche_jeu(plateau, moutons)


def affiche_jeu(plateau, moutons):
    """
    Affiche la grille du jeu choisie par l'utilisateur

    :param list plateau: La grille du jeu
    :param list moutons: La liste des moutons
    """
    ferme_fenetre()
    
    box_width = 90
    box_height = 88

    sideMenu_width = 100
    
    window_width = box_width * len(plateau[0]) + sideMenu_width
    window_height = box_height * len(plateau)

    cree_fenetre(window_width, window_height)
    rectangle(0, 0, window_width, window_height, remplissage='grey')
    attend_fermeture()
    



def dessine_grille(x, y, plateau, moutons):
    """
    x, y: coordonnes du plateau
    :param list plateau: La grille du jeu
    :param list moutons: La liste des moutons
    """
    # dessine le plateau
    for j in range(len(p)):
        for i in range(len(p[j])):
            xt = x + i * 90
            yt = y + j * 88
            rectangle(xt, yt, xt + 90, yt + 88)
            if p[j][i] == 'G':
                image(xt + 45, yt + 44, "./media/grass.png")
            elif p[j][i] == 'B':
                image(xt + 45, yt + 44, "./media/bush.png")
    # dessine les moutons
    for i in ms:
        xi, yi = i
        image(xi * 90 + 45, yi * 88 + 44, "./media/sheep.png")
    return
    
def dessine_menu(ps, lms):
    """
    ps: ensemble des plateaus à choisir
    lms: liste des listes des moutons
    """
    p = ps[0]
    # calcule la taille d'un plateau
    l = 90 * len(p)
    x, y = 0, 0
    for i in range(len(ps)):
        x = i * l
        dessine_grille(x, 0, ps[i], lms[i])
        
