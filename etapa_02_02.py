# Escolher Vértices (CD e Destinos)
# Iterar sobre os vértices aplicando o algoritmo de Dijkstra
# Gerar CSV com os resultados

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

# ESCOLHER VÉRTICES (ORIGEM E DESTINOS)
Empresa = (-45.6028463, -23.0316574) 

DESTINOS = {'Empresa': Empresa,'A': (-45.5996569, -23.0284983), 'B': (-45.5979163, -23.0304307), 'C': (-45.5990331, -23.0315897), 'D': (-45.6056408, -23.0272866), 'E': (-45.6084752, -23.0293651), 'F': (-45.6054539, -23.029753), 'G': (-45.6040497, -23.0338179), 'H': (-45.6039264, -23.0348083), 'I': (-45.6018611, -23.0357605)}

# ITERAR SOBRE OS VÉRTICES APLICANDO O ALGORITMO DE DIJKSTRA
file_teste = open('dijkstra_graph.txt', 'w')

trajetos = {}

def Dijkstra(key, value):
    # PARA TODOS OS VERTICES
    for d in DESTINOS:
            path = nx.bidirectional_dijkstra(weighted_G, source=value, target=DESTINOS[d], weight='weight')
            ROTA = path[1]
            # length = nx.dijkstra_path_length(weighted_G, source=value, target=DESTINOS[d], weight='weight')
            # CUSTO = length
            # print({(key, d)})
            trajetos[(key, d)] = path

def Dijkstra_Exemplo(key, value):
    # EXEMPLO DE UMA ROTA / EXEMPLO COMEÇANDO DA ORIGEM
    path = nx.bidirectional_dijkstra(weighted_G, source=Empresa, target=value, weight='weight')
    # ROTA = path[1]
    # length = nx.dijkstra_path_length(weighted_G, source=Empresa, target=value, weight='weight')
    # CUSTO = length
    result = nx.DiGraph()
    for data in weighted_G.edges(data=True):
        if data[0] in path[1] and data[1] in path[1]:
            result.add_edge(data[0], data[1], weight=data[2]['weight'])

    nx.draw_networkx_labels(result, pos, font_size=9, font_family='sans-serif', labels={DESTINOS[key]: key}, font_weight='bold', font_color='w')
    nx.draw_networkx(result, pos, node_size=20, with_labels=False, width=0.5, node_color='r', edge_color='r')
    nx.draw_networkx_nodes(result, pos, nodelist=[value], node_size=200, node_color='g')
    nx.draw_networkx_nodes(result, pos, nodelist=[Empresa], node_size=350, node_color='w')
    nx.draw_networkx_labels(result, pos, font_size=13, font_family='sans-serif', labels={Empresa: 'Empresa'}, font_weight='bold',font_color='w', bbox=dict(facecolor='r', alpha=1, edgecolor='black', boxstyle='round,pad=0.2'))

# loop in DESTINOS
for key, value in DESTINOS.items():
    Dijkstra(key, value)
    Dijkstra_Exemplo(key, value)

# EXEMPLO ?
plt.show()

# Dijkstra_Exemplo('C', (-45.5990331, -23.0315897))


file_teste.write(str(trajetos))

