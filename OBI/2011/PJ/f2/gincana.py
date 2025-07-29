# Estratégia: Union-Find
N,M = map(int,input().split())

parent = [i for i in range(N+1)]
rank = [1 for i in range(N+1)]

times = N # cada aluno é um time

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x]) # path compression
    return parent[x]

def union(a, b):
    pa = find(a)
    pb = find(b)

    if pa == pb: return

    # cada união significa que 2 times viraram 1.
    # Logo, retira 1
    global times
    times -= 1

    # union by rank
    if rank[pa] > rank[pb]:
        pa, pb = pb, pa

    parent[pa] = pb

    rank[pb] += rank[pa]

for _ in range(M):
    a, b = map(int, input().split())
    union(a, b)

print(times)
