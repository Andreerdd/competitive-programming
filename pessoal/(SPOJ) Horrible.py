"""
Segment Tree com Lazy Propagation
"""

T = int(input())

# N = tamanho do array
# C = quantidade de comandos
N,C = map(int, input().split())

tree = [0] * (4 * N)
lz = [0] * (4 * N)


def unlazy(node: int, nl: int, nr: int):
    # Verifica se existe algo para atualizar
    if lz[node] == 0: return

    # atualiza o nó na árvore
    tree[node] += (nr - nl + 1) * lz[node]

    # atualiza os filhos do nó
    if nl != nr:
        lz[2 * node + 1] += lz[node]
        lz[2 * node + 2] += lz[node]

    # diz que já atualizamos esse nó
    lz[node] = 0


def update(v: int, l: int, r: int, node: int = 0, nl: int = 0, nr: int = N - 1):
    unlazy(node, nl, nr)

    # se não tiver no intervalo, ignora
    if nl > r or nr < l: return

    # se tiver totalmente no intervalo, atualiza
    if nl >= l and nr <= r:
        lz[node] += v
        unlazy(node, nl, nr)
        return

    mid = (nl + nr) >> 1

    # Atualiza os dois filhos (pq esse nó atualizou)
    update(v, l, r, 2*node + 1, nl, mid)
    update(v, l, r, 2*node + 2, mid + 1, nr)

    tree[node] = tree[2 * node + 1] + tree[2 * node + 2]


def query(l: int, r: int, node: int = 0, nl: int = 0, nr: int = N - 1) -> int:
    unlazy(node, nl, nr)

    if nl > r or nr < l: return 0

    if nl >= l and nr <= r: return tree[node]

    mid = (nl + nr) >> 1

    return query(l, r, 2 * node + 1, nl, mid) + query(l, r, 2 * node + 2, mid + 1, nr)


def main():
    for _ in range(C):
        entrada = list(map(int, input().split()))
        if entrada[0] == 0:
            update(entrada[3], entrada[1] - 1, entrada[2] - 1)
        else:
            print(query(entrada[1] - 1, entrada[2] - 1))



main()