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

"""
Outra maneira de abordar esse problema é notar que:
- para um passo pequeno, pode se dar um passo grande ou um passo pequeno depois. Nesse
caso, o passo pequeno tem tamanho 1.
- para um passo grande, pode se dar apenas um passo pequeno depois. Nesse caso, podemos
agrupar esses 2 passos em 1 só estado que será de um passo de tamanho 2+1 = 3.

Com isso, é possível afirmar que
f(i) = f(i-1) + f(i - 3)
f(i - 1) -> formas de chegar com passo pequeno
f(i - 3) -> forams de chegar com passo grande 
"""

def fc2(c):
    # inicializa os valores base
    v = [1, 1, 2]

    # calcula cada valor
    for i in range(3, c+1):
        v.append(v[i-1] + v[i-3])

    return v[c]

print("considerando f(i) = f(i-1) + f(i - 3), obtemos: " + str(fc2(n)))