import requetes as req
import networkx as nx
import matplotlib.pyplot as plt
from datetime import datetime


def show_time(start_time):
    end_time = datetime.now()
    print(" ")
    print('Durée de la requête : {}'.format(end_time - start_time))
    print(" ")


G = req.json_vers_nx("data_10000.txt")
#nx.draw(G, with_labels=True)
#plt.show()
#print(req.collaborateurs_communs(G, "Marisa Berenson", "Mel Gibson"))

#print(req.collaborateurs_proches(G, "James Woods", 1))

#print(req.est_proche(G, "James Woods", "Bruno Kirby", 4))

start_time = datetime.now()
print(req.distance_naive(G, "James Woods", "Roy Jones Jr"))
show_time(start_time)

start_time = datetime.now()
print(req.distance(G, "James Woods", "Roy Jones Jr"))
show_time(start_time)

G9 = nx.Graph()
G9.add_edges_from([(1,4),(4,2),(4,3),(4,5),(5,6),(2,7),(6,8),(8,9),(7,10),(9,4)])

#print("Centralité de 4", req.centralite(G9, 4))
#print("Centralité de 10", req.centralite(G9, 10))
#print(req.centre_hollywood(G))
print(req.eloignement_max(G9))



start_time = datetime.now()
print(req.centraliteV3(G, "Al Pacino"))
#print(req.centralite_aaa(G, "Walter Matthau"))
show_time(start_time)



#nx.draw(G9, with_labels=True)
#plt.show()

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
        print("│" + " " * ((len_max - len(title))//2) + title + " " * (((len_max - len(title))//2)-len(title)%2) + " │")
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
            self.options = [" F: Choisir un jeu de données", " 1: collaborateurs_communs", " 2: collaborateurs_proches" , " 3: est_proche" , " 4: distance_naive", " 5: distance", " 6: centralite acteur", "7: centralite hollywood", "8: eloignement max", " Q: Quitter"]
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
        else:
            print("Choix invalide")

oracle = Oracle(None)
#oracle.start()

#print(req.distance_naive(self.G, "James Woods", "Roy Jones Jr"))