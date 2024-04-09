import networkx as nx
import matplotlib.pyplot as plt

def from_json(nom_fichier):
    liste_csv = []
    try:
        file = open(nom_fichier, "r", encoding="utf8")
        for line in file:
            line = line.split("\n")[0]
            liste_csv.append(eval(line))
        file.close()
    except Exception as err:
        print(err)
    return liste_csv


def formattage(data):
    for film in data:
        acteurs = film['cast']
        for i in range(len(acteurs)):
            acteur = acteurs[i].strip('[]')
            acteurs[i] = acteur



def genere_graph(data):
    G = nx.Graph()
    for film in data:
        acteurs = film['cast']
        for i in range(len(acteurs)):
            for j in range(i+1, len(acteurs)):
                G.add_edge(acteurs[i], acteurs[j])
    return G







json = from_json("extrait.txt")
json = formattage(json)
genere_graph(json)

plt.show()