# ---------------------------------------------------------------------------
# NOM :         Programme secondaire !
# Ce programme ouvre une nouvelle fenêtre
# et représente sur le graphique le champ E avec une multitude de charges
# ALGORITHME : Voir le document
# VERSION :  0.1     18/09/2022      H.ANSELME
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
#   q               Valeur de la charge
#   E               Champ électrostatique créé par la charge Q
# ---------------------------------------------------------------------------

from tkinter import *
from matplotlib import pyplot as plt
import calc_champ_E_Q_M
import numpy as np
from load_matrix import r1


# ---------------------------------------------------------------------------


class NewApp:

    def __init__(self, root):

        self.E_list = []
        window_2 = Toplevel(root)

        window_2.geometry("862x519")
        window_2.configure(bg="#3a7ff6")
        canvas = Canvas(window_2, bg="#3a7ff6", height=519, width=862, bd=0, highlightthickness=0, relief="ridge")
        canvas.place(x=0, y=0)

        background_img = PhotoImage(file=f"background_cmode.png")
        background = canvas.create_image(424.5, 259, image=background_img)

        img0 = PhotoImage(file=f"img0_cmode.png")
        b0 = Button(window_2, image=img0, borderwidth=0, highlightthickness=0, command=self.calculate, relief="flat")

        b0.place(x=73, y=272, width=180, height=55)

        img1 = PhotoImage(file=f"img1_cmode.png")
        b1 = Button(window_2, image=img1, borderwidth=0, highlightthickness=0, command=self.E_total, relief="flat")

        b1.place(x=73, y=354, width=180, height=55)

        img2 = PhotoImage(file=f"img2_cmode.png")
        b2 = Button(window_2, image=img2, borderwidth=0, highlightthickness=0, command=self.graph, relief="flat")

        b2.place(x=73, y=193, width=180, height=55)

        img3 = PhotoImage(file=f"img3_cmode.png")
        b3 = Button(window_2, image=img3, borderwidth=0, highlightthickness=0, command=self.adding_point, relief="flat")

        b3.place(x=440, y=286, width=116, height=35)

        entry0_img = PhotoImage(file=f"img_textBox0.png")
        entry0_bg = canvas.create_image(179.0, 123.5, image=entry0_img)

        self.entry0 = Entry(window_2, bd=0, bg="#eaf0ff", highlightthickness=0)

        self.entry0.place(x=80.0, y=109, width=198.0, height=27)

        entry1_img = PhotoImage(file=f"img_textBox1.png")
        entry1_bg = canvas.create_image(498.0, 107.5, image=entry1_img)

        self.entry1 = Entry(window_2, bd=0, bg="#eaf0ff", highlightthickness=0)

        self.entry1.place(x=399.0, y=93, width=198.0, height=27)

        entry2_img = PhotoImage(file=f"img_textBox2.png")
        entry2_bg = canvas.create_image(498.0, 146.5, image=entry2_img)

        self.entry2 = Entry(window_2, bd=0, bg="#eaf0ff", highlightthickness=0)

        self.entry2.place(x=399.0, y=132, width=198.0, height=27)

        entry3_img = PhotoImage(file=f"img_textBox3.png")
        entry3_bg = canvas.create_image(498.0, 185.5, image=entry3_img)

        self.entry3 = Entry(window_2, bd=0, bg="#eaf0ff", highlightthickness=0)

        self.entry3.place(x=399.0, y=171, width=198.0, height=27)

        entry4_img = PhotoImage(file=f"img_textBox4.png")
        entry4_bg = canvas.create_image(498.0, 233.5, image=entry4_img)

        self.entry4 = Entry(window_2, bd=0, bg="#eaf0ff", highlightthickness=0)

        self.entry4.place(x=399.0, y=219, width=198.0, height=27)

        window_2.mainloop()

    def graph(self):

        # Initialisation du graphe

        self.ax = plt.axes(projection='3d')
        self.ax.set_xlim(-20, 20)
        self.ax.set_ylim(-20, 20)
        self.ax.set_zlim(-20, 20)
        self.ax.set_xlabel("X label")
        self.ax.set_ylabel("Y label")
        self.ax.set_zlabel("Z label")
        plt.show()

    def calculate(self):

        # Initialisation des données
        r2 = np.array([float(self.entry1.get()), float(self.entry2.get()), float(self.entry3.get())])
        q = float(self.entry4.get())
        epsilon = 8.854 * 10 ** -12  # dans le vide

        # Initialisation de la liste E
        self.E_array = []

        # Indice pour le nombre de charges
        Num = int(self.entry0.get()) - 1

        # Condition sur l'indice
        if Num == 0:
            x2 = calc_champ_E_Q_M.calc(r1[0], r2, q, epsilon)
            self.E_array.append(x2)

        # Boucle calculant tous les champs E
        for i in range(0, Num):
            x = calc_champ_E_Q_M.calc(r1[i], r2, q, epsilon)
            self.E_array.append(x)

        print('Done')

    def adding_point(self):

        # Ajouter un point sur le graph
        self.ax.scatter(float(self.entry1.get()), float(self.entry2.get()), float(self.entry3.get()), c='orange', s=20)

    def E_total(self):

        # Faire la somme de tous les champs E de la liste
        self.E_tot = sum(self.E_array)
        print(self.E_tot)

        # Dessiner le champ E
        self.ax.quiver(float(self.entry1.get()), float(self.entry2.get()), float(self.entry3.get()),
                       self.E_tot[0], self.E_tot[1], self.E_tot[2], color='red')

        # Changer les limites du graphe si la force dépasse les limites initiales

        max_e = np.amax(self.E_tot)
        if max_e > 20:
            self.ax.set_xlim(-(max_e - 20), max_e + 20)
            self.ax.set_ylim(-(max_e - 20), max_e + 20)
            self.ax.set_zlim(-(max_e - 20), max_e + 20)

        # Changer les limites du graphe si la force dépasse les limites initiales

        min_e = np.amin(self.E_tot)
        if min_e < -20:
            self.ax.set_xlim(-(min_e - 20), min_e + 20)
            self.ax.set_ylim(-(min_e - 20), min_e + 20)
            self.ax.set_zlim(-(min_e - 20), min_e + 20)
