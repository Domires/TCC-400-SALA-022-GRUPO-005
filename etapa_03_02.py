# Aplicar Método de Clarke Wright
# Gerar roteiro
# plotar resultado final

SAVINGS = {
    ('D', 'E'):	[1090.74, 'MD'],
    ('B', 'C'):	[1012.89, 'MD'],
    ('D', 'F'):	[957.12, 'MD'],
    ('E', 'F'):	[956.54, 'MD'],
    ('A', 'B'):	[908.0, 'MD'],
    ('A', 'C'):	[883.51, 'MD'],
    ('I', 'H'):	[818.52, 'MU'],
    ('G', 'H'):	[755.56, 'MD'],
    ('I', 'G'):	[602.93, 'MU'],
    ('G', 'I'):	[594.04, 'MU'],
    ('H', 'I'):	[592.27, 'MU'],
    ('C', 'I'):	[555.57, 'MD'],
    ('D', 'A'):	[455.81, 'MU'],
    ('F', 'A'):	[450.5, 'MU'],
    ('E', 'A'):	[449.92, 'MU'],
    ('B', 'I'):	[404.33, 'MD'],
    ('E', 'G'):	[331.0, 'MD'],
    ('E', 'H'):	[329.22, 'MD'],
    ('A', 'I'):	[307.1, 'MD'],
    ('D', 'G'):	[305.9, 'MD'],
    ('F', 'G'):	[305.9, 'MD'],
    ('D', 'H'):	[304.13, 'MD'],
    ('F', 'H'):	[304.13, 'MD'],
    ('G', 'C'):	[270.53, 'MU'],
    ('H', 'C'):	[268.76, 'MU'],
    ('C', 'G'):	[255.4, 'MU'],
    ('C', 'H'):	[255.4, 'MU'],
    ('D', 'B'):	[199.1, 'MU'],
    ('F', 'B'):	[193.79, 'MU'],
    ('E', 'B'):	[193.21, 'MU'],
    ('I', 'E'):	[190.3, 'MU'],
    ('E', 'I'):	[181.41, 'MU'],
    ('A', 'D'):	[180.93, 'MU'],
    ('A', 'F'):	[180.93, 'MU'],
    ('B', 'D'):	[180.93, 'MU'],
    ('B', 'F'):	[180.93, 'MU'],
    ('A', 'E'):	[180.35, 'MU'],
    ('B', 'E'):	[180.35, 'MU'],
    ('D', 'C'):	[177.39, 'MU'],
    ('F', 'C'):	[172.08, 'MU'],
    ('E', 'C'):	[171.5, 'MU'],
    ('I', 'D'):	[165.21, 'MU'],
    ('I', 'F'):	[165.21, 'MU'],
    ('C', 'D'):	[159.22, 'MU'],
    ('C', 'F'):	[159.22, 'MU'],
    ('C', 'E'):	[158.63, 'MU'],
    ('D', 'I'):	[156.31, 'MU'],
    ('F', 'I'):	[156.31, 'MU'],
    ('G', 'B'):	[119.29, 'MU'],
    ('H', 'B'):	[117.51, 'MU'],
    ('B', 'G'):	[104.16, 'MU'],
    ('B', 'H'):	[104.16, 'MU'],
    ('G', 'A'):	[22.06, 'MU'],
    ('H', 'A'):	[20.28, 'MU'],
    ('A', 'G'):	[6.93, 'MU'],
    ('A', 'H'):	[6.93, 'MU']
}

rotas = []

index = 0

capacidade = 3

print('Capacidade', capacidade)

pontos_usados = []

def clarke_wright(S, r):
    # r = 0
    roteiro = {}
    qtd = 0
    for par, dados in S.items():
        if par[0] in str(pontos_usados) or par[1] in str(pontos_usados):
            continue
        if qtd == capacidade:
            roteiro['rota_' + str(r)].insert(0, 'Empresa')
            roteiro['rota_' + str(r)].append('Empresa')
            pontos_usados.append(roteiro['rota_' + str(r)])
            return roteiro
        if roteiro == {}:
            roteiro['rota_' + str(r)] = [par[0], par[1]]
            qtd += 2
            continue
        if par[0] in roteiro['rota_' + str(r)] and par[1] in roteiro['rota_' + str(r)]:
            continue

        # se o par conter 'MU' então verificar se o par[0] está no fim da rota ou se o par[1] está no início da rota
        if dados[1] == 'MU':
            if roteiro['rota_' + str(r)][0] == par[1]:
                roteiro['rota_' + str(r)].insert(0, par[0])
                qtd += 1
                continue
            elif roteiro['rota_' + str(r)][-1] == par[0]:
                roteiro['rota_' + str(r)].append(par[1])
                qtd += 1
                continue
            else:
                continue

        if par[0] in roteiro['rota_' + str(r)] or par[1] in roteiro['rota_' + str(r)]:
            if roteiro['rota_' + str(r)][0] == par[0]:
                roteiro['rota_' + str(r)].insert(0, par[1])
                qtd += 1
                continue
            if roteiro['rota_' + str(r)][0] == par[1]:
                roteiro['rota_' + str(r)].insert(0, par[0])
                qtd += 1
                continue
            if roteiro['rota_' + str(r)][-1] == par[0]:
                roteiro['rota_' + str(r)].append(par[1])
                qtd += 1
                continue
            if roteiro['rota_' + str(r)][-1] == par[1]:
                roteiro['rota_' + str(r)].append(par[0])
                qtd += 1
                continue
                 
for i in range(15):
    rot = clarke_wright(SAVINGS, r=i+1)
    if rot != None:
        print('clarke_wright', rot)





# print('Custo Total', 5363.52)

