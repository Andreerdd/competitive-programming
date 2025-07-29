# Algoritmo:
#   Vamos dar prioridade a consultas que terminam mais cedo ((1)).
#   Depois disso, vamos ter um vetor "total" guardando se a
# hora i tem uma consulta já marcada (nesse caso, total[i] = 1)
# ou não (nesse segundo caso, total[i] = 0).
# Durante o processo de marcar as consultas, atualizaremos o vetor
# total.
#
# Como marcar uma consulta no vetor total?
#   Primeiro, nós deixamos como 0 tudo entre a última consulta do
# vetor total e o inicio de agora; depois, completamos com 1 até
# o fim da consulta de agora ((2))
#   Caso a consulta seja marcada entre 2 consultas já existentes,
# (considerando que não há interseção), substituímos os 0 por 1

total = [0]

N = int(input())
res = 0

entradas = [list(map(int, input().split())) for i in range(N)]

# ((1))
entradas = sorted(entradas, key=lambda x: x[1])

# Verifica os atendimentos
for i in range(N):
    inicio, fim = entradas[i]
    tempo = fim - inicio
    
    # Verifica se esse horário está livre
    if (len(total) - 1) <= inicio:
        # ((2))
        # Tá livre
        total += [0] * (inicio - len(total)) # (2)
        
        total += [1] * (tempo+(-1 if total[-1] == 1 else 0))
        res += 1
        continue
    
    if (len(total) - 1) > inicio:
        # ((3))
        if sum(total[inicio:fim]) == 0: # verifica se existe algum elemento diferente de 0
            res += 1
            for r in range(inicio, fim):
                 total[r] = 1
            continue
                
print(res)