"""
Segment Tree

Utilizada quando precisa-se obter algo de um intervalo (como soma ou maior valor) e precisa
atualizar o intervalo também.
Atualizar = O(log n)
Obter = O(log n)
"""
valores = [1, 2, 3, 4]

maxn = len(valores) * 2 + 1
tree = [0 for _ in range(maxn)]

"""
Constrói a Segment Tree em O(n)
"""
def construir(node: int = 0, l: int = 0, r: int = len(valores)-1):
    """
    Constrói a Segment Tree em O(n)

    :param node: o índice do nó atual na árvore
    :param l: início do intervalo
    :param r: fim do intervalo
    :return: None
    """
    # se l==r, então é uma folha, o que significa que o
    # intervalo é apenas de um elemento
    if l==r:
        tree[node] = valores[l] # ou valores[r]
        return

    # Calcula a média
    mid = (l+r)//2

    # Constrói os dois filhos
    construir(2*node+1, l, mid)   # filho da esquerda
    construir(2*node+2, mid+1, r) # filho da direita

    # Agora, já sabemos o valor dos 2 filhos do nó atual
    tree[node] = tree[2*node+1] + tree[2*node+2]


"""
Atualiza o valor no índice, de modo que
atualiza todo o resto da árvore
"""
def atualizar(index: int, valor: float, node: int = 0, l: int = 0, r: int = len(valores) - 1):
    """
    Atualiza o valor no índice, de modo que
    atualiza todo o resto da árvore

    :param index: o índice do que se quer alterar
    :param valor: valor o valor
    :param node: índice do nó atual na árvore
    :param l: o início do intervalo
    :param r: o fim do intervalo
    :return: None
    """
    # Se é uma folha
    if l==r:
        # Atualiza o valor da folha
        tree[node] = valor

        # Atualiza o valor no vetor
        valores[l] = valor
        return

    # Calcula a média
    mid = (l+r)//2

    # Verifica se o index está no intervalo entre l e mid
    # ou mid+1 e r
    if l <= index <= mid: atualizar(index, valor, 2*node+1, l, mid)
    else: atualizar(index, valor, 2*node+2, mid+1, r)

    # Atualiza o valor do nó atual
    tree[node] = tree[2*node+1] + tree[2*node+2]

"""
Obtém a soma dos elementos no intervalo dado
"""


def query(sl: int, sr: int, node: int = 0, l: int = 0, r: int = len(valores) - 1) -> float:
    """
    Consulta uma árvore de segmentos para encontrar a soma dos elementos em um determinado intervalo [sl, sr].

    Esta função realiza consultas de intervalo em uma estrutura de árvore de segmentos. Ela verifica se
    o intervalo solicitado está fora dos limites, completamente dentro dos limites, ou parcialmente sobreposto,
    para calcular a soma adequadamente.

    :param sl: Limite esquerdo do intervalo para a consulta
    :type sl: int
    :param sr: Limite direito do intervalo para a consulta
    :type sr: int
    :param node: Índice do nó atual na árvore de segmentos
    :type node: int
    :param l: Limite esquerdo do segmento representado pelo nó atual
    :type l: int
    :param r: Limite direito do segmento representado pelo nó atual
    :type r: int
    :return: A soma dos elementos no intervalo [sl, sr]
    :rtype: float
    """
    # Se está fora do intervalo
    if sr < l or sl > r: return 0

    # Se está totalmente dentro do intervalo
    if sl <= l and sr >= r: return tree[node]

    # Obtemos o índice que divide o nó atual em duas metades
    mid = (l + r) >> 1 # equivalente a (l+r) // 2

    return query(sl, sr, 2 * node + 1, l, mid) + query(sl, sr, 2 * node + 2, mid + 1, r)


def main():
    construir()
    print(tree)
    atualizar(1, 5)
    print(tree)
    s = query(0, 2)
    print(s)

main()