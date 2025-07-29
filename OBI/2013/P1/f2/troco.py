# Estratégia: Programação Dinâmica
#   Dado o valor final V, para cada moeda m, vamos
# ver se é possível chegar no valor V-m sem usar a moeda m.
# Se for, V-m+m=V e, então, conseguiremos chegar ao valor final,
# portanto imprimimos 'S'. Se em nenhum caso conseguirmos chegar
# em V, imprimimos 'N'.

V, M = map(int, input().split())
moedas = list(map(int, input().split()))


def pegar():

    dp = [False] * (V + 1)

    dp[0] = True

    for m in moedas:
        for j in range(V, m-1, -1):
            if dp[j - m]: dp[j] = True

    return dp[V]


if pegar(): print('S')
else: print('N')