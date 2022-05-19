def tri_moutons(moutons, inv=False):
    """
    Trie les moutons par ordre croissant si False, décroissant si True (ligne -> colonne)

    :param list moutons: La liste des positions des moutons
    """
    moutons.sort(key = lambda coord: (coord[0], coord[1]), reverse=inv)

def jouer(plateau, moutons, direction):
    """ 
    Met à jour les positions des moutons

    :param list plateau: La grille du jeu
    :param list moutons: La liste des positions des moutons
    :param str direction: La chaîne representant la direction de déplacement
    """

    height = len(plateau)
    length = len(plateau[0])
    nb_moutons = len(moutons)

    if direction == 'Left' or direction == 'Up':
        tri_moutons(moutons) # Trie les moutons de gauche à droite et de haut en bas
    elif direction == 'Right' or direction == 'Down':
        tri_moutons(moutons, True) # Trie les moutons de droite à gauche et de bas en haut

    for m in range(nb_moutons):
        # Charge les coordonnées du mouton dans deux variables i et j
        i, j = moutons[m]
        
        obstacle_atteint = False
        while not obstacle_atteint:  # Tant qu'il n'y a pas de buissons et que la bordure n'est pas atteinte
            # Déplace les moutons dans la direction donnée jusqu'à toucher les bordures ou un
            # buisson ou un autre mouton
            if direction == 'Left':
                if j != 0 and plateau[i][j-1] != 'B' and (i, j-1) not in moutons:
                    j = j - 1
                else:
                    obstacle_atteint = True
            elif direction == 'Right':
                if j != length-1 and plateau[i][j+1] != 'B' and (i, j+1) not in moutons:
                    j = j + 1
                else:
                    obstacle_atteint = True
            elif direction == 'Up':
                if i != 0 and plateau[i-1][j] != 'B' and (i-1, j) not in moutons:
                    i = i - 1
                else:
                    obstacle_atteint = True
            elif direction == 'Down':
                if i != height-1 and plateau[i+1][j] != 'B' and (i+1, j) not in moutons:
                    i = i + 1
                else:
                    obstacle_atteint = True
        
        moutons.pop(m)
        # Met à jour les coordonnées du mouton avec les nouvelles, stockées dans i et j
        moutons.insert(m, (i, j))

    # tri_moutons(moutons)


def victoire(plateau, moutons):
    """
    Détéction de la victoire (si toutes les touffes d'herbes sont recouvertes par un mouton)
    :param list plateau: La grille du jeu
    :param list moutons: La liste des positions des moutons
    """

    touffes = []
    for i in range(len(plateau)):
        for j in range(len(plateau[0])):
            if plateau[i][j] == 'G':
                # Création d'une liste avec les coordonnées de chaque touffe
                touffes.append((i, j))

    victoire = True
    for pos in touffes:
        if pos not in moutons:
            victoire = False
    touffes = [(1, 2), (2, 3)]
    moutons = [(1, 2), (2, 3), (5, 6)]

    return victoire
