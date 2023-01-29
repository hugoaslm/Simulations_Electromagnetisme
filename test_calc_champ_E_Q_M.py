# ---------------------------------------------------------------------------
# NOM :         Programme principal !
# Ce programme simule un champ électrostatique
# et représente en graphique les forces exercées par les charges placées
# ALGORITHME : Voir le document
# VERSION :  0.1     09/09/2022      H.ANSELME
#                   Création de la routine
# ENTREES :         AUCUNE
# SORTIES :         AUCUNE
# LOCALES :
#   r1              Vecteur de la charge
#   r2              Vecteur du point créé
#   r               Distance vectorielle entre la charge et le point voulu
#   r_norm          Norme du vecteur r
#   r_unit_vector   Vecteur unitaire créé à partir de r
#   kc              Constante de Coulomb
#   Q               Valeur de la charge
#   E               Champ électrostatique créé par la charge Q
#   E               Norme du vecteur E
# ---------------------------------------------------------------------------

from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from calc_champ_E_Q_M import *

# ---------------------------------------------------------------------------

r1 = np.array([0, 0, 0])
r2 = np.array([1, 7, 4])
q = 5E-7
epsilon = 8.854 * 10 ** -12  # dans le vide

E = calc(r1, r2, q, epsilon)

print("E =", E, )
print("|E| =", np.linalg.norm(E), "N/C")


