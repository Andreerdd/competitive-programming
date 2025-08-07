# Estratégia: Line Sweep
N = int(input())

# adiciona 0 no início e no fim pra ficar mais fácil
ent = list(map(int, input().split()))

# retira duplicatas
cortes = [0]
for i in range(N):
    if ent[i] != cortes[-1]:
        cortes.append(ent[i])
cortes.append(0)

# pico: une os dois lados. Então é -1 corte
# vale: separa os dois lados. Então é +1 corte
pv = []
for i in range(1, len(cortes)-1):
    # se é pico
    if cortes[i-1] < cortes[i] > cortes[i+1]:
        pv.append((cortes[i], -1))
    # se é vale
    if cortes[i-1] > cortes[i] < cortes[i+1]:
        pv.append((cortes[i], 1))

pv = sorted(pv, key=lambda x:x[0]) # ordeno em ordem crescente de altura
curr = ans = 2
for k in pv:
    curr += k[1]
    ans = max(curr, ans)

print(ans)
