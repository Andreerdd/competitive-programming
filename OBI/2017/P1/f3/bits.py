# Estratégia: Programação Dinâmica
maxn = 1010
maxk = 1010
mod = 10e8 + 7

N, K = map(int, input().split())

# dp[n][v] = quantidade de sequências com n bits nas quais há v bits 1 consecutivos no final
dp = [[0] * maxk for _ in range(maxn)]
dp[1][0] = 1
if K > 1: dp[1][1] = 1

def calc(i):

    for x in range(2, i+1):
        dp[x][0] = sum(dp[x-1]) % mod

        for v in range(1, K):
            dp[x][v] = dp[x-1][v-1] % mod

    return dp[i]

print(int(sum(calc(N))))
