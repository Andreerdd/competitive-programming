N, X = map(int, input().split())
v = {i: i for i in range(N)}

c = 0
res = False
while c < N:
    if (X-v[c]) in v: 
        res = True
        break
    c += 1
    
print(res)