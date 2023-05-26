# 2° Etapa
# Calcular economias entre cada um dos pontos
# Gerar matriz de economias
# Organizar pares de economias em ordem decrecente

import csv

dicionario = {}
with open('dijkstra_graph.txt', 'r') as f:
    dicionario = eval(f.read())

print(dicionario[('Empresa', 'A')][0] + dicionario[('Empresa', 'B')][0] - dicionario[('A', 'B')][0])

AA = 0
AB = str(round(dicionario[('Empresa', 'A')][0] + dicionario[('Empresa', 'B')][0] - dicionario[('A', 'B')][0], 2)).replace('.', ',')
AC = str(round(dicionario[('Empresa', 'A')][0] + dicionario[('Empresa', 'C')][0] - dicionario[('A', 'C')][0], 2)).replace('.', ',')
AD = str(round(dicionario[('Empresa', 'A')][0] + dicionario[('Empresa', 'D')][0] - dicionario[('A', 'D')][0], 2)).replace('.', ',')
AE = str(round(dicionario[('Empresa', 'A')][0] + dicionario[('Empresa', 'E')][0] - dicionario[('A', 'E')][0], 2)).replace('.', ',')
AF = str(round(dicionario[('Empresa', 'A')][0] + dicionario[('Empresa', 'F')][0] - dicionario[('A', 'F')][0], 2)).replace('.', ',')
AG = str(round(dicionario[('Empresa', 'A')][0] + dicionario[('Empresa', 'G')][0] - dicionario[('A', 'G')][0], 2)).replace('.', ',')
AH = str(round(dicionario[('Empresa', 'A')][0] + dicionario[('Empresa', 'H')][0] - dicionario[('A', 'H')][0], 2)).replace('.', ',')
AI = str(round(dicionario[('Empresa', 'A')][0] + dicionario[('Empresa', 'I')][0] - dicionario[('A', 'I')][0], 2)).replace('.', ',')

BA = str(round(dicionario[('Empresa', 'B')][0] + dicionario[('Empresa', 'A')][0] - dicionario[('B', 'A')][0], 2)).replace('.', ',')
BB = 0
BC = str(round(dicionario[('Empresa', 'B')][0] + dicionario[('Empresa', 'C')][0] - dicionario[('B', 'C')][0], 2)).replace('.', ',')
BD = str(round(dicionario[('Empresa', 'B')][0] + dicionario[('Empresa', 'D')][0] - dicionario[('B', 'D')][0], 2)).replace('.', ',')
BE = str(round(dicionario[('Empresa', 'B')][0] + dicionario[('Empresa', 'E')][0] - dicionario[('B', 'E')][0], 2)).replace('.', ',')
BF = str(round(dicionario[('Empresa', 'B')][0] + dicionario[('Empresa', 'F')][0] - dicionario[('B', 'F')][0], 2)).replace('.', ',')
BG = str(round(dicionario[('Empresa', 'B')][0] + dicionario[('Empresa', 'G')][0] - dicionario[('B', 'G')][0], 2)).replace('.', ',')
BH = str(round(dicionario[('Empresa', 'B')][0] + dicionario[('Empresa', 'H')][0] - dicionario[('B', 'H')][0], 2)).replace('.', ',')
BI = str(round(dicionario[('Empresa', 'B')][0] + dicionario[('Empresa', 'I')][0] - dicionario[('B', 'I')][0], 2)).replace('.', ',')

CA = str(round(dicionario[('Empresa', 'C')][0] + dicionario[('Empresa', 'A')][0] - dicionario[('C', 'A')][0], 2)).replace('.', ',')
CB = str(round(dicionario[('Empresa', 'C')][0] + dicionario[('Empresa', 'B')][0] - dicionario[('C', 'B')][0], 2)).replace('.', ',')
CC = 0
Empresa = str(round(dicionario[('Empresa', 'C')][0] + dicionario[('Empresa', 'D')][0] - dicionario[('C', 'D')][0], 2)).replace('.', ',')
CE = str(round(dicionario[('Empresa', 'C')][0] + dicionario[('Empresa', 'E')][0] - dicionario[('C', 'E')][0], 2)).replace('.', ',')
CF = str(round(dicionario[('Empresa', 'C')][0] + dicionario[('Empresa', 'F')][0] - dicionario[('C', 'F')][0], 2)).replace('.', ',')
CG = str(round(dicionario[('Empresa', 'C')][0] + dicionario[('Empresa', 'G')][0] - dicionario[('C', 'G')][0], 2)).replace('.', ',')
CH = str(round(dicionario[('Empresa', 'C')][0] + dicionario[('Empresa', 'H')][0] - dicionario[('C', 'H')][0], 2)).replace('.', ',')
CI = str(round(dicionario[('Empresa', 'C')][0] + dicionario[('Empresa', 'I')][0] - dicionario[('C', 'I')][0], 2)).replace('.', ',')

