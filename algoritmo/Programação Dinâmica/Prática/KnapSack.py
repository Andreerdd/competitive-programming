"""
De maneira geral, um ladrão irá roubar uma casa com uma mochila que suporta um peso s.
Ele vê n objetos na casa e sabe estimar o peso pi e o valor vi de cada objeto i.
Com essas informações, qual o maior valor que o ladrão pode roubar sem rasgar sua mochila?
"""

S,N = map(int,input().split())
peso = []
valor = []
for _ in range(N):
    p, v = map(int,input().split())
    peso.append(p)
    valor.append(v)

maxs = 10010 # o máximo de peso que a mochila aguenta

# Inicializamos o vetor com -1 para indicar que
# não foi calculado ainda
dp = [[-1 for _ in range(maxs)] for _ in range(N)]

# i: a posição atual
# aguenta: quanto a mochila ainda aguenta
def pegar(i, aguenta):
    # Verificamos se já chegamos ao final ou não podemos
    # pegar mais nada
    if i >= N or not aguenta: return 0

    # Verifica se já calculou. Se já, retorna o
    # valor já calculado
    if dp[i][aguenta] != -1: return dp[i][aguenta]

    # O caso que não pega o objeto atual (continua
    # aguentando a mesma quantidade)
    nao_pega = pegar(i+1, aguenta)

    # O caso que aguenta
    pega = -1
    if aguenta >= peso[i]: # Só pode pegar se aguentar o peso
        pega = valor[i] + pegar(i+1, aguenta-peso[i])

    # Guarda o valor máximo no vetor dp
    dp[i][aguenta] = max(nao_pega, pega)

    # Retorna o valor máximo
    return dp[i][aguenta]

# Calcula a partir do primeiro elemento
print(pegar(0, S))