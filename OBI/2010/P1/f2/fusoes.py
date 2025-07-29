N,K = map(int,input().split())
parent = [i for i in range(N+1)]
rank = [0 for i in range(N+1)]

def union(a, b):
    if a == b:
        return
    pa, pb = find(a), find(b)

    if rank[pa] > rank[pb]:
        pa,pb = pb,pa

    parent[pa] = pb
    rank[pa] += rank[pb] if rank[pb] > 0 else 1

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

for _ in range(K):
    acao, a, b = input().split()
    a = int(a)
    b = int(b)

    if acao == 'F':
        union(a, b)
    else:
        print('S' if find(a) == find(b) else 'N')