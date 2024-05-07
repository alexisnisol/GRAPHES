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