# ---------------------------------------------------------------------------
# NOM :         Programme principal !
# Ce programme simule un champ électrostatique
# et représente en graphique le champ E généré par les charges placées
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
#   Q               Valeur de la charge
#   E               Champ électrostatique créé par la charge Q
# ---------------------------------------------------------------------------

from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
import window
import calc_champ_E_Q_M

# ---------------------------------------------------------------------------


class MyApp:

    def __init__(self):

        self.status = 0

        # Initialisation de la fenêtre
        self.window = Tk()
        self.window.geometry("862x519")
        self.window.configure(bg="#3a7ff6")

        # Fond bleu en arrière plan
        self.canvas = Canvas(self.window, bg="#603af6", height=519, width=862, bd=0,
                             highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)

        # Image en arrière plan
        self.background_img = PhotoImage(file=f"background.png")
        self.background = self.canvas.create_image(436.5, 259, image=self.background_img)

        # Zone de texte coordonnée en x pour la charge
        self.entry0_img = PhotoImage(file=f"img_textBox0.png")
        self.entry0_bg = self.canvas.create_image(371.0, 107.5, image=self.entry0_img)
        self.entry0 = Entry(bd=0, bg="#eaf0ff", highlightthickness=0)
        self.entry0.place(x=272.0, y=93, width=198.0, height=27)

        # Zone de texte coordonnée en y pour la charge
        self.entry1_img = PhotoImage(file=f"img_textBox1.png")
        self.entry1_bg = self.canvas.create_image(371.0, 146.5, image=self.entry1_img)
        self.entry1 = Entry(bd=0, bg="#eaf0ff", highlightthickness=0)
        self.entry1.place(x=272.0, y=132, width=198.0, height=27)

        # Zone de texte coordonnée en z pour la charge
        self.entry2_img = PhotoImage(file=f"img_textBox2.png")
        self.entry2_bg = self.canvas.create_image(371.0, 185.5, image=self.entry2_img)
        self.entry2 = Entry(bd=0, bg="#eaf0ff", highlightthickness=0)
        self.entry2.place(x=272.0, y=171, width=198.0, height=27)

        # Zone de texte valeur de q pour la charge
        self.entry3_img = PhotoImage(file=f"img_textBox3.png")
        self.entry3_bg = self.canvas.create_image(371.0, 233.5, image=self.entry3_img)
        self.entry3 = Entry(bd=0, bg="#eaf0ff", highlightthickness=0)
        self.entry3.place(x=272.0, y=219, width=198.0, height=27)

        # Zone de texte coordonnée en x pour le point
        self.entry4_img = PhotoImage(file=f"img_textBox4.png")
        self.entry4_bg = self.canvas.create_image(691.0, 107.5, image=self.entry4_img)
        self.entry4 = Entry(bd=0, bg="#eaf0ff", highlightthickness=0)
        self.entry4.place(x=592.0, y=93, width=198.0, height=27)

        # Zone de texte coordonnée en y pour le point
        self.entry5_img = PhotoImage(file=f"img_textBox5.png")
        self.entry5_bg = self.canvas.create_image(691.0, 146.5, image=self.entry5_img)
        self.entry5 = Entry(bd=0, bg="#eaf0ff", highlightthickness=0)
        self.entry5.place(x=592.0, y=132, width=198.0, height=27)

        # Zone de texte coordonnée en z pour le point
        self.entry6_img = PhotoImage(file=f"img_textBox6.png")
        self.entry6_bg = self.canvas.create_image(691.0, 185.5, image=self.entry6_img)
        self.entry6 = Entry(bd=0, bg="#eaf0ff", highlightthickness=0)
        self.entry6.place(x=592.0, y=171, width=198.0, height=27)

        # Zone de texte pour le point
        self.entry7_img = PhotoImage(file=f"img_textBox7.png")
        self.entry7_bg = self.canvas.create_image(691.0, 233.5, image=self.entry7_img)
        self.entry7 = Entry(bd=0, bg="#eaf0ff", highlightthickness=0)
        self.entry7.place(x=592.0, y=219, width=198.0, height=27)

        # Initialisation des listes pour les calculs
        self.E_list = []
        self.r1m = []
        self.r2m = []

        # Création des composants
        self.create_widgets()

    def create_widgets(self):

        # Initialisation des composants
        self.create_calc_button()
        self.create_sketch_button()
        self.create_add_button()
        self.create_graph_button()
        self.create_superposition_button()
        self.create_multiple_button()

    def next_step(self):
        self.status = self.status + 1

    def graph(self):

        # Initialisation du graphe
        fig = plt.figure()
        self.ax = fig.add_subplot(111, projection='3d')
        # self.ax = plt.axes(projection='3d')
        # self.event = fig.canvas.mpl_connect('button_press_event', self.mouse_event)
        self.ax.set_xlim(-20, 20)
        self.ax.set_ylim(-20, 20)
        self.ax.set_zlim(-20, 20)
        self.ax.set_xlabel("X label")
        self.ax.set_ylabel("Y label")
        self.ax.set_zlabel("Z label")
        plt.show()

    def add_charge(self):

        self.ax.scatter(float(self.entry0.get()), float(self.entry1.get()), float(self.entry2.get()), c='blue',
                        s=20, label='Charge')
        self.ax.legend()

        x1 = float(self.entry0.get()), float(self.entry1.get()), float(self.entry2.get())
        self.r1m.append(x1)

        self.number_of_colors = 12
        self.color = ["#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)]) for i in
                      range(self.number_of_colors)]

    def add_point(self, event):

        # Ajouter un point sur le graphe
        self.ax.scatter(float(self.entry4.get()), float(self.entry5.get()), float(self.entry6.get()), c='orange', s=20)

        x2 = float(self.entry4.get()), float(self.entry5.get()), float(self.entry6.get())
        self.r2m.append(x2)

        self.next_step()
        print(self.status)

    def calc(self):

        # Calculer le champ électrostatique
        r1 = np.array([float(self.entry0.get()), float(self.entry1.get()), float(self.entry2.get())])
        r2 = np.array([float(self.entry4.get()), float(self.entry5.get()), float(self.entry6.get())])
        r = r2 - r1
        q = float(self.entry3.get())
        epsilon = 8.854 * 10 ** -12  # dans le vide

        self.E = calc_champ_E_Q_M.calc(r1, r2, q, epsilon)

        self.E_list.append(self.E)

        print("E =", self.E, )
        print("|E| =", np.linalg.norm(self.E), "N/C")
        print(r1, r2, self.E)
        print(self.status)
        print(self.E_list)

    def calc_vector_np(self):

        for i in range(1, 25):
            if self.status == i:
                self.coloring = self.color[i]

        # Tracer la force exercée par la charge q
        self.ax.quiver(float(self.entry4.get()), float(self.entry5.get()), float(self.entry6.get()),
                       self.E[0], self.E[1], self.E[2], color=self.coloring)

        # Changer les limites du graphe si la force dépasse les limites initiales
        max_e = np.amax(self.E)
        if max_e > 20:
            self.ax.set_xlim(-(max_e - 20), max_e + 20)
            self.ax.set_ylim(-(max_e - 20), max_e + 20)
            self.ax.set_zlim(-(max_e - 20), max_e + 20)

        # Changer les limites du graphe si la force dépasse les limites initiales
        min_e = np.amin(self.E)
        if min_e < -20:
            self.ax.set_xlim(-(min_e - 20), min_e + 20)
            self.ax.set_ylim(-(min_e - 20), min_e + 20)
            self.ax.set_zlim(-(min_e - 20), min_e + 20)

    def th_superposition(self):

        self.E_tot = self.E_list[0] + self.E_list[1]
        print(self.E_tot)

        self.ax.quiver(float(self.entry4.get()), float(self.entry5.get()), float(self.entry6.get()),
                       self.E_tot[0], self.E_tot[1], self.E_tot[2], color='red')

    def open_new_window(self):

        window.NewApp(self.window)

    def create_calc_button(self):

        # Créer le bouton pour calculer le champ électrostatique
        self.img0 = PhotoImage(file=f"img1.png")
        b0 = Button(image=self.img0, borderwidth=0, highlightthickness=0, command=self.calc, relief="flat")
        b0.place(x=327, y=343, width=180, height=55)

    def create_sketch_button(self):

        # Créer le bouton pour tracer la force exercée par q
        self.img1 = PhotoImage(file=f"img2.png")
        b1 = Button(image=self.img1, borderwidth=0, highlightthickness=0, command=self.calc_vector_np, relief="flat")

        b1.place(x=554, y=417, width=180, height=55)

    def create_graph_button(self):

        # Créer le bouton pour tracer la charge
        self.img_c = PhotoImage(file=f"img3.png")
        b1c = Button(image=self.img_c, borderwidth=0, highlightthickness=0, command=self.graph, relief="flat")

        b1c.place(x=554, y=343, width=180, height=55)

    def create_add_button(self):

        # Créer le bouton pour ajouter une charge
        self.img2 = PhotoImage(file=f"img4.png")
        b2 = Button(image=self.img2, borderwidth=0, highlightthickness=0, command=self.add_charge, relief="flat")
        b2.place(x=313, y=268, width=116, height=35)

        # Créer le bouton pour ajouter un point
        self.img3 = PhotoImage(file=f"img5.png")
        b3 = Button(image=self.img3, borderwidth=0, highlightthickness=0, relief="flat")
        b3.place(x=633, y=266, width=116, height=35)

        b3.bind("<Button-1>", self.add_point)

    def create_superposition_button(self):

        # Créer le bouton pour calculer le champ E total
        self.img_tot = PhotoImage(file=f"img0.png")
        bt = Button(image=self.img_tot, borderwidth=0, highlightthickness=0, command=self.th_superposition,
                    relief="flat")
        bt.place(x=327, y=417, width=180, height=55)

    def create_multiple_button(self):

        # Passer au mode charges multiples
        self.img6 = PhotoImage(file=f"img6.png")
        b6 = Button(image=self.img6, borderwidth=0, highlightthickness=0, command=self.open_new_window, relief="flat")

        b6.place(x=77, y=398, width=38, height=38)


app = MyApp()
app.window.mainloop()
