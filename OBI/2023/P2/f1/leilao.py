N = int(input())
parts = []

maxv, maxnome = -1, ""
for i in range(N):
    nome = input()
    val = int(input())
    if val > maxv:
        maxv = val
        maxnome = nome

print(maxnome)
print(maxv)
