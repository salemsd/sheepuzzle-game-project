from fltk import *
from os import listdir
from grille import *
from solveur import *

# Dimensions de la fenêtre du menu principal
mainMenuWidth = 800
mainMenuHeight = 600

# Dimensions d'une case
box_width = 94
box_height = 92

# Dimensions du menu à droite dans la fenêtre du jeu
sideMenu_width = box_width * 3


def affiche_menuPrincipal():
    """
    Affiche le menu principal du jeu avec le choix du type de grille et le message de bienvenue
    """
    cree_fenetre(mainMenuWidth, mainMenuHeight)
    rectangle(0, 0, mainMenuWidth, mainMenuHeight,
              couleur='', remplissage='black')  # Remplis la fenêtre en noir

    # Affichage du texte de choix de type de grille
    texte(mainMenuWidth/2, mainMenuHeight/6, 'Ricosheep',
          couleur='white', ancrage='center', taille=35)
    texte(mainMenuWidth/2, (mainMenuHeight/6)*2, 'Bienvenue dans le jeu',
          couleur='white', ancrage='center', taille=20)
    texte(mainMenuWidth/2, (mainMenuHeight/6)*2.7, 'Veuillez choisir un type de grille',
          couleur='white', ancrage='center', taille=20)

    i = 3.5  # Indice d'incrémentation de la coordonnée y du texte
    rect_coord = []  # Liste qui va contenir les coordonnées xa, ya, xb, yb de chaque rectangle
    for typeGrille in ['Big', 'Square', 'Tests', 'Theme', 'Wide']:
        texte(mainMenuWidth/2, (mainMenuHeight/6)*i, typeGrille,
              couleur='white', ancrage='center', taille=14)
        rect_ax, rect_ay = mainMenuWidth/2 - 40, (mainMenuHeight/6)*i - 20
        rect_bx, rect_by = mainMenuWidth/2 + 40, (mainMenuHeight/6)*i + 15
        rect_coord.append((rect_ax, rect_ay, rect_bx, rect_by))
        rectangle(rect_ax, rect_ay, rect_bx, rect_by,
                  couleur='white', epaisseur=2)
        i = i+0.5

    # Liste qui va contenir les intervalles x et y allant de gauche à droite et de haut en bas, de chaque rectangle
    rectIntervals = []
    for rect in rect_coord:  # Pour chaque rectangle de séléction, sauvegarder son intervalle dans la liste
        rectIntervals.append(get_rectInterval(rect))

    quitte = False  # Variable de type bool qui nous permettra de quitter la boucle
    while not quitte:
        ev_souris = attend_ev()  # Attend un événement sur l'interface
        # Si c'est un clic gauche enregistre ses coordonnées et vérifie si elles font partie d'un intervalle
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
        # Si c'est un clic sur le bouton 'Fermer', arrête la boucle et ferme la fenêtre
        elif type_ev(ev_souris) == 'Quitte':
            quitte = True
            ferme_fenetre()

    if not quitte:  # Affiche le choix de grille si l'utilisateur n'a pas quitté
        affiche_menuGrille(choix)


def get_rectInterval(rect):
    """
    Retourne l'intervalle x de gauche à droite et y de haut en bas d'un rectangle

    :param list rect: Les coordonnées xa, ya, xb, yb du rectangle
    :return: L'intervalle en forme de liste
    """
    return list(range(int(rect[0]), int(rect[2])+1, 1)), list(range(int(rect[1]), int(rect[3])+1, 1))


def affiche_menuGrille(choix):
    """
    Affiche le menu du choix de la grille après le menu principal

    :param string choix: Le choix du type de grille effectué par l'utilisateur
    """
    rectangle(0, 0, mainMenuWidth, mainMenuHeight,
              couleur='', remplissage='black')

    # Affichage du texte de choix de grille
    texte(mainMenuWidth/2, mainMenuHeight/6,
          f'Vous avez choisi le type {choix}', couleur='white', ancrage='center', taille=35)
    texte(mainMenuWidth/2, (mainMenuHeight/6)*2, f'Choisir une grille (appuyer sur la touche correspondante)',
          couleur='white', ancrage='center', taille=22)
    texte(mainMenuWidth/1.27, (mainMenuHeight/6)*5.88,
          'Appuyez sur Esc pour revenir en arriere', couleur='white', ancrage='center', taille=13)

    if choix == 'Big':
        # Liste tout les fichiers dans le dossier en forme de liste
        listeGrilles = listdir('./maps/big')
    elif choix == 'Square':
        listeGrilles = listdir('./maps/square')
    elif choix == 'Tests':
        listeGrilles = listdir('./maps/tests')
    elif choix == 'Theme':
        listeGrilles = listdir('./maps/theme')
    elif choix == 'Wide':
        listeGrilles = listdir('./maps/wide')

    # Retourne les caractères à partir du code ASCII 97 (lettre a)
    # jusqu'au nombre de fichiers qu'on a, en forme de string dans une liste
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
                # Si la touche pressée par l'utilsiateur fait partie des touches proposées,
                # charge la grille demandée
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


