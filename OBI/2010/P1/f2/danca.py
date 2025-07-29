# tá incompleto!
N, E = map(int, input().split())
indios = [0 for i in range(E)]
iniciais = {}
torasAgora = {}

for i in range(E):
    t,d = map(int, input().split())
    iniciais[t] =  t
    indios[i] = [t, d]

batidas = 0
while True:
    batidas += 1
    if torasAgora == iniciais:
        break

    proxTora = {}
    for i in indios:
        t, d = i
        prox = ((t + d) % N) + 1
        # verifica se vai pular na direção de alguém
        if prox in torasAgora:
            d *= -1
            prox = t
            proxTora[prox] = [prox, d]
            continue
        if prox in proxTora: # já tem alguém
            if proxTora[prox][1] != d: # direcao oposta
                proxTora[prox][1] *= -1
                proxTora[prox] = [proxTora[prox], [prox, -d]]
                continue
        else:
            proxTora[prox] = [t, d]
            continue

    torasAgora = proxTora
print(batidas)




