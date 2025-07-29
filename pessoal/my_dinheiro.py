"""
Dado o conjunto de valores de n moedas de um país
e um dado valor V, decidir se é possível atingir o valor exato V usando essas moedas.
"""

N = int(input("Quantidade de moedas: ")) # Quantidade de moedas
F = int(input("Quer chegar: "))
chegou = False
moedas = list(map(int, input("Moedas: ").split()))

origin = moedas[0]

def tree(i, soma=0):
    # Verifica se chegou no final
    if (i >= N): return
    
    global chegou
    
    soma += moedas[i]
    
    # Verifica se a soma é suficiente
    if soma == F or (soma-origin) == F:
        chegou = True
        return
    
    # Pega as moedas de i+1 até o final
    for m in range(i+1, N):
        if not chegou: tree(m, soma)
    
# Começa a árvore do primeiro elemento
tree(0)

if chegou:
    print("S")
else:
    print("N")