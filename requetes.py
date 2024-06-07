import networkx as nx
from collections import deque

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
    if u not in G.nodes or v not in G.nodes:
        return None
    return set(G[u]) & set(G[v])

# Q3
def collaborateurs_proches(G,u,k):
    """Fonction renvoyant l'ensemble des acteurs à distance au plus k de l'acteur u dans le graphe G. La fonction renvoie None si u est absent du graphe.
    
    Parametres:
        G: le graphe
        u: le sommet de départ
        k: la distance depuis u
    """
    if u not in G.nodes:
        print(u,"est un illustre inconnu")
        return None
    collaborateurs = set()
    collaborateurs.add(u)
    for i in range(k):
        collaborateurs_directs = set() 
        for c in collaborateurs:
            for voisin in G.adj[c]:
                if voisin not in collaborateurs:
                    collaborateurs_directs.add(voisin)
        collaborateurs = collaborateurs.union(collaborateurs_directs)
    return collaborateurs

def est_proche(G, u,v,k=1):
    """Fonction renvoyant True si l'acteur v est à distance au plus k de l'acteur u dans le graphe G. La fonction renvoie False sinon.

    Args:
        G (nx.Graph): le graphe
        u (str): un acteur
        v (str): un acteur
        k (int, optional): la distance maximale. Defaults to 1.

    Returns:
        bool: True si v est à distance au plus k de u, False sinon
    """
    if u not in G.nodes or v not in G.nodes:
        return None
    return v in collaborateurs_proches(G, u, k)
    
def distance_naive(G,u,v):
    """Fonction renvoyant la distance entre les acteurs u et v dans le graphe G. La fonction renvoie -1 si u et v ne sont pas connectés.

    Args:
        G (nx.Graph): le graphe
        u (str): un acteur
        v (str): un acteur

    Returns:
        int: la distance entre u et v
    """
    if u not in G.nodes or v not in G.nodes:
        return None
    dist = 1
    dist_max = len(G.nodes())
    for _ in range(dist_max):
        proche = est_proche(G, u, v, dist)
        if proche:
            return dist
        dist += 1
    return -1

def distance(G,u,v):
    """Fonction renvoyant la distance entre les acteurs u et v dans le graphe G. La fonction renvoie -1 si u et v ne sont pas connectés.

    Args:
        G (nx.Graph): le graphe
        u (str): un acteur
        v (str): un acteur

    Returns:
        int: la distance entre u et v
    """
    k = len(G.nodes())
    if u not in G.nodes or v not in G.nodes:
        print(u,"est un illustre inconnu")
        return None
    collaborateurs = set()
    collaborateurs.add(u)
    for i in range(k):
        collaborateurs_directs = set()
        for c in collaborateurs:
            for voisin in G.adj[c]:
                if v == voisin:
                    return i+1
                if voisin not in collaborateurs:
                    collaborateurs_directs.add(voisin)
        collaborateurs = collaborateurs.union(collaborateurs_directs)
    return -1

# Fonction annexe pour centraliteV1
def cherche_acteur_mini(acteurs):
    """Fonction renvoyant l'acteur non visité le plus proche du graphe G

    Args:
        visite (set): les acteurs déjà visités

    Returns:
        str: l'acteur le plus proche
    """
    acteur_mini = None
    distance_mini = None
    for acteur, dist in acteurs.items():
        if distance_mini is None or dist < distance_mini:
            acteur_mini = acteur
            distance_mini = dist
    return acteur_mini

# Q4
def centraliteV1(t,u):
    """Renvoie la centralité de l'acteur u dans le graphe G version naïve

    Args:
        t (nx.Graph): le graphe
        u (str): un acteur

    Returns:
        int: la distance maximal avec un autre acteur dans le graph
    """
    if u not in t.nodes:
        return None
    G = t.copy() #A SUPPRIMER
    G.nodes[u]['distance_max'] = 0
    distance_max = 0
    acteur_actuel = u
    # visite contient les acteurs déjà parcourus
    visite = set()
    # acteurs_mini contient les acteurs  qui vont être parcourus
    acteurs_mini = dict()
    acteurs_mini[u] = 0
    # parcours des noeuds du graphe, O(|V|) avec V l'ensemble des noeuds
    while len(visite) < len(G.nodes):
        # parcours des voisins du noeud actuel, O(|E|) avec E l'ensemble des arêtes adjacentes
        for voisin in G.adj[acteur_actuel]:
            if voisin not in visite:
                if 'distance_max' not in G.nodes[voisin]:
                    G.nodes[voisin]['distance_max'] = G.nodes[acteur_actuel]['distance_max'] + 1
                    acteurs_mini[voisin] = G.nodes[voisin]['distance_max']
        visite.add(acteur_actuel) # O(1)
        # on retire l'acteur actuel de la liste des acteurs à parcourir
        acteurs_mini.pop(acteur_actuel) # O(1)
        # on actualise la distance maximale
        if distance_max < G.nodes[acteur_actuel]['distance_max']:
            distance_max = G.nodes[acteur_actuel]['distance_max']
        # on cherche l'acteur le plus proche, O(|E|) avec E l'ensemble des arêtes
        acteur_actuel = cherche_acteur_mini(acteurs_mini)  #A SUPPRIMER
    return distance_max



