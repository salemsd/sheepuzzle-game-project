from fltk import *
from grille import *
from jeu import *
from solveur import *
from gui import *

################################### TESTS ##############################################

p_test = [[None, 'B', None, 'B', None],
          ['B', 'B', None, None, 'G'],
          [None, 'G', 'B', None, None],
          [None, None, 'G', 'B', None],
          [None, None, None, None, None]]
m_test = [(0, 4), (1, 3), (4, 2), (4, 1)]

# #### TEST FONCTION JOUER ###
# # jouer(p_test, m_test, 'Up')
# # jouer(p_test, m_test, 'Right')

# #### TEST FONCTION VICTOIRE ###
# print(f'Victoire: {victoire(p_test, m_test)}\n')
# print(f'Nouvelle position des moutons: {m_test}\n')

# #### TEST FONCTION CHARGER ####
# plateau1, moutons1 = charger('maps/big/huge.txt')
# print(f'Plateau chargé:\n{plateau1}\n')
# print(f'Coordonnées des moutons chargés: {moutons1}\n')

# #### TEST SOLVEUR ####
# print(f'Solutions: {solutions(p_test, m_test)}')

#### TEST INTERFACE GRAPHIQUE ####
affiche_menuPrincipal()