DA = str(round(dicionario[('Empresa', 'D')][0] + dicionario[('Empresa', 'A')][0] - dicionario[('D', 'A')][0], 2)).replace('.', ',')
DB = str(round(dicionario[('Empresa', 'D')][0] + dicionario[('Empresa', 'B')][0] - dicionario[('D', 'B')][0], 2)).replace('.', ',')
DC = str(round(dicionario[('Empresa', 'D')][0] + dicionario[('Empresa', 'C')][0] - dicionario[('D', 'C')][0], 2)).replace('.', ',')
DD = 0
DE = str(round(dicionario[('Empresa', 'D')][0] + dicionario[('Empresa', 'E')][0] - dicionario[('D', 'E')][0], 2)).replace('.', ',')
DF = str(round(dicionario[('Empresa', 'D')][0] + dicionario[('Empresa', 'F')][0] - dicionario[('D', 'F')][0], 2)).replace('.', ',')
DG = str(round(dicionario[('Empresa', 'D')][0] + dicionario[('Empresa', 'G')][0] - dicionario[('D', 'G')][0], 2)).replace('.', ',')
DH = str(round(dicionario[('Empresa', 'D')][0] + dicionario[('Empresa', 'H')][0] - dicionario[('D', 'H')][0], 2)).replace('.', ',')
DI = str(round(dicionario[('Empresa', 'D')][0] + dicionario[('Empresa', 'I')][0] - dicionario[('D', 'I')][0], 2)).replace('.', ',')

EA = str(round(dicionario[('Empresa', 'E')][0] + dicionario[('Empresa', 'A')][0] - dicionario[('E', 'A')][0], 2)).replace('.', ',')
EB = str(round(dicionario[('Empresa', 'E')][0] + dicionario[('Empresa', 'B')][0] - dicionario[('E', 'B')][0], 2)).replace('.', ',')
EC = str(round(dicionario[('Empresa', 'E')][0] + dicionario[('Empresa', 'C')][0] - dicionario[('E', 'C')][0], 2)).replace('.', ',')
ED = str(round(dicionario[('Empresa', 'E')][0] + dicionario[('Empresa', 'D')][0] - dicionario[('E', 'D')][0], 2)).replace('.', ',')
EE = 0
EF = str(round(dicionario[('Empresa', 'E')][0] + dicionario[('Empresa', 'F')][0] - dicionario[('E', 'F')][0], 2)).replace('.', ',')
EG = str(round(dicionario[('Empresa', 'E')][0] + dicionario[('Empresa', 'G')][0] - dicionario[('E', 'G')][0], 2)).replace('.', ',')
EH = str(round(dicionario[('Empresa', 'E')][0] + dicionario[('Empresa', 'H')][0] - dicionario[('E', 'H')][0], 2)).replace('.', ',')
EI = str(round(dicionario[('Empresa', 'E')][0] + dicionario[('Empresa', 'I')][0] - dicionario[('E', 'I')][0], 2)).replace('.', ',')

FA = str(round(dicionario[('Empresa', 'F')][0] + dicionario[('Empresa', 'A')][0] - dicionario[('F', 'A')][0], 2)).replace('.', ',')
FB = str(round(dicionario[('Empresa', 'F')][0] + dicionario[('Empresa', 'B')][0] - dicionario[('F', 'B')][0], 2)).replace('.', ',')
FC = str(round(dicionario[('Empresa', 'F')][0] + dicionario[('Empresa', 'C')][0] - dicionario[('F', 'C')][0], 2)).replace('.', ',')
FD = str(round(dicionario[('Empresa', 'F')][0] + dicionario[('Empresa', 'D')][0] - dicionario[('F', 'D')][0], 2)).replace('.', ',')
FE = str(round(dicionario[('Empresa', 'F')][0] + dicionario[('Empresa', 'E')][0] - dicionario[('F', 'E')][0], 2)).replace('.', ',')
FF = 0
FG = str(round(dicionario[('Empresa', 'F')][0] + dicionario[('Empresa', 'G')][0] - dicionario[('F', 'G')][0], 2)).replace('.', ',')
FH = str(round(dicionario[('Empresa', 'F')][0] + dicionario[('Empresa', 'H')][0] - dicionario[('F', 'H')][0], 2)).replace('.', ',')
FI = str(round(dicionario[('Empresa', 'F')][0] + dicionario[('Empresa', 'I')][0] - dicionario[('F', 'I')][0], 2)).replace('.', ',')

