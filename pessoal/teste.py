def lis(A):
    if len(A) < 2: return 1

    sub = {0: (1, A[0])} # o primeiro smp tem tamanho 1 e o maior e o ultimo

    for i in range(1, len(A)):
        curr = A[i]
        maior = 0
        for tam, val in sub.values():
            if curr > val and maior < tam:
                maior = tam
        sub[i] = (maior+1, curr)
        
    # obtem o maior
    maior = 0
    for tam, _ in sub.values():
        if tam > maior:
            maior = tam

    return maior


print(lis([1, 2, 1, 5]))