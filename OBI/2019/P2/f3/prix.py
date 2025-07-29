"""
Grand Prix da Nlogônia
OBI 2019 - Fase 3 - Programação Nível 2

Estratégia: Segment Tree
"""

# N = vértices
# M = conexões
N,M = map(int,input().split())
planos = []

for _ in range(0, M):
    u, l, r = map(int,input().split())
    planos.append([u - 1,l - 1,r - 1])

total_vertices = 4*N
nos = [[] for _ in range(total_vertices)]
folhasPos = [-1 for _ in range(N)]

def build(tl=0, tr=N-1, no: int = 0):
    if tl == tr:
        nos[no] = []
        folhasPos[tl] = no
        return

    mid = (tl+tr) // 2

    build(tl, mid, 2*no + 1)
    build(mid+1, tr, 2*no + 2)

    nos[no] = []
    nos[no].append(2*no + 1)
    nos[no].append(2*no + 2)



def find_covering_nodes(l, r, memoPos, tl=0, tr=N-1, no: int = 0):
    global nos
    if tr < l or tl > r: return  # não faz parte do intervalo

    # se tiver dentro do intervalo
    if tl >= l and tr <= r:
        nos[memoPos].append(no)
        return

    mid = (tl+tr) >> 1
    find_covering_nodes(l, r, memoPos, tl, mid, 2*no+1)
    find_covering_nodes(l, r, memoPos, mid+1, tr, 2*no+2)


def dfs(i, vizinhos, visitados_globalmente, pilha):
    global nos

    pilha[i] = True

    for no in vizinhos:
        if no not in visitados_globalmente:
            visitados_globalmente[no] = True
            if dfs(no, nos[no], visitados_globalmente, pilha):
                return True
        elif no in pilha:
            return True

    pilha.pop(i)
    return False


def check(mid):
    global nos

    # reseta os nos
    build()

    # vê os planos e adiciona aos seus
    # vertices.adj os nós que eles podem
    # ir para
    for p in planos[:mid]:
        u, l, r = p
        find_covering_nodes(l, r, folhasPos[u])


    visitados_globalmente: dict[int: bool] = {}
    pilha: dict[int: bool] = {}

    for i in range(total_vertices):
        vizinhos = nos[i]
        if i not in visitados_globalmente:
            visitados_globalmente[i] = True
            if dfs(i, vizinhos, visitados_globalmente, pilha):
                return True

    return False


def main():
    build()
    X = -1

    # checa usando busca binária
    l, r = 1, M
    while l <= r:
        mid = (l + r) >> 1
        if mid == 0:
            l = mid + 1
            continue
        if check(mid):
            X = mid
            r = mid - 1
        else:
            l = mid + 1

    # mostra o resultado
    print(X)

main()