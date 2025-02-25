import requetes as req
import networkx as nx
import matplotlib.pyplot as plt
from datetime import datetime


def show_time(start_time):
    end_time = datetime.now()
    print(" ")
    print('Durée de la requête : {}'.format(end_time - start_time))
    print(" ")

# Exemples d'acteurs
# Al Pacino
# James Woods / Roy Jones Jr

class Oracle:

    def __init__(self, G):
        self.G = G
        self.file = "None"
        self.options = None
        self.quitter = None
    
    def menu_affichage(self, title, header, options):
        len_max = len(title)
        if len(header) > len_max:
            len_max = len(header)
        for opt in options:
            if len(opt) > len_max:
                len_max = len(opt)
        print("╭" + "─" * len_max + "╮")
        print("│" + " " * ((len_max - len(title))//2) + title + " " * (((len_max - len(title)-1)//2)-len(title)%2) + " │")
        print("├" + "─" * len_max + "┤")
        print("│" + header + " " * (len_max - len(header)) + "│")
        print("├" + "─" * len_max + "┤")
        for opt in options:
            print("│" + opt + " " * (len_max - len(opt)) + "│")
        print("╰" + "─" * len_max + "╯")
    
    def start(self):
        while not self.quitter:
            self.menu()
    
    def menu(self):
        title = "SAE Graphe"
        header = " Fichier sélectionné : " + self.file
        if self.G == None:
            self.options = [" F: Choisir un jeu de données", " Q: Quitter"]
        else:
            self.options = [" F: Choisir un jeu de données", " A: Afficher le graphe", " 1: collaborateurs_communs", " 2: collaborateurs_proches" , " 3: est_proche" , " 4: distance_naive", " 5: distance", " 6: centralite acteur", " 7: centralite hollywood", " 8: eloignement max", " Q: Quitter"]
        self.menu_affichage(title, header, self.options)

        choix = input("Choix : ")
        if choix == "Q":
            self.quitter = True
        elif choix == "F":
            self.file = input("Nom du fichier : ")
            trouve = False
            try:
                fichier = open(self.file, "r", encoding="utf8")
                trouve = True
                fichier.close()
            except Exception as err:
                print("Erreur chargement de fichier", err)
            if trouve:
                self.G = req.json_vers_nx(self.file)
            else:
                self.file = "None"
        elif choix == "A":
            nx.draw(self.G, with_labels=True)
            plt.show()
        elif choix == "1":
            actor1 = input("Acteur 1 : ")
            actor2 = input("Acteur 2 : ")
            if not self.G.has_node(actor1) and not self.G.has_node(actor2):
                print("Acteur(s) inconnu(s)")
            else:
                start_time = datetime.now()
                print("Les collaborateurs communs sont : ", req.collaborateurs_communs(self.G, actor1, actor2))
                show_time(start_time)
        elif choix == "2":
            actor1 = input("Acteur : ")
            dist = input("Distance : ")
            if not self.G.has_node(actor1):
                print("Acteur inconnu")
            elif not dist.isdecimal():
                print("Distance invalide")
            else:
                dist = int(dist)
                start_time = datetime.now()
                print("Les collaborateurs proches sont : ", req.collaborateurs_proches(self.G, actor1, dist))
                show_time(start_time)
        elif choix == "3":
            actor1 = input("Acteur 1 : ")
            actor2 = input("Acteur 2 : ")
            dist = input("Distance : ")
            if not self.G.has_node(actor1) and not self.G.has_node(actor2):
                print("Acteur(s) inconnu(s)")
            elif not dist.isdecimal():
                print("Distance invalide")
            else:
                dist = int(dist)
                start_time = datetime.now()
                print("Les acteurs sont proches à distance", dist, ":", req.est_proche(self.G, actor1, actor2, dist))
                show_time(start_time)
        elif choix == "4":
            actor1 = input("Acteur 1 : ")
            actor2 = input("Acteur 2 : ")
            if not self.G.has_node(actor1) and not self.G.has_node(actor2):
                print("Acteur(s) inconnu(s)")
            else:
                start_time = datetime.now()
                print("La distance naive entre les deux acteurs : ", req.distance_naive(self.G, actor1, actor2))
                show_time(start_time)
        elif choix == "5":
            actor1 = input("Acteur 1 : ")
            actor2 = input("Acteur 2 : ")
            if not self.G.has_node(actor1) and not self.G.has_node(actor2):
                print("Acteur(s) inconnu(s)")
            else:
                start_time = datetime.now()
                print("La distance optimisée entre les deux acteurs : ", req.distance(self.G, actor1, actor2))
                show_time(start_time)
        elif choix == "6":
            actor = input("Acteur : ")
            if not self.G.has_node(actor):
                print("Acteur inconnu")
            else:
                start_time = datetime.now()
                print("La centralité de l'acteur est : ", req.centralite(self.G, actor))
                show_time(start_time)
        elif choix == "7":
            print("Calcul du centre d'Hollywood en cours...")
            start_time = datetime.now()
            print("Le centre d'Hollywood est : ", req.centre_hollywood(self.G))
            show_time(start_time)
        elif choix == "8":
            print("Calcul de l'éloignement maximal en cours...")
            start_time = datetime.now()
            print("L'éloignement maximal est : ", req.eloignement_max(self.G))
            show_time(start_time)
        else:
            print("Choix invalide")

oracle = Oracle(None)
oracle.start()
