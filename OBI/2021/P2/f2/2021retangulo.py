# Quando é possível formar um retângulo?
#   Quando houver 2 pares de pontos que, ao serem ligados,
# formam uma corda que é o diâmetro (180º)

# Quando um par de pontos é um diâmetro?
#   Quando a distância entre eles (ao olhar da circunferência)
# é 180º (ou metade do perímetro)

N = int(input())

dist = list(map(int, input().split()))
somas = [sum(dist[:p]) for p in range(N)]

ht = sum(dist) / 2 # Half Total = metade do perímetro total

pares = 0
for i in somas:
    if i > ht:
        break
    if (i + ht) in somas:
        pares += 1
    if pares > 1:
        break
        
print('S' if pares > 1 else 'N')