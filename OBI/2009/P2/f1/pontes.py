# Estratégia: Dijkstra
import heapq
import sys # Importar a biblioteca sys

# Usar sys.stdin.readline para leitura rápida
input = sys.stdin.readline

hpush = heapq.heappush
hpop = heapq.heappop

inf = 10e6+10
maxn = 1010
maxm = 10010

N,M = map(int, input().split())
arestas = [[] for _ in range(maxn)]


for _ in range(M):
    s, t, b = map(int, input().split())

    arestas[s].append((t, b))
    arestas[t].append((s, b))


dist = [inf] * maxn
dist[0] = 0
def dijkstra():
    heap = []
    hpush(heap, (0, 0)) # (distância, pilar)

    while heap:
        b, p = hpop(heap)

        if b > dist[p]: continue

        for viz, bviz in arestas[p]:
            nb = b + bviz
            if nb < dist[viz]:
                dist[viz] = nb
                hpush(heap, (nb, viz))


dijkstra()

print(dist[N+1])