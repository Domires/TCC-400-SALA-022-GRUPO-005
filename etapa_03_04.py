import networkx as nx
import matplotlib.pyplot as plt

# G = nx.read_shp('teste/teste02.shp')
G = nx.read_shp('shapefile/arquivo.shp')

weighted_G = nx.DiGraph()
for data in G.edges(data=True):
#    print(data)
   if data[2]['other_tags'] is not None:
      if '"oneway"=>"yes"' in data[2]['other_tags']: 
         weighted_G.add_edge(data[0], data[1], weight=data[2]['comp2'])
      else:
         weighted_G.add_edge(data[0], data[1], weight=data[2]['comp2'])
         weighted_G.add_edge(data[1], data[0], weight=data[2]['comp2'])

pos = {v:v for v in weighted_G.nodes()}

nx.draw_networkx(weighted_G, pos, node_size=20, with_labels=False, width=0.2)

Empresa = (-45.6028463, -23.0316574) 
# DESTINOS = [(-45.5996569, -23.0284983), (-45.5979163, -23.0304307), (-45.5990331, -23.0315897), (-45.6056408, -23.0272866), (-45.6084752, -23.0293651), (-45.6054539, -23.029753), (-45.6040497, -23.0338179), (-45.6039264, -23.0348083), (-45.6018611, -23.0357605)]

DESTINOS = {'Empresa': Empresa,'A': (-45.5996569, -23.0284983), 'B': (-45.5979163, -23.0304307), 'C': (-45.5990331, -23.0315897), 'D': (-45.6056408, -23.0272866), 'E': (-45.6084752, -23.0293651), 'F': (-45.6054539, -23.029753), 'G': (-45.6040497, -23.0338179), 'H': (-45.6039264, -23.0348083), 'I': (-45.6018611, -23.0357605)}

path_result1 = []
path_result2 = []
path_result3 = []

total = 0

# considerando capacidade = 3
path = nx.bidirectional_dijkstra(weighted_G, source=DESTINOS['Empresa'], target=DESTINOS['F'], weight='weight')
ROTA = path[1]
total += path[0]
path_result1.append(ROTA)
path = nx.bidirectional_dijkstra(weighted_G, source=DESTINOS['F'], target=DESTINOS['D'], weight='weight')
ROTA = path[1]
total += path[0]
path_result1.append(ROTA)
path = nx.bidirectional_dijkstra(weighted_G, source=DESTINOS['D'], target=DESTINOS['E'], weight='weight')
ROTA = path[1]
total += path[0]
path_result1.append(ROTA)
path = nx.bidirectional_dijkstra(weighted_G, source=DESTINOS['E'], target=DESTINOS['Empresa'], weight='weight')
ROTA = path[1]
total += path[0]
path_result1.append(ROTA)

path = nx.bidirectional_dijkstra(weighted_G, source=DESTINOS['Empresa'], target=DESTINOS['A'], weight='weight')
ROTA = path[1]
total += path[0]
path_result2.append(ROTA)
path = nx.bidirectional_dijkstra(weighted_G, source=DESTINOS['A'], target=DESTINOS['B'], weight='weight')
ROTA = path[1]
total += path[0]
path_result2.append(ROTA)
path = nx.bidirectional_dijkstra(weighted_G, source=DESTINOS['B'], target=DESTINOS['C'], weight='weight')
ROTA = path[1]
total += path[0]
path_result2.append(ROTA)
path = nx.bidirectional_dijkstra(weighted_G, source=DESTINOS['C'], target=DESTINOS['Empresa'], weight='weight')
ROTA = path[1]
total += path[0]
path_result2.append(ROTA)

path = nx.bidirectional_dijkstra(weighted_G, source=DESTINOS['Empresa'], target=DESTINOS['I'], weight='weight')
ROTA = path[1]
total += path[0]
path_result3.append(ROTA)
path = nx.bidirectional_dijkstra(weighted_G, source=DESTINOS['I'], target=DESTINOS['H'], weight='weight')
ROTA = path[1]
total += path[0]
path_result3.append(ROTA)
path = nx.bidirectional_dijkstra(weighted_G, source=DESTINOS['H'], target=DESTINOS['G'], weight='weight')
ROTA = path[1]
total += path[0]
path_result3.append(ROTA)
path = nx.bidirectional_dijkstra(weighted_G, source=DESTINOS['G'], target=DESTINOS['Empresa'], weight='weight')
ROTA = path[1]
total += path[0]
path_result3.append(ROTA)
total = round(total, 2)
print(total)

