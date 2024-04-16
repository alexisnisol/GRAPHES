import networkx as nx
import matplotlib.pyplot as plt
from datetime import datetime

def show_time(start_time):
    end_time = datetime.now()
    print('Duration Q1: {}'.format(end_time - start_time))


# Q1
start_time = datetime.now()

def from_json(nom_fichier):
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
    acteurs = film['cast']
    for i in range(len(acteurs)):
        acteurs[i] = acteurs[i].strip('[]')
    return film


def json_vers_nx(chemin):
    data = from_json(chemin)
    G = nx.Graph()
    for film in data:
        acteurs = film['cast']
        for i in range(len(acteurs)):
            for j in range(i+1, len(acteurs)):
                G.add_edge(acteurs[i], acteurs[j])
    return G

show_time(start_time)

# Q2
start_time = datetime.now()

def collaborateurs_communs(G,u,v):
    print("TEST ", G)

show_time(start_time)

# Q3
start_time = datetime.now()

def collaborateurs_proches(G,u,k):
    ...
def est_proche(G,u,v,k=1):
    ...
def distance_naive(G,u,v):
    ...
def distance(G,u,v):
    ...

show_time(start_time)

# Q4
start_time = datetime.now()

def centralite(G,u):
    ...
def centre_hollywood(G):
    ...

show_time(start_time)

# Q5
start_time = datetime.now()

def eloignement_max(G:nx.Graph):
    ...

show_time(start_time)

# Bonus
start_time = datetime.now()

def centralite_groupe(G,S):
    ...

show_time(start_time)