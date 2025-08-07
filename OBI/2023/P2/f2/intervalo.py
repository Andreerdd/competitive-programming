N = int(input())

curr = {}
l, r = 0, 0
maior = 0

for i in range(N):
    e = int(input())

    # se não tiver no intervalo, só adiciona
    if not e in curr:
        curr[e] = i
        maior = max(maior, r-l+1)
        r += 1
    else:
        pos = curr[e] # a posição do número que já tá no intervalo

        if pos < l: # se ela não está no intervalo, só adiciona
            curr[e] = i
            maior = max(maior, r-l+1)
            r += 1
            continue

        l = pos+1
        r = i+1
        curr[e] = i

print(maior)



