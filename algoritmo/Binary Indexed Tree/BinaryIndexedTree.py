"""
Binary Indexed Tree (BIT)

Uma Segment tree (árvore de segmento) com a indexação feita
a partir do pressuposto que todo número pode ser escrito como
uma soma de potências de 2. Nesse sentido, ao invés de ser
organizado na forma "2n+1", como na Segment Tree, é organizado
na forma "n - (menor potência de 2 na soma de n por potências de 2)".
Por exemplo, se fossemos dar query(13), as posições do vetor
que iriam ser olhadas são:
Dado que: 13 = 2^3 + 2^2 + 2^0 = 8 + 4 + 1

Primeiramente, a posição (2^3+2^2+2^0) - 0 = 13
Depois, a posição (2^3 + 2^2 + 2^0)-2^0 = 13 - 1 = 12
Depois, a posição (2^3 + 2^2) - 2^2 = 12 - 4 = 8
"""

valores = [0, 1, 2, 3, 4, 5] # 1-based indexing ( o primeiro elemento não vale )
tree = [0] * (len(valores))

"""
Atualiza o valor de um índice
"""
def update(idx: int, valor: int):
    valores[idx] = valor
    add(idx, valor - valores[idx])

"""
Adiciona um valor a um elemento na árvore
"""
def add(idx: int, valor: int):
    """
    Atualiza um elemento na árvore adicionando o valor dado

    :param idx: o índice
    :param valor: o valor a somar naquele elemento
    """
    curr = idx

    while curr < len(tree) :
        tree[curr] += valor
        curr += curr & -curr

def query(idx: int):
    total = 0
    curr = idx

    while curr > 0:
        total += tree[curr]
        curr -= curr & -curr

    return total

def between(x, y) -> int:
    if x > y: x, y = y, x
    return query(y) - query(x-1)



def main():
    # Carrega a árvore
    for i in range(1, len(valores)):
        add(i, valores[i])

    # Testa
    print(query(3))
    update(1, 5) # troca o valor
    print(query(3))
    add(1, 1) # adiciona mais um
    print(query(3))

main()