def affiche_jeuMenu(plateau, moutons, first_execution=True, affiche_recherche=False, affiche_sol=False):
    """
    Affiche le menu à droite du jeu et la grille choisie par l'utilisateur si c'est la première execution

    :param list plateau: La grille du jeu
    :param list moutons: La liste des moutons
    :param bool first_execution: Indique si c'est la première fois qu'on appelle la fonction
    :param bool affiche_recherche: Indique si l'affichage graphique de la recherche est actif (inactif par défaut)
    :param bool affiche_sol: Indique si l'affichage de la solution graphiquement est actif (inactif par défaut)
    """
    window_width = box_width * len(plateau[0]) + sideMenu_width
    window_height = box_height * len(plateau)

    if first_execution:
        cree_fenetre(window_width, window_height)

    rectangle(0, 0, window_width, window_height, remplissage='grey')

    sideMenu_x = window_width - sideMenu_width
    rectangle(sideMenu_x, 0, window_width, window_height, remplissage='black')

    # Affichage du texte du menu à droite du jeu
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
    texte(sideMenu_x + sideMenu_width/5.5, (window_height/11.5)*10.5,
          'Touche \'A\': ', couleur='white', ancrage='center', taille=9)
    texte(sideMenu_x + sideMenu_width/1.82, (window_height/11.5)*10.5,
          'Affichage de la recherche:', couleur='white', ancrage='center', taille=9)
    texte(sideMenu_x + sideMenu_width/5.5, (window_height/11.5)*11.1,
          'Touche \'Z\': ', couleur='white', ancrage='center', taille=9)
    texte(sideMenu_x + sideMenu_width/1.82, (window_height/11.5)*11.1,
          'Affichage de la solution:', couleur='white', ancrage='center', taille=9)

    if affiche_recherche:
        texte(sideMenu_x + sideMenu_width/1.16, (window_height/11.5)*10.5,
              'Actif', couleur='white', ancrage='center', taille=9)
    else:
        texte(sideMenu_x + sideMenu_width/1.16, (window_height/11.5)*10.5,
              'Inactif', couleur='white', ancrage='center', taille=9)
    
    if affiche_sol:
        texte(sideMenu_x + sideMenu_width/1.16, (window_height/11.5)*11.1,
              'Actif', couleur='white', ancrage='center', taille=9)
    else:
        texte(sideMenu_x + sideMenu_width/1.16, (window_height/11.5)*11.1,
              'Inactif', couleur='white', ancrage='center', taille=9)

    if first_execution:
        affiche_jeu(plateau, moutons)


def affiche_jeu(plateau, moutons):
    """
    Affiche la grille du jeu et débute le jeu

    :param list plateau: La grille du jeu
    :param list moutons: La grille des moutons
    """
    dessine_grille(plateau, moutons)

    # Crée une copie du jeu de base pour y revenir si l'utilisateur veut rejouer
    moutons_base = moutons[:]
    back = False
    victoire_gui = victoire_def(plateau, moutons)
    aff_rech = False  # Affichage de la recherche inactif par défaut
    aff_sol = False # Affichage de la solution inactif par défaut
    while not(back or victoire_gui is not None):
        appui_touche = attend_ev()
        if type_ev(appui_touche) == 'Touche':
            # Si touche directionnelle, efface la grille, joue la direction et redesinne la grille
            if touche(appui_touche) in ['Left', 'Right', 'Up', 'Down']:
                # efface_grille(grid_width, window_height)
                efface_tout()
                affiche_jeuMenu(plateau, moutons, False)
                jouer(plateau, moutons, touche(appui_touche))
                dessine_grille(plateau, moutons)
            # Si rejouer, recharge la grille de base, efface la grille et redessine
            elif touche_pressee('r'):
                moutons = moutons_base[:]
                efface_tout()
                affiche_jeuMenu(plateau, moutons, False, aff_rech, aff_sol)
                dessine_grille(plateau, moutons)
            elif touche_pressee('s'):
                moutons_avantSol = moutons[:] # Enregistre les moutons avant recherche
                
                if not aff_rech:
                    sol = solutions(plateau, moutons, first_execution=True)
                    moutons = moutons_avantSol[:] # Restaure les moutons après la recherche
                if aff_rech:
                    sol = solutions_gui(plateau, moutons, aff_sol, first_execution=True)
                    moutons = moutons_avantSol[:]
                    attente(0.7)
                    efface_tout()
                    print(aff_sol)
                    affiche_jeuMenu(plateau, moutons, False, aff_rech, aff_sol)
                    dessine_grille(plateau, moutons)    
                if aff_sol:
                    if aff_rech:
                        attente(0.7)
                    jouer_sol(plateau, moutons, sol, aff_rech)
                    attente(0.7)
                    moutons = moutons_avantSol[:]
                    efface_tout()
                    affiche_jeuMenu(plateau, moutons, False, aff_rech, aff_sol)
                    dessine_grille(plateau, moutons)
                
                print(f'La solution de cette grille est : {sol}')
                if sol is not None:
                    print(f'Longueur: {len(sol)}')
            
            elif touche_pressee('a'):
                aff_rech = not aff_rech
                efface_tout()
                affiche_jeuMenu(plateau, moutons, False, aff_rech, aff_sol)
                dessine_grille(plateau, moutons)

            elif touche_pressee('z'):
                aff_sol = not aff_sol
                efface_tout()
                affiche_jeuMenu(plateau, moutons, False, aff_rech, aff_sol)
                dessine_grille(plateau, moutons)

            elif touche_pressee('Escape'):
                back = True
                ferme_fenetre()
            victoire_gui = victoire_def(plateau, moutons)
        elif type_ev(appui_touche) == 'Quitte':
            ferme_fenetre()
            break

    if victoire_gui == True:
        affiche_menuFinJeu(True)
    elif victoire_gui == False:
        affiche_menuFinJeu(False)
    elif back:
        affiche_menuPrincipal()