GA = str(round(dicionario[('Empresa', 'G')][0] + dicionario[('Empresa', 'A')][0] - dicionario[('G', 'A')][0], 2)).replace('.', ',')
GB = str(round(dicionario[('Empresa', 'G')][0] + dicionario[('Empresa', 'B')][0] - dicionario[('G', 'B')][0], 2)).replace('.', ',')
GC = str(round(dicionario[('Empresa', 'G')][0] + dicionario[('Empresa', 'C')][0] - dicionario[('G', 'C')][0], 2)).replace('.', ',')
GD = str(round(dicionario[('Empresa', 'G')][0] + dicionario[('Empresa', 'D')][0] - dicionario[('G', 'D')][0], 2)).replace('.', ',')
GE = str(round(dicionario[('Empresa', 'G')][0] + dicionario[('Empresa', 'E')][0] - dicionario[('G', 'E')][0], 2)).replace('.', ',')
GF = str(round(dicionario[('Empresa', 'G')][0] + dicionario[('Empresa', 'F')][0] - dicionario[('G', 'F')][0], 2)).replace('.', ',')
GG = 0
GH = str(round(dicionario[('Empresa', 'G')][0] + dicionario[('Empresa', 'H')][0] - dicionario[('G', 'H')][0], 2)).replace('.', ',')
GI = str(round(dicionario[('Empresa', 'G')][0] + dicionario[('Empresa', 'I')][0] - dicionario[('G', 'I')][0], 2)).replace('.', ',')

HA = str(round(dicionario[('Empresa', 'H')][0] + dicionario[('Empresa', 'A')][0] - dicionario[('H', 'A')][0], 2)).replace('.', ',')
HB = str(round(dicionario[('Empresa', 'H')][0] + dicionario[('Empresa', 'B')][0] - dicionario[('H', 'B')][0], 2)).replace('.', ',')
HC = str(round(dicionario[('Empresa', 'H')][0] + dicionario[('Empresa', 'C')][0] - dicionario[('H', 'C')][0], 2)).replace('.', ',')
HD = str(round(dicionario[('Empresa', 'H')][0] + dicionario[('Empresa', 'D')][0] - dicionario[('H', 'D')][0], 2)).replace('.', ',')
HE = str(round(dicionario[('Empresa', 'H')][0] + dicionario[('Empresa', 'E')][0] - dicionario[('H', 'E')][0], 2)).replace('.', ',')
HF = str(round(dicionario[('Empresa', 'H')][0] + dicionario[('Empresa', 'F')][0] - dicionario[('H', 'F')][0], 2)).replace('.', ',')
HG = str(round(dicionario[('Empresa', 'H')][0] + dicionario[('Empresa', 'G')][0] - dicionario[('H', 'G')][0], 2)).replace('.', ',')
HH = 0
HI = str(round(dicionario[('Empresa', 'H')][0] + dicionario[('Empresa', 'I')][0] - dicionario[('H', 'I')][0], 2)).replace('.', ',')

IA = str(round(dicionario[('Empresa', 'I')][0] + dicionario[('Empresa', 'A')][0] - dicionario[('I', 'A')][0], 2)).replace('.', ',')
IB = str(round(dicionario[('Empresa', 'I')][0] + dicionario[('Empresa', 'B')][0] - dicionario[('I', 'B')][0], 2)).replace('.', ',')
IC = str(round(dicionario[('Empresa', 'I')][0] + dicionario[('Empresa', 'C')][0] - dicionario[('I', 'C')][0], 2)).replace('.', ',')
ID = str(round(dicionario[('Empresa', 'I')][0] + dicionario[('Empresa', 'D')][0] - dicionario[('I', 'D')][0], 2)).replace('.', ',')
IE = str(round(dicionario[('Empresa', 'I')][0] + dicionario[('Empresa', 'E')][0] - dicionario[('I', 'E')][0], 2)).replace('.', ',')
IF = str(round(dicionario[('Empresa', 'I')][0] + dicionario[('Empresa', 'F')][0] - dicionario[('I', 'F')][0], 2)).replace('.', ',')
IG = str(round(dicionario[('Empresa', 'I')][0] + dicionario[('Empresa', 'G')][0] - dicionario[('I', 'G')][0], 2)).replace('.', ',')
IH = str(round(dicionario[('Empresa', 'I')][0] + dicionario[('Empresa', 'H')][0] - dicionario[('I', 'H')][0], 2)).replace('.', ',')
II = 0

