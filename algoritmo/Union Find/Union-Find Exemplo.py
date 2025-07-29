# DSU (Disjoint set union)
# Algoritmo que une 2 ou mais sets que contém um elemento representativo (que liga todos)

def create_parent_array(n):
    # Parent[i] = i -> i é representativo
    Parent = []
    
    for i in range(n):
        # Todos são representativos de si mesmo
        Parent.append(i)
    
    return Parent

Parent = create_parent_array(5) # Mesma coisa que [i for i in range(n)]


# Coloca a dentro de b
def dsu_union(a, b):
    # Pega o representativo de b e coloca como filho do representativo de a
    Parent[dsu_find(a)] = dsu_find(b)

def dsu_find(x):
    # Note que temos que achar um i tal que Parent[i] = i
    # Ao mesmo tempo que i é um pai de x. Portanto, se
    # Parent[x] != x, vamos ver se Parent[x] == Parent[Parent[x]]
    if Parent[x] == x:
        return x
    else:
        return dsu_find(Parent[x])

# Faz essa relação
"""
    0
   / \
  1   2
"""
Parent[1] = 0
Parent[2] = 0

# Faz essa outra relação
"""
    4
    |
    3
"""
Parent[3] = 4

# Note que Parent[4] = 4 e Parent[0] = 0 por natureza!

op = '0'
while op != 'S':
    op = input('Unir(U), Achar(F) ou sair(S)? ')
    match (op):
        case 'U':
            nodes = list(map(int, input("Quer unir quais 2 elementos? ").split()))
            if len(nodes) < 2:
                print("Digite algo valido!")
                continue
            a = nodes[0]
            b = nodes[1]
            print(dsu_union(a, b))
            
        case 'F': # Encontrar
            node = int(input("Quer saber o pai de qual? "))
            print(dsu_find(node))
            
        case 'S':
            print("Parando..\n")
            break
        
        case _:
            print("Digite U, F ou S maiusculo!")

