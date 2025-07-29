# Pede a quantidade
qntd = int(input())

# Cria um vetor dos números
nums = []
tamIntervalo = 0 # tamanho do intervalo atual
inicio = 1       # início do intervalo atual
maior = 0        # tamanho do maior intervalo

# Pede os números
for i in range(1, qntd+1):
    current = int(input())
    
    # Se o número escrito já está dentro do intervalo,
    # troca o início pra 1 posição depois da posição do número (já) escrito
    if current in nums[inicio:i]:
        inicio += nums[inicio:i].index(current) + 1
        
    # Tamanho do intervalo agora
    tamIntervalo = i - inicio
    
    # se o tamanho do intervalo agora for maior
    # que o maior intervalo, substitui
    if tamIntervalo > maior:
        maior = tamIntervalo
        
    # Adiciona na última posição o número digitado agora
    nums.append(current)
        
# Printa o resultado final
print(maior)