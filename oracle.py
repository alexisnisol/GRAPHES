import requetes as req
import networkx as nx
import matplotlib.pyplot as plt
from datetime import datetime


def show_time(start_time):
    end_time = datetime.now()
    print('Duration Q1: {}'.format(end_time - start_time))


G = req.json_vers_nx("data.txt")
#nx.draw(G, with_labels=True)
#plt.show()
print(req.collaborateurs_communs(G, "Marisa Berenson", "Mel Gibson"))

