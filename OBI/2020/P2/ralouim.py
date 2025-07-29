# Algoritmo:
#   nao sei

import math

N = int(input())
doces = 0

# Obtem as entradas
centro_dist = []
centro_dist.append(0) # o castelo
for _ in range(N):
    x, y = map(int, input().split())
    # d² = x² + y²
    # d = sqrt(x² + y²)
    centro_dist.append(x**2 + y**2)

centro_dist.sort() # Ordena

# quantidade máxima de doces que pode obter A PARTIR do
# caminho i até j (qd[i][j])
qd: list[list[int]] = [[] * (N+1)] * (N+1)
for i in range(0, N+1):
    # da origem ao centro
    last_dist = centro_dist[i]
    qd[i] = [0]
    
    for j in range(1, N+1):
        # Primeiro, verifica se não tá tentando ir pro mesmo
        if i == j:
            qd[i].append(-1)
            continue
        
        # Verifica se a distância é menor que a última
        if abs(centro_dist[i] - centro_dist[j]) < last_dist:
            qd[i].append(max(qd[j]) + 1)
        
print(qd)