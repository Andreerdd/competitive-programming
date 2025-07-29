N,K = map(int, input().split())
nomes = []
for _ in range(N):
    nomes.append(input())

nomes.sort()
print(nomes[K-1])