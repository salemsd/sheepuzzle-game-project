from jeu import *

def solutions(plateau, moutons):
    visite = set()
    if victoire(plateau, moutons):
        return []
    if tuple(moutons) in visite:
        print('******************')
        return None
    
    # print(f'Avant: {moutons}')
    visite.add(tuple(moutons))
    # print(f'Visites: {visite}')
    
    for direction in ['Left', 'Right', 'Up', 'Down']:
        jouer(plateau, moutons, direction)
        # print(f'{direction} : {moutons}')
        
        s = solutions(plateau, moutons)
        
        if s != None:
            # print(moutons)
            return [direction] + s
        
        # print('----------- DEJA VISITE ----------')
