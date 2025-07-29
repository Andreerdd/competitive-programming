N, Q = list(map(int, input().split()))
jogo = [[] for _ in range(N)]

# Carrega o vetor
for l in range(N):
    entrada = input()
    for c in range(N):
        jogo[l].append(int(entrada[c]))
        

# retorna os vizinhos vivos
def vizinhos(l, c):
    viz = 0
    for i in range(-1, 1 +1):
        for j in range(-1, 1 +1):
            x,y = l+i, c+j
            if (x < 0 or x >= N) or (y < 0 or y >= N) or (x == l and y == c):
                continue
            if jogo[x][y] == 1: viz +=1
    
    return viz
        
def passo():
    global jogo
    novo = [[] for _ in range(N)]
    
    # Olha no vetor todo
    for l in range(N):
        for c in range(N):
            curr = jogo[l][c]
            viz = vizinhos(l, c)
            
            if curr == 0:   # morto
                if viz == 3:
                    novo[l].append(1)
                else:
                    novo[l].append(0)
            else:           # vivo
                if (viz == 3) or (viz == 2):
                    novo[l].append(1)
                else:
                    novo[l].append(0)
                    
    jogo = novo
                
        
        
for _ in range(Q):
    passo()
    
# printa

for l in range(N):
    for c in range(N):
        print(jogo[l][c], end='')
    print()
        

