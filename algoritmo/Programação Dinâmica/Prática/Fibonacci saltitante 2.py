maxn = 1010
maxk = 510

n, k = map(int, input().split())
# dp[n][p] = quantas formas pode chegar ao degrau n de forma que o último passo tenha tamanho p+1


def fs(d):
    # v[0] = 1, o resto 0
    v = [1] + [0] * d


    # calcula cada forma
    for i in range(1, d+1):
        for j in range(1, min(i, k) + 1):
            v[i] += v[i-j]

    return v[d]



print(fs(n))