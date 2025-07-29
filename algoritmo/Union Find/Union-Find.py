"""
Union-Find Algorithm é um algoritmo que trata elementos como
vértices de um grafo e une eles por meio de um elemento pai.
Ou seja, se pai[x] == pai[y], eles estão unidos no mesmo grafo.
Se pai[x] != pai[y], eles estão em grafos diferentes.
Um elemento é pai se e somente se pai[x] == x.

Olhemos o grafo abaixo:
    1
    |
    2
   /|\
  3 4 5

Se tivéssemos um vetor que guardasse o pai do i-ésimo elemento,
esse vetor seria:
parent[5] = 2
parent[4] = 2
parent[3] = 2
parent[2] = 1
parent[1] = 1

Ou seja:
"""
parent = [0, 1, 1, 2, 2, 2]
"""
No entanto, uma característica do Union-Find é que o pai de um elemento
é sempre a raiz do grafo. Ou seja, ao obter o parent de um elemento,
iriamos verificar se ele é pai de si mesmo. Se for, chegamos na raiz;
no entanto, se não for, iríamos olhar o pai desse elemento. Isso acontece
de forma recursiva até encontrar um elemento x tal que parent[x] = x. Logo,
aplicando isso no exemplo acima, teríamos que:
parent[5] = 2 -> parent[2] = 1 -> parent[1] = 1. Logo, parent[5] = 1
parent[4] = 2 -> parent[2] = 1 -> parent[1] = 1. Logo, parent[4] = 1
parent[3] = 2 -> parent[2] = 1 -> parent[1] = 1. Logo, parent[3] = 1
parent[2] = 1 -> parent[1] = 1. Logo, parent[2] = 1
parent[1] = 1. Logo, parent[1] = 1 (que é raiz).

Ou seja:
"""
parent = [0, 1, 1, 1, 1, 1]
"""
Todavia, sem otimização, o vetor seria algo como o visto antes:
"""
parent = [0, 1, 1, 2, 2, 2]
"""
Como esse vetor não está do jeito que queremos, precisaremos implementar
uma função que busca o verdadeiro pai do elemento x.
Em código, essa busca recursiva fica:
"""
def procurar(x):
    if parent[x] == x: # se for raiz
        return x  # encontrou o pai
    return procurar(parent[x]) # encontra o pai do "pai de x"

"""
Agora, lembra do primeiro exemplo:
    1
    |
    2
   /|\
  3 4 5
O vetor seria:

parent[5] = 2 -> parent[2] = 1 -> parent[1] = 1. Logo, parent[5] = 1
parent[4] = 2 -> parent[2] = 1 -> parent[1] = 1. Logo, parent[4] = 1
parent[3] = 2 -> parent[2] = 1 -> parent[1] = 1. Logo, parent[3] = 1
parent[2] = 1 -> parent[1] = 1. Logo, parent[2] = 1
parent[1] = 1. Logo, parent[1] = 1 (que é raiz).

Note que, ao fazer a busca para o elemento 5, por exemplo, fazemos a busca
para o elemento 2 e 1 também, que tem pai o elemento 1 (e o 5 também).
Nesse sentido, é possível otimizar a função lembrando que o pai de cada
elemento é a raiz do grafo que ele pertence:
"""
# Isso se chama "Path Compression"
def procurarOtimizado(x):
    if parent[x] == x: # se for raiz
        return x  # encontrou o pai
    parent[x] = procurarOtimizado(parent[x]) # o novo pai de x vai ser a raiz
    return parent[x] # retorna a raiz (que é o pai de x)

"""
Para unir um elemento ao grafo de outro, temos a função union:
"""
def union(a, b):
    parent[procurar(a)] = procurar(b)

"""
Também é possível otimizar em função da quantidade de filhos
que uma raiz tem.
"""
qntd_filhos = [] # aqui, salva a quantidade de filhos de cada raiz
def unionOtimizado(a, b):
    if qntd_filhos[a] > qntd_filhos[b]:
        a,b = b,a # troca, para o que tem mais filhos ser substituído
    parent[procurar(a)] = procurar(b)
    qntd_filhos[b] += qntd_filhos[a]