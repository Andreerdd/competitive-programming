# Estratégia: Dijkstra
# Vamos considerar o tabuleiro como um grafo e ligar os
# quadrados adjacentes com peso 1 se há uma pedra no quadrado
# ou, se não houver uma pedra, peso 0.
import heapq
hpu = heapq.heappush
hpp = heapq.heappop

inf = float('inf')

N = int(input())
mina = []

# obtém a mina
for x in range(N):
    mina.append( list(map(int, input().split())) )


# distância até o ponto [x, y]
dist = [[inf for _ in range(N)] for _ in range(N)]

movimentos = [[0, -1], [-1, 0], [0, 1], [1, 0]] # movimentos ortogonais
def dijkstra():
    heap = []

    # coloca a origem
    hpu(heap, (0, (0, 0) ))

    # enquanto houver coisa para calcular
    while heap:
        p, v = hpp(heap)
        x,y = v

        # se a qntd de pedra for maior do que a já calculada, ignora
        if p > dist[x][y]: continue

        # pega os vizinhos
        for i, j in movimentos:
            if not (0 <= x+i < N) or not (0 <= y+j < N): continue

            novo_p = p + mina[x+i][y+j]
            if dist[x+i][y+j] > novo_p:
                dist[x+i][y+j] = novo_p
                hpu(heap, (novo_p, (x+i, y+j)))


dijkstra()
print(dist[N-1][N-1])