# N = quantidade de elementos no vetor
# Q = quantidade de perguntas
N, Q = map(int, input().split())

# Obtém o vetor
v = list(map(int, input().split()))

# A função de busca binária
def buscaBinaria(x) -> int:
    """
    Obtém a posição do elemento x no vetor v

    :param x: o elemento que se quer achar a posição
    :return: a posição do elemento x. Se não encontrar, retorna -1
    """

    # o intervalo de dúvida
    l, r = 0, N-1

    # enquanto o limite esquerdo do intervalo for
    # menor que o direito, ainda não sabemos a posição
    # do elemento x. Portanto, continuamos a procurar.
    while l <= r:
        meio = (l+r)//2 # calculamos o meio do intervalo

        # verificamos se o elemento do meio não é nosso alvo
        if v[meio] == x:
            return meio

        # vemos se o elemento no meio é maior que o nosso alvo
        elif v[meio] > x:
            # o elemento x está à esquerda do meio
            r = meio-1

        # vemos se o elemento no meio é menor que o nosso alvo
        elif v[meio] < x:
            # o elemento x está à direita do meio
            l = meio+1

    # se chegou até aqui, não encontrou o elemento
    return -1

# Obtém as perguntas
for _ in range(Q):
    i = int(input())
    print(buscaBinaria(i))

