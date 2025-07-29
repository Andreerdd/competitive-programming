# Estratégia: Dijkstra
import heapq
hpu = heapq.heappush
hpp = heapq.heappop

maxn = 1010

inf = float('inf')
N, M = map(int, input().split())
arestas = [[] for _ in range(maxn)]

# Obtém as arestas (grafo não direcional)
for _ in range(M):
    u,v,p = map(int, input().split())
    arestas[u].append((v, p)) # 0-indexed, então retira 1
    arestas[v].append((u, p))

S = int(input()) # onde o servidor vai ser instalado

dist = [inf] * maxn
dist[S] = 0 # a ilha do próprio servidor tem ping 0

def dijkstra():
    heap = []
    hpu(heap, (0, S))

    while heap:
        p, i = hpp(heap)

        # se a distância for maior, ignora
        if p > dist[i]: continue

        for viz, pviz in arestas[i]:
            novo_p = p + pviz
            if novo_p < dist[viz]:
                dist[viz] = novo_p
                hpu(heap, (novo_p, viz))

dijkstra()

# printa a diferença exceto a ilha do servidor
res = dist[1:S] + dist[S+1:N+1]
print(max(res) - min(res))