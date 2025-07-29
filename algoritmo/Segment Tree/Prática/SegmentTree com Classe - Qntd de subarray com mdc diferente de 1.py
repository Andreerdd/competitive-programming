"""
OBI 2020, Fase 3, P2: Candidatas

Resumidamente, o problema nos dá um vetor e realizará dois tipos de operações:

1.  Mudar o valor de uma posição do vetor;
2.  Saber o número de subintervalos desse vetor com máximo divisor comum maior do
    que 1 dentro de um intervalo [l,r] dado.
"""

# poderia usar isso aqui pra calcular mdc também #
# from math import gcd as mdc

class Node:
    def __init__(self, tl=0,tr=0,ans=0, mdc=1,left=None, right=None):
        self.tl = tl        # o início do intervalo do nó
        self.tr = tr        # o fim do intervalo do nó
        self.ans = ans      # a quantidade de subintervalos com mdc > 1
        self.left = left    # o filho da esquerda
        self.right = right  # o filho da direita
        self.mdc = mdc      # o mdc de todos os elementos (dos filhos)
        self.pref = []      # lista dos mdc's do filho da esquerda
        self.suf = []       # lista dos mdc's do filho da direita



vals = [2,4,3]
N = len(vals)

def mdc(a, b): return a if not b else mdc(b, a%b);

def merge(l: Node, r: Node, _no: Node = 0) -> Node:
    no = None
    if _no == 0: no = Node()    # para criar um novo nó
    else: no = _no              # para atualizar o nó

    # adiciona o que já tem
    no.ans = l.ans + r.ans
    # calcula o novo mdc
    no.mdc = mdc(l.mdc, r.mdc)

    # A subsequência válida inicia no filho da esquerda
    # e termina no filho da direita.
    no.pref = l.pref.copy()
    if l.mdc > 1:
        last = l.mdc
        # Calcula o vetor prefixo
        for p in r.pref:
            v = mdc(p[0], last)

            # Não contaremos os 1.
            # Ademais, os próximos p[0] também terão
            # mdc = 0, então pode parar o loop
            if v == 1: break

            # Se já contou, apenas incrementa
            if no.pref and v == no.pref[-1][0]: no.pref[-1][1] += p[1]
            # Se não contou, cria um novo
            else: no.pref.append([v, p[1]])

            last = v

    # Calcula o vetor sufixo
    no.suf = r.suf.copy()
    if r.mdc > 1:
        last = r.mdc
        for p in l.suf:
            v = mdc(p[0], last)

            # Não contaremos os 1.
            # Ademais, os próximos p[0] também terão
            # mdc = 0, então pode parar o loop
            if v == 1: break

            # Se já contou, apenas incrementa
            if no.suf and v == no.suf[-1][0]: no.suf[-1][1] += p[1]
            # Se não contou, cria um novo
            else: no.suf.append([v, p[1]])

            last = v

    """
    # Calcula a quantidade de intervalos que se inicia no 
    # filho da esquerda e termina no filho da direita.
    # Isso é, basicamente, ver quantos sufixos do filho da 
    # esquerda tem mdc diferente de 1 quando comparados aos 
    # prefixos da direita.
    """
    ptr = len(r.pref)-1
    total = 0
    for i in r.pref: total += i[1]
    for s in l.suf:
        while ptr >= 0 and mdc(s[0], r.pref[ptr][0]) == 1:
            total -= r.pref[ptr][1]
            ptr -= 1
        no.ans += total * s[1]


    return no

def update(idx, val, no: Node):
    tl, tr = no.tl, no.tr
    if tl == tr:
        vals[tl] = val
        no.ans = int(vals[tl]>1)
        no.mdc = vals[tl]
        no.pref.clear()
        no.suf.clear()
        if vals[tl] != 1:
            no.pref.append([vals[tl], 1])
            no.suf.append([vals[tl], 1])
        return
    mid = (tl+tr) >> 1

    if tl <= idx <= mid: update(idx, val, no.left)
    else: update(idx, val, no.right)

    merge(no.left, no.right, no)

def build(tl=0, tr=N-1):
    no = Node(tl=tl, tr=tr)
    if tl == tr:
        no.ans = int(vals[tl]>1)
        no.mdc = vals[tl]
        if vals[tl] != 1:
            no.pref.append([vals[tl], 1])
            no.suf.append([vals[tl], 1])
        return no

    mid = (tl+tr) >> 1

    no.left = build(tl, mid)
    no.right = build(mid+1, tr)

    return merge(no.left, no.right, no)

def query(l, r, no: Node):
    tl, tr = no.tl, no.tr

    if tl > r or tr < l:
        return Node()
    if tl >= l and tr <= r:
        return no

    return merge(query(l, r, no.left), query(l, r, no.right))


def main():
    root = build()
    print(query(0, N-1, root).ans)
    update(1, 5, root)
    print(query(0, N-1, root).ans)
    update(1, 6, root)
    print(query(0, N-1, root).ans)

main()