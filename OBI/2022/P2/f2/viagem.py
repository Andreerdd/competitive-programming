import heapq # heap queue (pilhas)
INF = 1e9

# valor disponivel, n ilhas, n rotas
V,N,M = list(map(int, input().split()))

# as conexões (barcos)
arestas = [[] for _ in range(N+1)]

for _ in range(M):
    # a, b -> ilhas
    # t -> tempo
    # p -> preço
    a,b,t,p = list(map(int, input().split()))
    
    # conecta a ilha 'a' ate 'b'
    arestas[a].append((b, t, p))
    arestas[b].append((a, t, p))
    
# inicio e fim da viagem
X, Y = list(map(int, input().split()))

## algoritmo dijkstra modificado ##

# menores_tempos[ilha][preco] = menor tempo para aquela ilha com aquele preço
menores_tempos = [[INF for _ in range(V+1)] for _ in range(N+1)]

def dijkstra():
    
    # heap queue
    # [tempo, preco, ponto]
    pq = []
    heapq.heapify(pq)
    
    # adiciona a origem
    heapq.heappush(pq, [0, 0, X])
    
    # enquanto houver elementos para olhar
    while pq:
        # pega o vertice
        pair = heapq.heappop(pq)
        
        # tempo total, preco, ponto
        ti, pi, vi = pair
        
        # se já encontramos um caminho melhor com esse preço,
        # pule essa iteração
        if (ti > menores_tempos[vi][pi]): continue
                
        # obtem as arestas que ele vai
        for viz in arestas[vi]:
            # ilha fim, tempo, preço do ponto final
            vf, tf, pf = viz
            
            # novo custo
            nc = pi+pf
            # novo tempo
            nt = ti+tf
            
            # se o preço não ultrapassou o total (ainda há orçamento)
            if nc <= V:
                # se o tempo agora é menor que o tempo salvo (com o mesmo preço)
                if nt < menores_tempos[vf][nc]:
                    # encontramos um caminho mais rápido para vf gastando nc e demorando nt
                    menores_tempos[vf][nc] = nt
                    heapq.heappush(pq, [nt, nc, vf])
                    
dijkstra()

res = min(menores_tempos[Y])
print(-1 if res == INF else res)

