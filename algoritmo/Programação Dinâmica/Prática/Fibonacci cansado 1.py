maxn = 1010
n = int(input(f"valor maximo: 1010\ndigite o valor de n:"))

# dp[n][p] = quantas formas pode chegar ao degrau n de forma que o último passo tenha tamanho p+1
dp = [[-1, -1] for _ in range(maxn)]
dp[0] = dp[1] = [1, 0]
dp[2] = [1, 1]

# flag[n] = se já calculou o degrau n
flag = [False] * maxn
flag[0] = flag[1] = flag[2] = True


def fc(c):
    if flag[c]: return dp[c]

    flag[c] = True

    # calcula com 1 passo #
    # todas as formas de chegar no degrau anterior
    dp[c][0] = sum(fc(c-1))

    # calcula com 2 passos #
    # as formas de chegar no penúltimo degrau de forma que o último passo tenha tamanho 1
    dp[c][1] = fc(c-2)[0]

    # retorna o que calculou
    return dp[c]


print("com vetor dp, obtemos: " + str(sum(fc(n))))
