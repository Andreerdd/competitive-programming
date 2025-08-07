maxn = 1010
maxk = 510

n, k = map(int, input().split())
# dp[n][p] = quantas formas pode chegar ao degrau n de forma que o último passo tenha tamanho p+1

dp = [[0] * maxk for _ in range(maxn)]
dp[0][0] = dp[1][0] = 1 # só pode chegar no primeiro degrau dando 1 passo
dp[2][0] = dp[2][1] = 1 # pode chegar no 2 degrau dando 2 passos de tamanho 1 ou 1 passo de tamanho 2

# flag[n] = se já calculou o degrau n
flag = [False] * maxn
flag[0] = flag[1] = flag[2] = True

def fs(d):
    if d < 0: return [0]
    if flag[d]: return dp[d]
    flag[d] = True

    # calcula cada forma
    for i in range(1, k+1):
        dp[d][i] = sum(fs(d - i))

    return dp[d]


print(sum(fs(n)))