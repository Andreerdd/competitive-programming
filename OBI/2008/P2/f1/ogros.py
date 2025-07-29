# Estratégia: Busca Binária
#   Procuraremos no vetor de faixas qual o intervalo que o ogro
# atual está. Depois, obteremos sua pontuação no vetor de pontuações.
N,M = map(int, input().split())

faixas = [0] + list(map(int, input().split())) # a primeira faixa tem intervalo que começa em 0
pontuacoes = list(map(int, input().split()))
ogros = list(map(int, input().split()))

for og in ogros:
    l, r = 0, len(faixas)-1
    # se o ogro fez uma pontuação igual ou maior que
    # a maior faixa
    if og >= faixas[-1]:
        print(pontuacoes[-1], end=' ')
    else:
        # busca binária
        while l <= r:
            m = (l+r) // 2

            # se estiver dentro do intervalo de m e o seu antecessor,
            # achou a pontuação desse ogro
            if faixas[m-1] <= og < faixas[m]:
                print(pontuacoes[m-1], end=' ')
                break
            elif og >= faixas[m]:
                l = m+1
            elif og < faixas[m-1]:
                r = m-1



