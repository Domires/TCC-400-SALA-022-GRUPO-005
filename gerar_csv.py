import csv

dicionario = {}
with open('dijkstra_graph.txt', 'r') as f:
    dicionario = eval(f.read())

with open('dijkstra_graph.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    qtd = 0
    linha = []
    for key, value in dicionario.items():
            qtd += 1
            linha.append(str(round(value[0], 2)).replace('.', ','))

            if qtd == 10:
                writer.writerow(linha)
                print(linha)
                linha = []
                qtd = 0
