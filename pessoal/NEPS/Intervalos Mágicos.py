"""
Estratégia: Two Pointers
"""

N, K = map(int, input().split())
v = list(map(int, input().split()))

ans = 0
l, r = 0, 0
soma = v[0]

while l <= r:
    if l >= N or r >= N: break

    if soma == K:
        ans += 1

        l += 1
        soma -= v[l-1]

        r += 1
        if r >= N: break
        soma += v[r]

        continue

    if soma < K:
        r += 1
        if r >= N: break
        soma += v[r]

        continue
    if soma > K:
        if l == r:
            l += 1
            soma -= v[l-1]
            r += 1
            if r >= N: break
            soma += v[r]
        else:
            l += 1
            soma -= v[l-1]

print(ans)