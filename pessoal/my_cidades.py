"""
São dadas cidades e as suas distâncias.
O objetivo é achar a menor distância da cidade A à B.
Uma cidade é representada de um número de 1 a N.
Uma conexão tem uma distância de 1 a 100000.
"""

infinito = 1000000

N = int(input("Quantidade de cidades: ")) + 1 # + 1 para ficar mais fácil olhar na lista
C = int(input("Quantidade de conexoes: "))

# A = cidade inicial, B = cidade final (a que se quer chegar)
A = int(input("Numero da cidade inicial: "))
B = int(input("Numero da cidade final: "))

# Cria um set para cada cidade e sua conexão com outra
conexoes = [[] for _ in range(N)]

# Cria um set para salvar o que já foi contado
ja_visto = set()

# Cria um set para salvar as distâncias de A até i
distancias = [infinito for _ in range(N)]

# Pede as cidades
print("Conexoes:") # No formato: {i} {j} {peso}
for _ in range(C):
    i,j,peso = map(int, input().split())
    conexoes[i].append((j, peso))
    conexoes[j].append((i, peso))
    

# Retorna o indice e o menor valor
def menor():
    minIdx, minVal = -1, infinito
    for i in range(1, N):
        if distancias[i] < minVal:
            # Verifica se já não foi visto
            if not (i in ja_visto):
                minVal = distancias[i]
                minIdx = i
            
    return minIdx
        
    
# Procura a menor conexão
def calcVizinhos(k): 
    
    # A distância de k
    peso_k = distancias[k]
    
    # Obtém os vizinhos de k
    vizinhos = conexoes[k]
    
    # Atualiza os vizinhos de k
    for i, peso in vizinhos:
        if (peso_k+peso) < distancias[i]:
            distancias[i] = peso_k+peso
    
    # Adiciona si mesmo
    ja_visto.add(k)

distancias[A] = 0
calcVizinhos(A)

while len(ja_visto) < (N-1):
    # Obtém a menor distância na lista
    minIdx = menor()
    
    # Verifica se não achou ninguém (já olhou tudo)
    if minIdx == -1:
        break
    elif minIdx == B:
        calcVizinhos(minIdx)
        break
    
    # Chama para o próximo menor
    calcVizinhos(minIdx)
    

print(distancias[B])
        

