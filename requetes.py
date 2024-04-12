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
            acteurs[i] = acteurs[i].strip('[]')
    return data


def genere_graph(data):
    G = nx.Graph()
    for film in data:
        acteurs = film['cast']
        for i in range(len(acteurs)):
            for j in range(i+1, len(acteurs)):
                G.add_edge(acteurs[i], acteurs[j])
    return G


liste_json = from_json("extrait.txt")
liste_json = formattage(liste_json)
G = genere_graph(liste_json)
nx.draw(G, with_labels=True)
plt.show()