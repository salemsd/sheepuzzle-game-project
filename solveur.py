from jeu import *
from collections import deque

def moutons_trie(moutons):
    return sorted(moutons, key=lambda coord: (coord[0], coord[1]))

def victoire_def(plateau, moutons):
    """
    Détection de la victoire ET de la défaite (si le solveur ne trouve aucune solution)

    :param list plateau: La grille du jeu
    :param list moutons: La liste des positions des moutons
    :return: True si le jeu est gagné, False si on a perdu, None si on n'a pas encore gagné
    """
    
    touffes = []
    for i in range(len(plateau)):
        for j in range(len(plateau[0])):
            if plateau[i][j] == 'G':
                # Création d'une liste avec les coordonnées de chaque touffe
                touffes.append((i, j))

    for pos in touffes:
        # Si une seule des touffes n'est pas encore recouverte, on procède au test de défaite
        if pos not in moutons:     
            moutons_test = moutons[:]
            test_def = solutions(plateau, moutons_test, first_execution=True)
            # Si le solveur ne retourne aucune solution, on a perdu
            if test_def is None:
                return False
            # Sinon, on peut encore continuer de jouer
            return None

    return True

def solutions(plateau, moutons, visite=set(), first_execution=False):
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

        jouer(plateau, moutons, direction)

        s = solutions(plateau, moutons, visite)

        if s != None:
            # moutons = moutons_annule[:]
            return [direction] + s
        # Si le cas a déjà été visité, annule le jeu et continue à partir de là
        else:
            moutons = moutons_annule[:]
            continue


def solutions_lrg(plateau, moutons, visite=set(), dir_queue=deque(), first_execution=False):
    '''
    Recherche la solution du plateau avec le parcours en largeur

    :param list plateau: La grille du jeu
    :param list moutons: La liste des positions des moutons
    :param set visite: L'ensemble des positions visitées
    :param bool first_execution: Indique si c'est la première fois qu'on appelle la fonction
    '''
    # Si c'est la première execution, vide l'ensemble visite des eventuelles positions des précédentes executions
    if first_execution:
        visite.clear()
        dir_queue.clear()