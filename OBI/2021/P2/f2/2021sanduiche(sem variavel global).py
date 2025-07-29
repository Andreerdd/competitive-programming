# Algoritmo:
#   Uma "árvore binária" que sempre verifica os próximos números
# (que são maiores), até ter chegado no número máximo (N+1).   ((o1))
# Por exemplo:
"""
     1                   2                3                4
    /|\                 3 4               4
   2 3 4               4
  /  |
  3  4  

"""
# A cada verificação, adiciona mais 1 no "total"
# Antes de cada verificação, é analisado se o ingrediente colocado
# pode realmente ser colocado ((o2))

def criarAlturaArvore(i, n_ing, pares, naoJunto = []):
    # Adiciona mais um ao total, já que, se chegou aqui, é porque é possível
    r = 1
    
    # Adiciona os que não podem estar juntos até agora
    naoJunto += pares[i]
    
    # Adiciona os próximos
    for k in range(i+1, n_ing + 1): # ((o1))
        if not (k in naoJunto):     # ((o2))
            r += criarAlturaArvore(k, n_ing, pares, naoJunto)
            
    return r


        
# N = n ingredientes
# M = n pares
N, M = map(int, input().split())

# Cria um dicionário de listas vazias
pares: dict = {i: [] for i in range(N+1)}

# Pede os pares
for p in range(M):
    a, b = map(int, input().split())
    pares[a].append(b)
    pares[b].append(a)
        
# Pra cada ingrediente, cria uma árvore
res = 0
for i in range(1, N+1):
    res += criarAlturaArvore(i, N, pares)

# Printa o total    
print(res)




lucas_alves = 30
def sei_la():
    # a variável lucas_alves não existe aqui!!!!
    # então, essa linha abaixo vai dar erro
    print(lucas_alves)
    
lucas_alves = 'lab verde'
sei_la()