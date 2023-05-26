# 1° Etapa
# Gerar dados geográficos
# Importar os dados do arquivo shapefile
# Criar grafo

import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_shp('shapefile/arquivo.shp')

G2 = nx.Graph()
for data in G.edges(data=True):
    G2.add_edge(data[0], data[1], weight=data[2]['comp2'])

posicao = {v:v for v in G2.nodes()}

pesos = nx.get_edge_attributes(G2, 'weight')
nx.draw_networkx_nodes(G2, posicao, node_color='r', node_size=50)
nx.draw_networkx_edges(G2, posicao)
nx.draw_networkx_edge_labels(G2, posicao, edge_labels=pesos, font_size=5)
plt.title('GRAFO INICIAL')
plt.show()