def solutions_gui(plateau, moutons, aff_sol, visite=set(), first_execution=False):
    '''
    Recherche la solution du plateau avec le parcours en profondeur

    :param list plateau: La grille du jeu
    :param list moutons: La liste des positions des moutons
    :param set visite: L'ensemble des positions visitées
    :param bool first_execution: Indique si c'est la première fois qu'on appelle la fonction
    '''
    # Si c'est la première execution, vide l'ensemble visite des eventuelles positions des précédentes executions
    if first_execution:
        visite.clear()
    if victoire(plateau, moutons):
        return []
    if tuple(moutons_trie(moutons)) in visite:
        return None

    visite.add(tuple(moutons_trie(moutons)))
    # Enregistre la position des moutons avant de jouer pour y revenir
    moutons_annule = moutons[:]

    for direction in ['Left', 'Right', 'Up', 'Down']:

        jouer(plateau, moutons, direction) # Joue le coup
        efface_tout() 
        affiche_jeuMenu(plateau, moutons, False, True, aff_sol)
        dessine_grille(plateau, moutons) # Dessine la nouvelle grille
        attente(0.15) # Attend 0.15 sec avant de jouer l'autre coup

        s = solutions(plateau, moutons, visite)

        if s != None:
            # moutons = moutons_annule[:]
            return [direction] + s
        # Si le cas a déjà été visité, annule le jeu et continue à partir de là
        else:
            moutons = moutons_annule[:]
            continue

def jouer_sol(plateau, moutons, sol, aff_rech):
    '''
    Joue une série de coups entière sur un plateau

    :param list plateau: La grille du jeu
    :param list moutons: La liste des positions des moutons
    :param list sol: La liste des coups à jouer (ou la solution)
    '''
    if sol is not None and len(sol) != 0:
        for direction in sol:
            jouer(plateau, moutons, direction)
            efface_tout()
            affiche_jeuMenu(plateau, moutons, False, aff_rech, True)
            dessine_grille(plateau, moutons)
            attente(0.15)

def dessine_grille(plateau, moutons):
    """
    Dessine la grille du jeu dans la fenêtre

    :param list plateau: La grille du jeu
    :param list moutons: La liste des moutons
    """

    for i in range(len(plateau)):
        for j in range(len(plateau[0])):
            x_case = j * box_width  # Abscisse de début de la case à dessiner
            y_case = i * box_height  # Ordonnée

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


def affiche_menuFinJeu(victoire):
    """
    Affiche l'écran de victoire en fin de jeu
    """
    if victoire:
        print('Vous avez gagné!')
    else:
        print('Vous avez perdu!')
    attente(1)  # Attend 1 seconde avant d'afficher l'écran de victoire
    ferme_fenetre()
    cree_fenetre(mainMenuWidth, mainMenuHeight)
    rectangle(0, 0, mainMenuWidth, mainMenuHeight, remplissage='black')

    # Texte du menu de fin de jeu
    if victoire:
        texte(mainMenuWidth/2, mainMenuHeight/6, 'Bien joué!',
              couleur='white', ancrage='center', taille=30)
    else:
        texte(mainMenuWidth/2, mainMenuHeight/6, 'Perdu!',
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
