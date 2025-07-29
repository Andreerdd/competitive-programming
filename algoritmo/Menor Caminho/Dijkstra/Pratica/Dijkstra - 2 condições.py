# Aqui, usa-se um dijkstra com 2 condições:
# - o nível de instabilidade não pode ultrapassar o nível
#   de instabilidade máximo (I)
# - tem que andar da partida ao destino no mínimo de
#   risco possível

import heapq
INF = 1e9

# n distritos, m passarelas, i = nível máximo de instabilidade
N,M,I = map(int, input().split())

# arestas[n] = (fim, risco, instabilidade)
arestas = [[] for _ in range(N+1)]

for _ in range(M):
    # a, b -> inicio e fim
    # r -> risco
    # s -> instabilidade (nao pode ultrapassar)
    a,b,r,s = map(int, input().split())
    arestas[a].append((b, r, s))
    arestas[b].append((a, r, s))
    
# Partida, Destino
P, D = map(int, input().split())

## dijkstra modificado ##

# menores_riscos[distrito][instabilidade] = menor risco naquele distrito naquela instabilidade
menores_riscos = [[INF for _ in range(I+1)] for _ in range(N+1)]

# nao tem risco de ir para o inicio nem instabilidade
for i in range(I+1):
    menores_riscos[P][i] = 0
    
def dijkstra():

    # Estrutura: pq[i] = (risco, instabilidade, fim)
    pq = []
    
    heapq.heappush(pq, (0, 0, P))
    
    while pq:
        curr = heapq.heappop(pq)
        
        # (risco, instabilidade, fim)
        ri, si, fi = curr
        
        # se já encontrou um caminho melhor com essa instabilidade para fi
        if ri > menores_riscos[fi][si]: continue
        
        for arr in arestas[fi]:
            # fim, risco, instabilidade do fim
            ff, rf, sf =  arr
            
            # novo risco
            nr = ri+rf
            
            # nova instabilidade
            ns = si+sf
            
            # se não ultrapassou a instabilidade total
            if ns <= I:
                # se for diminuir o risco, atualiza
                if nr < menores_riscos[ff][ns]:
                    heapq.heappush(pq, (nr, ns, ff))
                    menores_riscos[ff][ns] = nr
        

res = min(menores_riscos[D])
print(-1 if res == INF else res)
