# Algoritmo:
#   Uma "árvore binária" que sempre verifica os próximos números
# que são maiores, até não ter mais nenhum.
# Por exemplo:
"""
     1                   2                3                4
    /|\                 3 4               4
   2 3 4               4
  /  |
  3  4  

"""

total = 0

def criarAlturaArvore(i, n_ing, pares, naoJunto):
    # Adiciona mais um ao total, já que, se chegou aqui, é porque é possível
    global total
    total += 1
    
    # Se já chegou no maior ingrediente
    if i == n_ing:
        return
    
    # Adiciona os que não podem estar juntos até agora
    novoNaoJunto = naoJunto | pares[i]
    
    # Adiciona os próximos
    for k in range(i+1, n_ing + 1):
        if not (k in novoNaoJunto):
            criarAlturaArvore(k, n_ing, pares, novoNaoJunto)


        
# N = n ingredientes
# M = n pares
N, M = map(int, input().split())
pares: dict = {i: set() for i in range(N+1)}

# Pede os pares

for p in range(M):
    a, b = map(int, input().split())
    pares[a].add(b)
    pares[b].add(a)
        
# Pra cada ingrediente, cria uma árvore
res = 0
for i in range(1, N+1):
    criarAlturaArvore(i, N, pares, set())

# Printa o total    
print(total)

