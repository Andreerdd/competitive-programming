# Estratégia: Two Pointers
N, D = map(int, input().split())
v = list(map(int, input().split()))

total = 0

def contar_contiguo():
    l,r = 0, 0
    soma = v[l]
    qntd = 0

    while l < N and r < N:
        if soma == D:
            qntd += 1

            soma -= v[l]
            l += 1

            r += 1
            if r >= N: break

            soma += v[r]
        elif soma < D:
            r += 1
            if r >= N: break

            soma += v[r]
        else:
            soma -= v[l]
            l += 1


    return qntd

def contar_extremidades():
    l, r = 0, 0
    qntd = 0


    psum = [v[0]]
    for i in range(1, N):
        psum.append(psum[-1] + v[i])

    ssum = [0] * N
    for i in range(N-1, -1, -1):
        if i == N-1: ssum[i] = v[i]
        else: ssum[i] = ssum[i+1] + v[i]

    while l <= r and l < N and r < N:
        soma = psum[l] + ssum[r]
        if l == r: soma -= v[r]
        if l == r == N - 1: break

        if soma == D:
            qntd += 1
            l += 1
            r += 1
        elif soma < D: l += 1
        else: r += 1


    return qntd

total += contar_contiguo()
total += contar_extremidades()

print(total)




