import networkx as nx
import matplotlib.pyplot as plt

# Q1
def from_json(nom_fichier):
    """Renvoie le contenu d'un fichier json sous forme de liste de dictionnaires

    Args:
        nom_fichier (str): le nom du fichier json

    Returns:
        list: la liste de dictionnaires
    """
    liste_csv = []
    try:
        file = open(nom_fichier, "r", encoding="utf8")
        for line in file:
            line = line.split("\n")[0]
            liste_csv.append(formattage(eval(line)))
        file.close()
    except Exception as err:
        print(err)
    return liste_csv


def formattage(film):
    """formatte le nom des acteurs des films

    Args:
        film (Dict): le film

    Returns:
        dict: le film avec les noms formattés
    """
    acteurs = film['cast']
    for i in range(len(acteurs)):
        acteurs[i] = acteurs[i].strip('[]')
    return film


def json_vers_nx(chemin):
    """transforme un fichier json en graphe

    Args:
        chemin (str): le chemin vers le fichier json

    Returns:
        nx.Graph: le graphe
    """
    data = from_json(chemin)
    G = nx.Graph()
    for film in data:
        acteurs = film['cast']
        for i in range(len(acteurs)):
            for j in range(i+1, len(acteurs)):
                G.add_edge(acteurs[i], acteurs[j])
    return G

# Q2
def collaborateurs_communs(G,u,v):
    '''
    Renvoie l'ensemble des collaborateurs communs de u et v dans G
    Args:
        G (nx.Graph) : Le graphe
        u (str) : un acteur (un sommet du graphe)
        v (str) : un acteur (un sommet du graphe)
    Returns:
        set : l'ensemble des collaborateurs
    '''
    return set(G[u]) & set(G[v])

# Q3
def collaborateurs_proches(G,u,k):
    ...
def est_proche(G,u,v,k=1):
    ...
def distance_naive(G,u,v):
    ...
def distance(G,u,v):
    ...

# Q4
def centralite(G,u):
    ...
def centre_hollywood(G):
    ...

# Q5
def eloignement_max(G:nx.Graph):
    ...

# Bonus
def centralite_groupe(G,S):
    ...