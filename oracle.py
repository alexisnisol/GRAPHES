import requetes as req
import networkx as nx
import matplotlib.pyplot as plt
from datetime import datetime


G = req.json_vers_nx("extrait.txt")
#nx.draw(G, with_labels=True)
#plt.show()
print(req.collaborateurs_communs(G, "Marisa Berenson", "Mel Gibson"))

