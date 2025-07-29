"""
Estratégia: Segment Tree
Para o nó pai, usaremos um merge que verá a diferença
entre o mínimo de um e o máximo de outro (e vice-versa).

- Para construir a árvore, inicialmente, é gasto O(n) de tempo
- Para cada atualização, é gasto O(log n)
- Para cada query, pode ser gasto:
  - se a maior bola e a menor bola estiverem em baldes diferentes,
    o tempo é O(log n)
  - se a maior bola e a menor bola estiverem em baldes iguais, o
    tempo é O(log n + 2*log n) = O(log n)
  - Logo, para cada query, o tempo é O(log n)

Portanto, o tempo é O(n + m*log n)
"""

inf = 10e6

N, M = map(int, input().split())
# baldes[k] = [minimo, maximo]
baldes = [[] for _ in range(N + 1)]
queries = []
ent = list(map(int, input().split()))

for i in range(N):
    baldes[i] = [ent[i], ent[i]]


for _ in range(M):
    ent = list(map(int, input().split()))
    # 1 = 'u' = update
    # 2 = 'q' = query
    ent[0] = 'u' if ent[0] == 1 else 'q'
    queries.append(ent)

# Só precisamos nos importar com o mínimo e o máximo,
# já que a maior diferença é com eles
def updatebalde(p, b):
    if p < baldes[b][0]: baldes[b][0] = p
    if p > baldes[b][1]: baldes[b][1] = p

tree = [[] for _ in range(4 * N)]
def buildTree(tl=0, tr=N-1, no: int = 0):

    if tl == tr:
        tree[no] = baldes[tl] + [tl, tl]
        return tree[no]

    mid = (tl+tr) >> 1

    left = buildTree(tl, mid, 2*no+1)
    right = buildTree(mid+1, tr, 2*no+2)

    _min = min(left[0], right[0])
    min_idx = left[2] if _min == tree[2*no+1][0] else right[2]

    _max = max(left[1], right[1])
    max_idx = left[3] if _max == tree[2*no+1][1] else right[3]

    tree[no] = [ _min, _max, min_idx, max_idx ]
    return tree[no]


def updateTree(b, tl=0, tr=N-1, no: int = 0):
    if tl == tr:
        tree[no] = baldes[tl] + [tl, tl]
        return tree[no]

    mid = (tl+tr) >> 1
    if tl <= b <= mid:
        left = updateTree(b, tl, mid, 2*no+1)
        right = tree[2*no+2] # assim, verifica se vai mudar algo pro nó
    else:
        left = tree[2*no+1]
        right = updateTree(b, mid+1, tr, 2*no+2)

    _min = min(left[0], right[0])
    min_idx = left[2] if _min == tree[2*no+1][0] else right[2]

    _max = max(left[1], right[1])
    max_idx = left[3] if _max == tree[2*no+1][1] else right[3]

    tree[no] = [ _min, _max, min_idx, max_idx ]
    return tree[no]

def query(l, r, tl=0, tr=N-1, no: int = 0):
    if tl > r or tr < l: return None

    if tl >= l and tr <= r: return tree[no]

    mid = (tl+tr) >> 1

    left = query(l, r, tl, mid, 2*no+1)
    right = query(l, r, mid+1, tr, 2*no+2)

    if left is None:
        return right
    if right is None:
        return left

    _min = min(left[0], right[0])
    min_idx = left[2] if _min == tree[2*no+1][0] else right[2]

    _max = max(left[1], right[1])
    max_idx = left[3] if _max == tree[2*no+1][1] else right[3]

    # se chegou até aqui, nenhum dos dois é none
    return [ _min, _max, min_idx, max_idx ]

def solvequery(l, r):
    res = query(l, r)
    min_i, max_i = res[2], res[3]

    # se for diferente
    if min_i != max_i:
        return res[1] - res[0]

    # se for igual
    lq = [inf, -inf]
    if min_i > l: lq = query(l, min_i-1)

    rq = [inf, -inf]
    if max_i < r: rq = query(max_i+1, r)

    temp = [min(lq[0], rq[0]), max(lq[1], rq[1])]

    if temp[0] == inf: return 0

    return max(res[1] - temp[0], temp[1] - res[0])

def solve():
    buildTree()
    for entry in queries:
        r,a,b = entry

        if r == 'u':
            updatebalde(a, b-1)
            updateTree(b-1)
        else:
            print(solvequery(a-1, b-1))



solve()
