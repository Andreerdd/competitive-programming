# Estratégia: Union-Find


# qntd pessoas, qntd conexões
N,M = map(int, input().split())

total = N # total de pais

# rank[i] = qntd de elementos com o pai i
rank = [1 for i in range(N+1)]

# Parent[i] = pai de i
# Se parent[i] = i, i é raíz
Parent = [i for i in range(N+1)] # pais

def find(k):
    if Parent[k] == k: return k
    Parent[k] = find(Parent[k])
    return Parent[k]

def union(a, b):
    Parent[find(a)] = find(b)
    

for _ in range(M):
    a, b = map(int, input().split())
    
    # verifica quem tem mais rank.
    # trabalharemos sempre com a > b
    if rank[b] > rank[a]:
        a, b = b, a
        
    rank[a] += rank[b]
    
    fa, fb = find(a), find(b)
    
    if fa != fb: total -= 1
    
    # coloca b dentro de a
    union(fa, fb)

print(total)
    
    
    
    
    
    