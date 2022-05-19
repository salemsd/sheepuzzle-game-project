from gui import *

################################### TESTS ##############################################

p_test = [[None, 'B', None, 'B', None],
          ['B', 'B', None, None, 'G'],
          [None, 'G', 'B', None, None],
          [None, None, 'G', 'B', None],
          [None, None, None, None, None]]
m_test = [(1, 3), (0, 4), (4, 2), (4, 1)]
m_test1 = [(0, 3), (0, 2), (0, 9), (0, 1), (1, 3), (6, 4), (6, 2), (3, 4)]

# #### TEST FONCTION JOUER ###
# jouer(p_test, m_test, 'Up')
# jouer(p_test, m_test, 'Right')

# # #### TEST FONCTION VICTOIRE ###
# print(f'Victoire: {victoire(p_test, m_test)}\n')
# print(f'Nouvelle position des moutons: {m_test}\n')

# #### TEST FONCTION CHARGER ####
# plateau1, moutons1 = charger('maps/big/huge.txt')
# print(f'Plateau chargé:\n{plateau1}\n')
# print(f'Coordonnées des moutons chargés: {moutons1}\n')

#### TEST SOLVEUR PROFONDEUR ####
sol1 = solutions(p_test, m_test)
print(f'Solutions: {sol1}')
if sol1 is not None:
    print(f'Longueur: {len(sol1)}')
jouer_sol(p_test, m_test, sol1)
print(f'Solution marche: {victoire(p_test, m_test)}')

# #### TEST SOLVEUR LARGEUR ####
# sol2 = solutions_lrg(p_test, m_test)
# print(f'Solutions: {sol2}')
# if sol2 is not None:
#     print(f'Longueur: {len(sol2)}')
# jouer_sol(p_test, m_test, sol2)
# print(f'Solution marche: {victoire(p_test, m_test)}')

### TEST INTERFACE GRAPHIQUE ####
# affiche_menuPrincipal()
