def charger(fichier):
    """
    Charge la grille en fichier texte vers une liste
    :param str fichier: Le chemin du fichier à charger
    :return: La grille du jeu et la liste des moutons
    """
    fPlateau = open(fichier, 'r')
    plateau = []
    moutons = []
    i = 0  # Indice de la ligne
    # Liste pour sauvegarder la taille de chaque ligne de la grille et les comparer
    rowLengths = []

    for line in fPlateau:
        # Supprime le caractère \n (nouvelle ligne) qui est à chaque fin de ligne
        line = line.strip()
        # Sauvegarde la taille de la ligne actuelle
        rowLengths.append(len(line))
        # Si la taille change d'une ligne à une autre,
        if len(rowLengths) > 1 and rowLengths[i] != rowLengths[i-1]:
            # le fichier n'est pas correctement formaté
            return None, None

        row = []
        j = 0  # Indice de la colonne qui sera reinitialisé à 0 à chaque changement de ligne

        for char in line:
            # Si l'un des caractères ne correspond pas, alors le fichier n'est pas correctement formaté
            if char not in ['B', 'S', 'G', '_']:
                return None, None
            if char == '_':
                row.append(None)
            elif char == 'S':
                row.append(None)
                # Sauvegarde les coordonnées du mouton dans une liste à part pour les moutons
                moutons.append((i, j))
            else:
                row.append(char)
            j = j + 1

        plateau.append(row)
        i = i + 1

    return plateau, moutons
