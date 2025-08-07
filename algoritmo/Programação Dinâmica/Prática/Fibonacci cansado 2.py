maxn = 1010
n = int(input(f"valor maximo: 1010\ndigite o valor de n:"))

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

def fc(c):
    # inicializa os valores base
    v = [1, 1, 2]

    # calcula cada valor
    for i in range(3, c+1):
        v.append(v[i-1] + v[i-3])

    return v[c]

print("considerando f(i) = f(i-1) + f(i - 3), obtemos: " + str(fc(n)))