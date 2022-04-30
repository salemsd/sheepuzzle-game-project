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
    rowLengths = [] # Liste pour sauvegarder la taille de chaque ligne de la grille et les comparer

    for line in fPlateau:
        line = line.strip() # Supprime le caractère \n (nouvelle ligne) qui est à chaque fin de ligne
        rowLengths.append(len(line)) # Sauvegarde la taille de la ligne actuelle
        if len(rowLengths) > 1 and rowLengths[i] != rowLengths[i-1]: # Si la taille change d'une ligne à une autre,
            return None, None                                        # le fichier n'est pas correctement formaté
        
        row = []
        j = 0 # Indice de la colonne qui sera reinitialisé à 0 à chaque changement de ligne
        
        for char in line:
            if char not in ['B', 'S', 'G', '_']: # Si l'un des caractères ne correspond pas
                return None, None                # le fichier n'est pas correctement formaté
            if char == '_':
                row.append(None)
            elif char == 'S':
                moutons.append((i, j)) # Sauvegarde les coordonnées du mouton dans une liste à part pour les moutons
            else:
                row.append(char)
            j = j + 1
        
        plateau.append(row)
        i = i + 1
    
    return plateau, moutons