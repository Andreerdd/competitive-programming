"""
Dadas duas sequências s1 e s2, uma de tamanho n e outra de tamanho m,
qual a maior subsequência comum às duas?

Por exemplo, se s1=[1, 2, 3, 4, 5] e s2 = [1, -2, 3, -4, -5, 5],
a maior subsequência é [1, 3, 5] (pois esses elementos aparecem
na mesma ordem nas duas sequência -- mas não necessariamente
adjacentes)

Estratégia: vamos olhar a maior subsequência que termina nas posições
j da sequência s1 e k da sequência s2, começando com j=n e k=m (ou
seja, do fim da sequência). A partir disso, olharemos os sub casos como
se são iguais (então somamos 1 à maior subsequência antes de j e k) ou
se são diferentes (então subtraímos 1 de a ou de b).
"""

maxn = 1010

N, M = map(int, input().split())

s1 = [0] + list(map(int, input().split()))
s2 = [0] + list(map(int, input().split()))

dp = [[-1 for _ in range(maxn)] for _ in range(maxn)]


def lcs(j, k):
    # Se já calculamos, retorna o já calculado
    if dp[j][k] != -1: return dp[j][k]

    # Se não é válido, retorna 0  
    if j <= 0 or k <= 0:
        dp[j][k] = 0
        return dp[j][k]

    # se s1[j] == s2[k], podemos adicionar na subsequência
    if s1[j] == s2[k]:
        dp[j][k] = 1 + lcs(j - 1, k - 1)
        return dp[j][k]

    # se chegou até aqui, são diferentes

    # se forem diferentes, retorna o máximo entre retirar de s1
    # e retirar de s2
    dp[j][k] = max(lcs(j - 1, k), lcs(j, k - 1))
    return dp[j][k]

print(lcs(N, M))

