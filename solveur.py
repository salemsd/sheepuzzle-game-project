from jeu import *

def moutons_trie(moutons):
    return sorted(moutons, key=lambda coord: (coord[0], coord[1]))

def jouer_sol(plateau, moutons, sol):
    '''
    Joue une série de coups entière sur un plateau

    :param list plateau: La grille du jeu
    :param list moutons: La liste des positions des moutons
    :param list sol: La liste des coups à jouer (ou la solution)
    '''
    for direction in sol:
        jouer(plateau, moutons, direction)

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


def solutions_lrg(plateau, moutons, visite=set()):
    '''
    Recherche la solution du plateau avec le parcours en largeur

    :param list plateau: La grille du jeu
    :param list moutons: La liste des positions des moutons
    :param set visite: L'ensemble des positions visitées
    :param bool first_execution: Indique si c'est la première fois qu'on appelle la fonction
    '''
    if victoire(plateau, moutons):
        return []
    if tuple(moutons) in visite:
        return None

    # print(f'Avant: {moutons}')
    visite.add(tuple(moutons))
    moutons_annule = moutons[:]
    # print(f'Visites: {visite}')
    for direction in ['Down', 'Up', 'Right', 'Left']:

        jouer(plateau, moutons, direction)
        # print(f'{direction} : {moutons}')

        s = solutions(plateau, moutons, visite)

        if s != None:
            moutons = moutons_annule[:]
            return [direction] + s
        else:
            moutons = moutons_annule[:]
