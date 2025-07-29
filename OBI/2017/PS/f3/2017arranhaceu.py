# Número de pessoas até aquele andar (1 a k)
nPessoas = {}

# Pede o número de pessoas e eventos
N, E = list(map(int, input().split()))

# Lista com a quantidade
p = list(map(int, input().split()))

# inicializa nPessoas usando como base o anterior
for i in range(0, N):
    if i == 0:
        nPessoas[i] = p[i]
        continue
    nPessoas[i] = nPessoas[i-1] + p[i]
    
# para cada evento
for _ in range(E):
    # pede as entradas
    e = list(map(int, input().split())) 
    
    # verifica se é mudança ou bombeiro
    if len(e) == 2: # Bombeiro
        pass        
    else:           # Mudança
        pass
