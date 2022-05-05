from jeu import *


def solutions(plateau, moutons, visite=set()):
    if victoire(plateau, moutons):
        return []
    if tuple(moutons) in visite:
        return None

    # print(f'Avant: {moutons}')
    visite.add(tuple(moutons))
    # print(f'Visites: {visite}')

    for direction in ['Left', 'Right', 'Up', 'Down']:
        jouer(plateau, moutons, direction)
        # print(f'{direction} : {moutons}')

        s = solutions(plateau, moutons, visite)

        if s != None:
            # print(moutons)
            return [direction] + s

        else:
            continue
        # print('----------- DEJA VISITE ----------')
