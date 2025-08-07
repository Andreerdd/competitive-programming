# Algoritmo de MST
# Complexidade: O(m log n)

class Aresta:
    def __init__(self, args):
        self.x = args[0]
        self.y = args[1]
        self.peso = args[2]

maxn = 5010  # limite da quantidade de nós

N,M = map(int, input().split())
arestas = []
for i in range(M):
    ent = list(map(int, input().split()))
    arestas.append(Aresta(ent))

# union-find
pai = [i for i in range(maxn)]
rank = [1 for i in range(maxn)]

def find(x):
    if pai[x] == x: return x
    pai[x] = find(pai[x]) # path compression
    return pai[x]

def union(a, b):
    pa = find(a)
    pb = find(b)

    # union by rank
    if rank[pa] > rank[pb]:
        pa, pb = pb, pa

    pai[pa] = pb
    rank[pb] += rank[pa]


# MST
mst = []

def buildMST():
    for ar in arestas:
        a, b, p = ar.x, ar.y, ar.peso

        # só adiciona a aresta na mst se ela tiver
        # um pai diferente (para evitar ciclo)
        if find(a) != find(b):
            union(a, b) # une as arestas

            mst.append(ar) # adiciona na mst

def main():
    # ordena as arestas em função do peso
    arestas.sort(key=lambda aresta: aresta.peso)

    # constrói a MST
    buildMST()

    # imprime o resultado
    for ar in mst:
        print(ar.x, ar.y, ar.peso)

main()