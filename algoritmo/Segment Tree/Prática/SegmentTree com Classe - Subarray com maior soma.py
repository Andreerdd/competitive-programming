"""
Segment Tree com Classe ++ (avançado)

Aqui, o problema é, dado um intervalo [l, r] do vetor,
encontrar o valor do subarray [i,j] de soma máxima tal
que l <= i <= j <= r.
"""

class Node:
    def __init__(self, tl=0, tr=0, left=None, right=None, ans=0, somatotal=0, maxprefixo=0, maxsufixo=0):
        self.tl = tl                    # início do intervalo do nó
        self.tr = tr                    # fim do intervalo do nó
        self.left = left                # filho da esquerda
        self.right = right              # filho da direita
        self.ans = ans                  # o maior subarray
        self.somaTotal = somatotal      # a soma: todos os filhos da esquerda + todos os filhos da direita
        self.maxPrefixo = maxprefixo    # o maior subarray que começa no primeiro elemento do filho da esquerda -> [tl, ...]
        self.maxSufixo = maxsufixo      # o maior subarray que termina no último elemento do filho da direita -> [..., tr]

vals = [1, 2, -3, 4, 5]
N = len(vals)

def merge(a: Node, b: Node, _no: Node = 0) -> Node:
    """
    Une os dois nós, fazendo um nó pai
    que tem o maior subarray calculado
    :return: nó pai
    """

    # define se vai atualizar um nó já existente
    # ou se vai criar um novo
    no = None
    if _no == 0: no = Node()
    else: no = _no

    no.somaTotal = a.somaTotal + b.somaTotal
    no.maxPrefixo = max(a.maxPrefixo, a.somaTotal + b.maxPrefixo)
    no.maxSufixo = max(b.maxSufixo, b.somaTotal + a.maxSufixo)
    no.ans = max(a.ans, b.ans, a.maxSufixo + b.maxPrefixo)
    no.left = a
    no.right = b

    return no

def build(tl=0, tr=N-1):

    if tl==tr:
        # cria um novo nó (folha)
        return Node(tl=tl, tr=tr, ans=max(0, vals[tl]), somatotal=vals[tl], maxprefixo=vals[tl], maxsufixo=vals[tl])

    mid = (tl+tr) >> 1

    # cria os nós filhos
    left = build(tl, mid)
    right = build(mid+1, tr)

    no = merge(left, right)
    no.tl = tl
    no.tr = tr

    return no

def update(idx: int, val: int, no: Node):
    tl = no.tl
    tr = no.tr

    if tl==tr:
        # atualiza o nó folha e o vetor
        vals[idx] = val
        no.ans = max(0, val)
        no.somaTotal = no.maxPrefixo = no.maxSufixo = val
        return

    # se o caminho para o elemento que vai atualizar (idx)
    # for para a esquerda, vai para a esquerda; se não,
    # vai para a direita

    mid = (tl+tr) >> 1
    if tl <= idx <= mid: update(idx, val, no.left)
    else: update(idx, val, no.right)

    # atualiza o nó
    merge(no.left, no.right, no)


def queue(l, r, no: Node):
    tl = no.tl
    tr = no.tr

    # se tá fora do intervalo, a resposta é 0
    if tl > r or tr < l: return Node(ans=0, somatotal=0, maxprefixo=0, maxsufixo=0)

    # se tá dentro do intervalo, retorna o nó
    if tl >= l and tr <= r: return no

    # aqui, a gente usa o "merge" pq ele garante que
    # a resposta vai ser sempre a melhor
    return merge(queue(l, r, no.left), queue(l, r, no.right))



# alguns testes
def main():
    root = build()
    print(queue(0, N - 1, root).ans)
    update(2, 3, root)
    print(queue(0, N - 1, root).ans)


main()