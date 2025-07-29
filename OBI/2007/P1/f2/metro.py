# Estratégia: Busca Binária
#   Testaremos os valores que podem ser o tamanho inteiro máximo
# da fatia que pode ser cortada. Nesse sentido, o menor valor é
# 1 e o maior é 10^4, já que, para o intervalo dado, um valor maior
# que 10^4 resultará em 0 pedaços.

N, M = int(input()), int(input())
paes = list(map(int, input().split()))

def calc(tamanho):
    """
    Calcula a quantidade de pedaços
    :param tamanho: o tamanho de cada pedaço
    :return: a quantidade de pedaços
    """

    # obtém a parte inteira da divisão de cada elemento
    cortar = lambda x: x // tamanho

    # executa a função cortar em cada pão
    pedacos = map(cortar, paes)

    # retorna a soma da quantidade de pedaços
    return sum(pedacos)

ans = 0

# busca binária
l, r = 1, 1e4
while l <= r:
    m = (l+r) // 2
    # calcula a quantidade de pedaços que se
    # pode ter com tamanho m
    p = calc(m)

    # se a quantidade de pedaços é maior ou igual
    # à quantidade necessária, salva e aumenta o
    # tamanho do pedaço (ao aumentar o tamanho mínimo do pedaço)
    if p >= N:
        ans = m
        l = m + 1

    # se a quantidade de pedaços é menor à
    # quantidade necessária, diminui o tamanho do
    # pedaço (ao diminuir o tamanho máximo do pedaço)
    elif p < N:
        r = m - 1

print(int(ans))

