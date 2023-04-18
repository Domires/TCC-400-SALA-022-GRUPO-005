# importar bibliotecas
import networkx as nx
import matplotlib.pyplot as plt

# Importar arquivo shapefile
G = nx.read_shp('shapefile/arquivo.shp')

# Criar grafo direcionado
weighted_G = nx.DiGraph()
for data in G.edges(data=True):
   # Verificar se a tag 'oneway' existe
   if data[2]['other_tags'] is not None:
      # Verificar se a tag 'oneway' é 'yes' => direção única
      if '"oneway"=>"yes"' in data[2]['other_tags']: 
         weighted_G.add_edge(data[0], data[1], weight=data[2]['comp2'])
      else:
         weighted_G.add_edge(data[0], data[1], weight=data[2]['comp2'])
         weighted_G.add_edge(data[1], data[0], weight=data[2]['comp2'])

# Criar arquivo txt com os dados do grafo
f = open("arestas.txt", "a")
f.write(str(weighted_G.edges(data=True)))
f.close()
f = open("vertices.txt", "a")
f.write(str(weighted_G.nodes()))
f.close()

# Criar dicionário de posições
pos = {v:v for v in weighted_G.nodes()}

# nx.draw_networkx_nodes(weighted_G, pos, node_size=100, node_color='r')
# nx.draw_networkx_edges(weighted_G, pos)
# labels = nx.get_edge_attributes(weighted_G, 'weight')
# nx.draw_networkx_edge_labels(weighted_G, pos, edge_labels=labels)

# Desenhar grafo
nx.draw_networkx(weighted_G, pos, node_size=10, with_labels=False, width=0.2)

# Exibir grafo
plt.show()

