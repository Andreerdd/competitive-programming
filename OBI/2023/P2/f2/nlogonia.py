# Estratégia: DSU (Disjoint set union)
# Algoritmo que une 2 ou mais sets que contém um
# elemento representativo (que liga todos)

def ler_linha_int(tx):
    return list(map(int, input(tx).split()))

N = int(input("Quantas ilhas? "))
B = int(input("Quantos barcos? "))
# Pede as conexões
conexoes = [ler_linha_int("Ilhas para ligar: ") for _ in range(B)]

C = int(input("Quantas consultas? "))
consultas = [ler_linha_int("Consulta: ") for _ in range(C)]

Parent = list(range(N + 1))                      # todos são seus próprios representantes
Rank = [0] * (N + 1)                             # Rank é, basicamente, a altura da árvore de representante i
consultas_com_node = [set() for i in range(N+1)] # As consultas que a ilha x participa estão em consultas_com_node[x]
respostas = [-1 for i in range(C)]               # a resposta da i-ésima consulta

# Coloca a dentro de b
def dsu_union(a, b, peso):
    # União por rank
    aroot = dsu_find(a)
    broot = dsu_find(b)
    
    if aroot == broot:
        return
    
    if Rank[aroot] < Rank[broot]:
        aroot, broot = broot, aroot
        
    Parent[broot] = aroot
    
    if Rank[aroot] == Rank[broot]:
        Rank[aroot] += 1
        
    trocou = False
    if len(consultas_com_node[aroot]) < len(consultas_com_node[broot]):
        aroot, broot = broot, aroot  # Swap para garantir que broot sempre tem menos consultas
        trocou = True
        
    for id in consultas_com_node[broot]:
        if id in consultas_com_node[aroot]:
            # Viu que b e a tem a mesma consulta, então encontrou o melhor caminho!
            consultas_com_node[aroot].remove(id)
            respostas[id] = peso
        else:
            # B tem essa consulta mas a não tem, então agora isso é problema do a!
            consultas_com_node[aroot].add(id)
        
    consultas_com_node[broot].clear()  # Limpamos pois já unimos ao maior conjunto
    
    if trocou:
        consultas_com_node[aroot], consultas_com_node[broot] = consultas_com_node[broot], consultas_com_node[aroot]

# Encontra o representante de x
def dsu_find(x):
    # Note que temos que achar um i tal que Parent[i] = i
    # Ao mesmo tempo que i é um pai de x. Portanto, se
    # Parent[x] != x, vamos ver se Parent[x] == Parent[Parent[x]]
    if Parent[x] != x:
        Parent[x] = dsu_find(Parent[x])
        return Parent[x]
    
    # Achou o representante     
    return Parent[x]

def solve():
    # Liga cada consulta a um "id"
    for i in range(C):
        x, y = consultas[i]
        consultas_com_node[x].add(i)
        consultas_com_node[y].add(i)
        
    # Ordena em ordem decrescente usando o 2+1 argumento (capacidade) como parâmetro
    conexoes.sort(key=lambda x: -x[2])
    for aresta in conexoes:
        a, b, cap = aresta
        dsu_union(a, b, cap) 
    
solve()
for s in respostas:
    print(s)