with open('savings.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'])
    writer.writerow([AA, AB, AC, AD, AE, AF, AG, AH, AI])
    writer.writerow([BA, BB, BC, BD, BE, BF, BG, BH, BI])
    writer.writerow([CA, CB, CC, Empresa, CE, CF, CG, CH, CI])
    writer.writerow([DA, DB, DC, DD, DE, DF, DG, DH, DI])
    writer.writerow([EA, EB, EC, ED, EE, EF, EG, EH, EI])
    writer.writerow([FA, FB, FC, FD, FE, FF, FG, FH, FI])
    writer.writerow([GA, GB, GC, GD, GE, GF, GG, GH, GI])
    writer.writerow([HA, HB, HC, HD, HE, HF, HG, HH, HI])
    writer.writerow([IA, IB, IC, ID, IE, IF, IG, IH, II])

# GERAR PARES DE ECONOMIA
pair_of_savings = {
    ('A', 'A'): AA, ('A', 'B'): AB, ('A', 'C'): AC, ('A', 'D'): AD, ('A', 'E'): AE, ('A', 'F'): AF, ('A', 'G'): AG, ('A', 'H'): AH, ('A', 'I'): AI,
    ('B', 'A'): BA, ('B', 'B'): BB, ('B', 'C'): BC, ('B', 'D'): BD, ('B', 'E'): BE, ('B', 'F'): BF, ('B', 'G'): BG, ('B', 'H'): BH, ('B', 'I'): BI,
    ('C', 'A'): CA, ('C', 'B'): CB, ('C', 'C'): CC, ('C', 'D'): Empresa, ('C', 'E'): CE, ('C', 'F'): CF, ('C', 'G'): CG, ('C', 'H'): CH, ('C', 'I'): CI,
    ('D', 'A'): DA, ('D', 'B'): DB, ('D', 'C'): DC, ('D', 'D'): DD, ('D', 'E'): DE, ('D', 'F'): DF, ('D', 'G'): DG, ('D', 'H'): DH, ('D', 'I'): DI,
    ('E', 'A'): EA, ('E', 'B'): EB, ('E', 'C'): EC, ('E', 'D'): ED, ('E', 'E'): EE, ('E', 'F'): EF, ('E', 'G'): EG, ('E', 'H'): EH, ('E', 'I'): EI,
    ('F', 'A'): FA, ('F', 'B'): FB, ('F', 'C'): FC, ('F', 'D'): FD, ('F', 'E'): FE, ('F', 'F'): FF, ('F', 'G'): FG, ('F', 'H'): FH, ('F', 'I'): FI,
    ('G', 'A'): GA, ('G', 'B'): GB, ('G', 'C'): GC, ('G', 'D'): GD, ('G', 'E'): GE, ('G', 'F'): GF, ('G', 'G'): GG, ('G', 'H'): GH, ('G', 'I'): GI,
    ('H', 'A'): HA, ('H', 'B'): HB, ('H', 'C'): HC, ('H', 'D'): HD, ('H', 'E'): HE, ('H', 'F'): HF, ('H', 'G'): HG, ('H', 'H'): HH, ('H', 'I'): HI,
    ('I', 'A'): IA, ('I', 'B'): IB, ('I', 'C'): IC, ('I', 'D'): ID, ('I', 'E'): IE, ('I', 'F'): IF, ('I', 'G'): IG, ('I', 'H'): IH, ('I', 'I'): II
}

# ORGANIZAR POR ORDEM DECRESCENTE
# sorted_savings = sorted(pair_of_savings.items(), key=lambda x: x[1], reverse=True)
# ORGANIZAR POR ORDEM DECRESCENTE TRANSFORMANDO TODOS OS ITENS EM FLOAT E APLICANDO REPLACE PARA TROCAR . POR ,
sorted_savings = sorted(pair_of_savings.items(), key=lambda x: float(str(x[1]).replace(',', '.')), reverse=True)
print(sorted_savings)

# GERAR CSV COM PARES DE ECONOMIA
with open('pair_of_savings.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter='=')
    writer.writerow(['Pair', 'Savings'])
    for i in sorted_savings:
        writer.writerow([str(i[0]).replace("'", ''), i[1]])