result = nx.DiGraph()

for data in weighted_G.edges(data=True):
    if data[0] in path_result1[0] and data[1] in path_result1[0]:
        result.add_edge(data[0], data[1], weight=data[2]['weight'])
    if data[0] in path_result1[1] and data[1] in path_result1[1]:
        result.add_edge(data[0], data[1], weight=data[2]['weight'])
    if data[0] in path_result1[2] and data[1] in path_result1[2]:
        result.add_edge(data[0], data[1], weight=data[2]['weight'])
    if data[0] in path_result1[3] and data[1] in path_result1[3]:
        result.add_edge(data[0], data[1], weight=data[2]['weight'])
        # nx.draw_networkx(result, pos, node_size=40, with_labels=False, width=2, node_color='b', edge_color='b')

result2 = nx.DiGraph()
for data in weighted_G.edges(data=True):
    if data[0] in path_result2[0] and data[1] in path_result2[0]:
        result2.add_edge(data[0], data[1], weight=data[2]['weight'])
    if data[0] in path_result2[1] and data[1] in path_result2[1]:
        result2.add_edge(data[0], data[1], weight=data[2]['weight'])
    if data[0] in path_result2[2] and data[1] in path_result2[2]:
        result2.add_edge(data[0], data[1], weight=data[2]['weight'])
    if data[0] in path_result2[3] and data[1] in path_result2[3]:
        result2.add_edge(data[0], data[1], weight=data[2]['weight'])
        # nx.draw_networkx(result2, pos, node_size=40, with_labels=False, width=2, node_color='g', edge_color='g')

result3 = nx.DiGraph()
for data in weighted_G.edges(data=True):
    if data[0] in path_result3[0] and data[1] in path_result3[0]:
        result3.add_edge(data[0], data[1], weight=data[2]['weight'])
    if data[0] in path_result3[1] and data[1] in path_result3[1]:
        result3.add_edge(data[0], data[1], weight=data[2]['weight'])
    if data[0] in path_result3[2] and data[1] in path_result3[2]:
        result3.add_edge(data[0], data[1], weight=data[2]['weight'])
    if data[0] in path_result3[3] and data[1] in path_result3[3]:
        result3.add_edge(data[0], data[1], weight=data[2]['weight'])
        # nx.draw_networkx(result3, pos, node_size=40, with_labels=False, width=2, node_color='y', edge_color='y')

nx.draw_networkx(result, pos, node_size=40, with_labels=False, width=2, node_color='b', edge_color='b')
nx.draw_networkx(result2, pos, node_size=40, with_labels=False, width=2, node_color='g', edge_color='g')
nx.draw_networkx(result3, pos, node_size=40, with_labels=False, width=2, node_color='y', edge_color='y')
nx.draw_networkx_nodes(result, pos, nodelist=[DESTINOS['F'], DESTINOS['D'], DESTINOS['E']], node_size=350, node_color='b')
nx.draw_networkx_nodes(result, pos, nodelist=[DESTINOS['A'], DESTINOS['B'], DESTINOS['C']], node_size=350, node_color='g')
nx.draw_networkx_nodes(result, pos, nodelist=[DESTINOS['I'], DESTINOS['H'], DESTINOS['G']], node_size=350, node_color='y')
nx.draw_networkx_labels(result, pos, font_size=9, font_family='sans-serif', labels={DESTINOS['A']: 'A', DESTINOS['B']: 'B', DESTINOS['C']: 'C', DESTINOS['D']: 'D', DESTINOS['E']: 'E', DESTINOS['F']: 'F', DESTINOS['G']: 'G', DESTINOS['H']: 'H', DESTINOS['I']: 'I'}, font_weight='bold',font_color='w')

nx.draw_networkx_nodes(result, pos, nodelist=[DESTINOS['Empresa']], node_size=350, node_color='w')
nx.draw_networkx_labels(result, pos, font_size=13, font_family='sans-serif', labels={DESTINOS['Empresa']: 'Empresa'}, font_weight='bold',font_color='w', bbox=dict(facecolor='r', alpha=1, edgecolor='black', boxstyle='round,pad=0.2'))

plt.show()