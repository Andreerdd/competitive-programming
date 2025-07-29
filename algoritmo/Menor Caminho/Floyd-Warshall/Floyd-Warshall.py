"""
O algoritmo de Floyd-Warshall é utilizado para calcular a menor distância entre
todos os pares de vértices do grafo, diferentemente do algoritmo de Dijkstra.

Vamos definir d(u, v, k) como a menor distância de u para v considerando que,
de u para v, há apenas vértices (que são intermediários) de índice menor ou
igual a k. Assim:
    - Se k = 0, então d(u, v, k=0) = aresta[u][v]
    - Se k != 0, então d(u, v, k) = min( d(u, v, k-1), d(u, k, k-1) + d(k, v, k-1) )

Note que, se não houver caminho direto de u até v, d(u, v, 0) = infinito.
"""

inf = float('inf')

# Obtém os nós e as arestas
Qntd_Nos, Qntd_Arestas = 5, 10

arestas = [[inf for _ in range(Qntd_Nos)] for _ in range(Qntd_Nos)]

dist = [[inf for _ in range(Qntd_Nos)] for _ in range(Qntd_Nos)]

def calcularDistancia():

    # inicializa as distâncias no caso d(u, v, k=0)
    for i in range(Qntd_Nos):
        for j in range(Qntd_Nos):
            dist[i][j] = arestas[i][j]

    # calcula os casos com um vértice intermediário
    for k in range(1, Qntd_Nos):
        for i in range(Qntd_Nos):
            for j in range(Qntd_Nos):
                # não precisamos colocar k-1 pois o loop já garante
                # que o dist[i][k] reflete o estado de dist[i][k-1]
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])