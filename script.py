import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_shp('teste/teste02.shp')

weighted_G = nx.DiGraph()
for data in G.edges(data=True):
   if data[2]['other_tags'] is not None:
      if '"oneway"=>"yes"' in data[2]['other_tags']: 
         weighted_G.add_edge(data[0], data[1], weight=data[2]['comp2'])
      else:
         weighted_G.add_edge(data[0], data[1], weight=data[2]['comp2'])
         weighted_G.add_edge(data[1], data[0], weight=data[2]['comp2'])

pos = {v:v for v in weighted_G.nodes()}

nx.draw_networkx(weighted_G, pos, node_size=20, with_labels=False, width=0.2)

CD = (-45.6028463, -23.0316574)
DESTINOS = {'CD': CD,'A': (-45.5996569, -23.0284983), 'B': (-45.5979163, -23.0304307), 'C': (-45.5990331, -23.0315897), 'D': (-45.6056408, -23.0272866), 'E': (-45.6084752, -23.0293651), 'F': (-45.6054539, -23.029753), 'G': (-45.6040497, -23.0338179), 'H': (-45.6039264, -23.0348083), 'I': (-45.6018611, -23.0357605)}

file_teste = open('dijkstra_graph.txt', 'w')

trajetos = {}

def Dijkstra(key, value):
    # A PARTIR DO CD
    # path = nx.bidirectional_dijkstra(weighted_G, source=CD, target=value, weight='weight')
    # # ROTA = path[1]
    # # length = nx.dijkstra_path_length(weighted_G, source=CD, target=value, weight='weight')
    # # CUSTO = length
    # result = nx.DiGraph()
    # for data in weighted_G.edges(data=True):
    #     if data[0] in path[1] and data[1] in path[1]:
    #         result.add_edge(data[0], data[1], weight=data[2]['weight'])

    # # nx.write_edgelist(result, 'teste.txt', data=True)
    # nx.draw_networkx_labels(result, pos, font_size=9, font_family='sans-serif', labels={DESTINOS[key]: key}, font_weight='bold', font_color='w')
    # nx.draw_networkx(result, pos, node_size=20, with_labels=False, width=0.5, node_color='r', edge_color='r')
    # nx.draw_networkx_nodes(result, pos, nodelist=[value], node_size=200, node_color='g')
    # nx.draw_networkx_nodes(result, pos, nodelist=[CD], node_size=250, node_color='b')
    # # write dict in file_teste
    # # file_teste.write(str(key) + ' ' + str(value) + '\n')

    # PARA TODOS OS VERTICES
    for d in DESTINOS: # if d != key:
            path = nx.bidirectional_dijkstra(weighted_G, source=value, target=DESTINOS[d], weight='weight')
            ROTA = path[1]
            length = nx.dijkstra_path_length(weighted_G, source=value, target=DESTINOS[d], weight='weight')
            CUSTO = length
            # result = nx.DiGraph()
            # for data in weighted_G.edges(data=True):
            #      if data[0] in path[1] and data[1] in path[1]:
            #          result.add_edge(data[0], data[1], weight=data[2]['weight'])
            # nx.write_edgelist(result, 'teste.txt', data=True)
            # nx.draw_networkx(result, pos, node_size=40, with_labels=False, width=2, node_color='r', edge_color='r')
            print({(key, d)})
            # add dict in trajetos
            trajetos[(key, d)] = path
            # plt.savefig('teste/' + str(key) + '_' + str(d) + '.png', dpi=300)
    #         plt.show() plt.clf() plt.cla() plt.close()

# loop in DESTINOS
for key, value in DESTINOS.items():
    Dijkstra(key, value)

print(trajetos)
file_teste.write(str(trajetos))

# plt.show()

# for d in DESTINOS:
#     # plt.scatter(d[0], d[1], c='r', s=50)
#     path = nx.bidirectional_dijkstra(weighted_G, source=CD, target=d, weight='weight')
#     ROTA = path[1]
#     length = nx.dijkstra_path_length(weighted_G, source=CD, target=d, weight='weight')
#     CUSTO = length
#     result = nx.DiGraph()
#     for data in weighted_G.edges(data=True):
#          if data[0] in path[1] and data[1] in path[1]:
#              result.add_edge(data[0], data[1], weight=data[2]['weight'])
#     nx.write_edgelist(result, 'teste.txt', data=True)
#     print('\n', 'ROTA', '\n', ROTA, '\n')
#     print('\n', 'CUSTO', '\n', CUSTO, '\n')
#     # nx.draw_networkx(result, pos, node_size=30, with_labels=False, width=0.2)
#     nx.draw_networkx(result, pos, node_size=40, with_labels=False, width=2, node_color='r', edge_color='r')

# plt.show()

    # plt.clf()
    # plt.cla()
    # plt.close()


# path = nx.bidirectional_dijkstra(weighted_G, source=ORIGEM, target=DESTINO, weight='weight')
# ROTA = path[1]

# length = nx.dijkstra_path_length(weighted_G, source=ORIGEM, target=DESTINO, weight='weight')
# PESO = length

# print('\n', 'ROTA', '\n', ROTA, '\n') 
# print('\n', 'PESO', '\n', PESO, '\n')

# # CD (-45.6028463, -23.0316574)
# GARAGEM = 0 # (-45.6028463, -23.0316574)

# #(-45.6028463, -23.0316574)
# ORIGEM =  (-45.6028463, -23.0316574) 

# # A (-45.5996569, -23.0284983)
# # B (-45.5979163, -23.0304307)
# # C (-45.5990331, -23.0315897)
# # D (-45.6056408, -23.0272866)
# # E (-45.6084752, -23.0293651)
# # F (-45.6054539, -23.029753)
# # G (-45.6040497, -23.0338179)
# # H (-45.6039264, -23.0348083)
# # I (-45.6018611, -23.0357605)
# DESTINO = (-45.6018611, -23.0357605)

# path = nx.bidirectional_dijkstra(weighted_G, source=ORIGEM, target=DESTINO, weight='weight')
# ROTA = path[1]

# length = nx.dijkstra_path_length(weighted_G, source=ORIGEM, target=DESTINO, weight='weight')
# PESO = length

# result = nx.DiGraph()
# for data in weighted_G.edges(data=True):
#    if data[0] in path[1] and data[1] in path[1]:
#       result.add_edge(data[0], data[1], weight=data[2]['weight'])

# nx.write_edgelist(result, 'teste.txt', data=True)

# nx.draw_networkx(result, pos, node_size=40, with_labels=False, width=2, node_color='r', edge_color='r')

# print('\n', 'ROTA', '\n', ROTA, '\n') 
# print('\n', 'PESO', '\n', PESO, '\n')

# plt.show()
