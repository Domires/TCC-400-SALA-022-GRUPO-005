# TCC-400-SALA-022-GRUPO-005
Este repositório contém todo o código fonte desenvolvido durante o trabalho de conclusão de curso TCC-400-SALA-022-GRUPO-005, intitulado "UTILIZAÇÃO DE HEURISTICA E ALGORITMOS DE ESCOLHA DE ROTAS PARA DEFINIÇÃO DA ROTA MAIS ECONÔMICA EM UM FRETAMENTO DE FUNCIONÁRIOS".

O código fonte está disponível em Python. Ele inclui todas as etapas do processo desenvolvido no trabalho até o presente momento, desde a extração de dados geográficos do de um arquivo shapefile até a implementação do algoritmo de busca de menor custo usando a biblioteca NetworkX.

Execução:
- Certifique-se de ter o Python 3.x instalado em seu computador.
- Faça o download do código-fonte disponível em https://github.com/Domires/TCC-400-SALA-022-GRUPO-005.
- Abra o cmd e navegue até o diretório onde o código-fonte foi baixado.
- Execute o script.py digitando "python script.py" no prompt de comando e pressione Enter. Este script irá gerar o grafo e os dados necessários para gerar o csv.
- Em seguida, execute o gerar_csv.py digitando "python gerar_csv.py" no prompt de comando e pressione Enter. Este script irá gerar a tabela com as menores distâncias entre os vértices em formato csv.

# OBS: O código fonte ainda está desenvolvimento
- [x] Gerar Digrafo a partir de um arquivo shapefile
- [x] Calcular menor caminho entre todos os vértices (CD e Destinos) utilizando Dijkstra
- [x] Gerar CSV com a matriz de distâncias entre cada vértice
- [ ] Implementar o método de Clarke e Wright para gerar o roteiro final
- [ ] Refatorar código (desacoplar)
