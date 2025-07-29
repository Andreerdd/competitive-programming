# Só para brincar
# Estratégia: Segment Tree

N,Q = map(int, input().split())
v = list(map(int, input().split()))
queries = []

class Node:
    def __init__(self, esq=None, dir=None, soma=0, isFolha=False):
        if dir is None:
            dir = []
        if esq is None:
            esq = []
        self.esq = esq
        self.dir = dir
        self.soma = soma
        self.isFolha = isFolha

tree = [0 for _ in range(4*N)]

for _ in range(Q):
    queries.append(list(map(int, input().split())))

def merge(l: Node, r: Node, no: Node = 0):
    if no == 0: no = Node(isFolha=False)

    if l == 0:
        no.dir = r.dir.copy()
        no.esq = r.esq.copy()
        if r.isFolha:
            no.esq.append(r.soma)
            no.soma = 0
        else:
            no.soma = r.soma
        return no
    if r == 0:
        no.dir = l.dir.copy()
        no.esq = l.esq.copy()

        if l.isFolha:
            no.esq.append(l.soma)
            no.soma = 0
        else:
            no.soma = l.soma
        return no

    if l.isFolha: no.esq.append(l.soma)
    else:
        no.esq = l.esq + l.dir
        no.soma += l.soma

    if r.isFolha: no.dir.append(r.soma)
    else:
        no.dir = r.esq + r.dir
        no.soma += r.soma

    # faz a soma entre eles
    for i in no.esq:
        for j in no.dir:
            no.soma += i*10+j
    for i in no.dir:
        for j in no.esq:
            no.soma += i*10+j

    return no

def build(tl=0, tr=N-1, no=0):
    if tl == tr:
        tree[no] = Node(soma=v[tl], isFolha=True)
        return tree[no]

    mid = (tl+tr) >> 1
    left = build(tl, mid, 2*no+1)
    right = build(mid+1, tr, 2*no+2)

    tree[no] = merge(left, right)
    return tree[no]

def query(l, r, tl=0, tr=N-1, no=0):
    if tl > r or tr < l: return 0
    if tl >= l and tr <= r: return tree[no]
    mid = (tl+tr) >> 1
    return merge(query(l, r, tl, mid, 2*no+1), query(l, r, mid+1, tr, 2*no+2))

def solve():
    build()
    for q in queries:
        print(query(q[0] - 1, q[1] - 1).soma)

solve()