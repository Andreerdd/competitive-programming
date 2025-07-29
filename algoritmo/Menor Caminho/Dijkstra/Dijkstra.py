# Dijkstra

import heapq
hpush = heapq.heappush
hpop = heapq.heappop

inf = 10e6+10
maxn = 1010
maxm = 10010

# obtém as arestas
N,M = map(int, input().split())
arestas = [[] for _ in range(maxn)]

for _ in range(M):
    s, t, d = map(int, input().split())

    arestas[s].append((t, d))
    arestas[t].append((s, d))

# inicializa todas as distâncias como infinito
dist = [inf] * maxn
dist[0] = 0

def dijkstra():
    heap = [] # estrutura: heap[i] = [distancia, vertice]

    # coloca a origem no heap
    hpush(heap, (0, 0))

    # enquanto houver arestas para calcular
    while heap:
        # obtém o topo do heap
        d, v = hpop(heap)

        # se a distância for maior do que a já calculada, ignora
        if d > dist[v]: continue

        # calcula novamente a distância para os vizinhos
        for viz, dviz in arestas[v]:
            nova_distancia = d + dviz
            if nova_distancia < dist[viz]:
                dist[viz] = nova_distancia
                hpush(heap, nova_distancia)


dijkstra()
print(dist[N+1])


