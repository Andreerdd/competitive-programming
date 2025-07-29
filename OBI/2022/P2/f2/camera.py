# colunas, linhas, câmeras
N,M,K = list(map(int, input().split()))

# cameras[lin][col]
cameras = {i: dict() for i in range(1,M+2)}

for _ in range(K):
    c,l,d = input().split()
    c,l = int(c),int(l)
    i, j = 0, 0
    
    # Define a direção que vai andar
    if d == 'N': i,j = 0,-1
    elif d == 'S': i,j= 0,1
    elif d == 'L': i,j= 1,0
    elif d == 'O': i,j= -1,0

    while (c > 0 and l > 0 and c <= N and l <= M):
        cameras[l][c] = True
        c += i
        l += j


for i in range(1, M+1):
    for j in range(1, N+1):
        if j in cameras[i]:
            print("(X)",end='')
        else:
            print("( )",end='')
    print()


# visitou[lin][col]
visitou = {i: dict() for i in range(1, M+2)}
conseguiu = False

# i = linha
# j = coluna
def andar(i, j):
    if i > M+1 or j >= N+1 or i < 1 or j < 1: return
    if j in visitou[i] : return
    visitou[i][j] = True
    if j in cameras[i]:
        # Nao conseguiu
        return 
    global conseguiu
    if conseguiu: return
    if j == N and i == M+1: 
        conseguiu = True
        return
    
    andar(i+1, j)
    andar(i, j+1)
    andar(i-1, j)
    andar(i, j-1)


andar(1,1)
print('S' if conseguiu else 'N')