def centraliteV2(t,u):
    """Renvoie la centralité de l'acteur u dans le graphe G, version optimisée qui utilise un algorithme de parcours en largeur

    Args:
        t (nx.Graph): le graphe
        u (str): un acteur

    Returns:
        int: la distance maximal avec un autre acteur dans le graph
    """
    if u not in t.nodes:
        return None
    G = t.copy()
    G.nodes[u]['distance_max'] = 0
    distance_max = 0
    # visite contient les acteurs déjà parcourus
    visite = set()
    sommets_a_explorer = [u]
    # parcours des noeuds du graphe, O(|V|) avec V l'ensemble des noeuds
    while (len(sommets_a_explorer)>0):
        acteur_actuel = sommets_a_explorer.pop(0)
        visite.add(acteur_actuel)
        # parcours des voisins du noeud actuel, O(|E|) avec E l'ensemble des arêtes adjacentes
        for voisin in G.adj[acteur_actuel]:
            if voisin not in visite:
                if 'distance_max' not in G.nodes[voisin]:
                    G.nodes[voisin]['distance_max'] = G.nodes[acteur_actuel]['distance_max'] + 1
                visite.add(voisin) # O(1)
                sommets_a_explorer.append(voisin)

        # on actualise la distance maximale
        if distance_max < G.nodes[acteur_actuel]['distance_max']:
            distance_max = G.nodes[acteur_actuel]['distance_max']

    return distance_max

def centraliteV3(G, u):
    """Renvoie la centralité de l'acteur u dans le graphe G, Version 3 qui utilise un algorithme de parcours en largeur sans copie du graphe

    Args:
        G (nx.Graph): le graphe
        u (str): un acteur

    Returns:
        int: la distance maximal avec un autre acteur dans le graph
    """
    if u not in G.nodes:
        return None
    distance_max = 0
    distances = {u: 0}
    # visite contient les acteurs déjà parcourus
    visite = set()
    sommets_a_explorer = [u]
    # parcours des noeuds du graphe, O(|V|) avec V l'ensemble des noeuds
    while sommets_a_explorer:
        acteur_actuel = sommets_a_explorer.pop(0)
        visite.add(acteur_actuel)
        # parcours des voisins du noeud actuel, O(|E|) avec E l'ensemble des arêtes adjacentes
        for voisin in G.adj[acteur_actuel]:
            if voisin not in visite:
                distances[voisin] = distances[acteur_actuel] + 1
                visite.add(voisin) # O(1)
                sommets_a_explorer.append(voisin)

        # on actualise la distance maximale
        if distance_max < distances[acteur_actuel]:
            distance_max = distances[acteur_actuel]

    return distance_max

def centralite(G, u):
    """Renvoie la centralité de l'acteur u dans le graphe G, Version 4 semblable à la version 3 mais avec une deque : plus rapide pour les pop(0) et retire des variables inutiles

    Args:
        G (nx.Graph): le graphe
        u (str): un acteur

    Returns:
        int: la distance maximal avec un autre acteur dans le graph
    """
    if u not in G.nodes:
        return None
    distance_max = 0
    # visite contient les acteurs déjà parcourus
    visite = {u: 0}
    sommets_a_explorer = deque([u])
    # parcours des noeuds du graphe, O(|V|) avec V l'ensemble des noeuds
    while sommets_a_explorer:
        acteur_actuel = sommets_a_explorer.popleft()
        # parcoure des voisins du noeud actuel, O(|E|) avec E l'ensemble des arêtes adjacentes
        for voisin in G.adj[acteur_actuel]:
            if voisin not in visite:
                visite[voisin] = visite[acteur_actuel] + 1
                if visite[voisin] > distance_max:
                    distance_max = visite[voisin]
                sommets_a_explorer.append(voisin)

    return distance_max

# O( |V| * 2 * |E| ) avec V l'ensemble des noeuds et E l'ensemble des arêtes


def centre_hollywood(G, debug=False):
    """retourne l'acteur le plus au centre d'hollywood

    Args:
        G (nx.Graph): le graph des acteurs

    Returns:
        str: l'acteur le plus proche
    """
    minim = None
    acteur_max = None
    i = 0
    len_act = len(G.nodes)
    for acteur in G.nodes:
        if debug:
            print(i, "/", len_act,":", acteur)
        centralite_act = centralite(G, acteur)
        if acteur_max is None or minim > centralite_act:
            acteur_max = acteur
            minim = centralite_act
        i += 1
    return acteur_max

# Q5
def eloignement_max(G:nx.Graph):
    """La distance maximale entre 2 paires quelquonques du graphe

    Args:
        G (nx.Graph): le graphe
    
    Returns:
        int : La distance maximale entre 2 paires quelquonques du graphe
    """
    maxim = 0
    acteur_max = None
    for acteur in G.nodes:
        centralite_act = centralite(G, acteur)
        if maxim < centralite_act:
            maxim = centralite_act
            acteur_max = acteur
    return acteur_max

# Bonus
def centralite_groupe(G,S):
    ...
