import requetes as req
import networkx as nx
import matplotlib.pyplot as plt
from datetime import datetime


def show_time(start_time):
    end_time = datetime.now()
    print('Duration Q1: {}'.format(end_time - start_time))


G = req.json_vers_nx("data_100.txt")
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
nx.draw(G9)

print(req.centralite(G9, 4))
print()