# 2° Etapa
# Diferenciar vias de mão dupla e mão única
# Tranformar o grafo em um Dígrafo

import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_shp('shapefile/arquivo.shp')

weighted_G = nx.DiGraph()
for data in G.edges(data=True):
   if data[2]['other_tags'] is not None:
      if '"oneway"=>"yes"' in data[2]['other_tags']: 
         weighted_G.add_edge(data[0], data[1], weight=data[2]['comp2'])
      else:
         weighted_G.add_edge(data[0], data[1], weight=data[2]['comp2'])
         weighted_G.add_edge(data[1], data[0], weight=data[2]['comp2'])

pos = {v:v for v in weighted_G.nodes()}

nx.draw_networkx(weighted_G, pos, node_size=30, with_labels=False, width=0.5)

plt.show()

