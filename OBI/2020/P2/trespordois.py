# Algoritmo:
#   É lucro se não pagarmos por um caro a um barato.
#   Que tal minimizar a quantidade de caros pagos?
#   Isso acontece quando o "caro" é o menor no grupo, então
# pegamos os 3 maiores não utilizados e colocamos em um grupo

N = int(input())

entradas = [int(input()) for _ in range(N)]
entradas = sorted(entradas, reverse=True)

total = 0
# Cria os grupos
i = 0
while (True):
    if (N - i) < 3:
        total += sum(entradas[i:N])
        break
    total += sum(entradas[i:i+2])
    i += 3
    
print(total)
