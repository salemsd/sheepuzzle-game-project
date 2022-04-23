from fltk import *
from grille import *
from jeu import *

# Membres du groupe
# SAOUDI Salem - TP11
# JIA Siyuan - TP11
# Thilelli - TP12

p_test = [[None, 'B', None, 'B', None],
          ['B', 'B', None, None, 'G'],
          [None, 'G', 'B', 'B', None],
          [None, None, 'G', None, None],
          [None, None, None, None, None]]
m_test = [(0, 4), (1, 3), (4, 2), (4, 1)]
d_test = 'Up'
d_test2 = 'Right'

jouer(p_test, m_test, d_test)

jouer(p_test, m_test, d_test2)

print(victoire(p_test, m_test))
print(m_test)

aplato, akraren = charger('maps/wide/wide4.txt')
print(aplato)
print(akraren)
