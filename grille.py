from fltk import *

def charger(fichier):
    """
    Charge la grille en fichier texte vers une liste
    :param str fichier: Le chemin du fichier à charger
    :return: La grille du jeu en forme de liste de liste
    """
    fPlateau = open(fichier, 'r')
    plateau = []
    moutons = []
    i = 0 # Indice de la ligne

    for line in fPlateau:
        row = []
        j = 0 # Indice de la colonne qui sera reinitialisé à 0 à chaque changement de ligne
        for char in line:
            if char != '\n':
                if char == '_':
                    row.append(None)
                elif char == 'S':
                    moutons.append((i, j))
                else:
                    row.append(char)
            j = j + 1
        plateau.append(row)
        i = i + 1
    
    return plateau, moutons