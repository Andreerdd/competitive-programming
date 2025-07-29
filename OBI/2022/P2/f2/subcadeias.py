"""
--> Essa primeira estratégia foi a usada pela resposta na OBI <--
Estratégia:
digamos que estamos no caractere c (de posicao i). Procuramos o proximo
caractere c (que vai ter posicao j). Se houver, vemos se o caractere
de i+1 eh igual a j-1 . Se sim, vemos se o i+2 e j-2 sao iguais e assim
por diante. Se i + ??? == j - ??? (chegarmos na mesma posicao), eh palindromo
e, caso (j-i+1) for maior que o maior palindromo, o maior palindromo agora tem
esse tamanho.

obs.: usei 'l' em vez de 'i' e 'r' em vez de 'j' no codigo!

Meu código ficou:
maior = 1
for l in range(N): # left
    cl = txt[l]
    for r in range(l+1, N):
        cr = txt[r]
        if cl == cr:
            k = 1
            success = True
            while k < (r-l)/2:
                if txt[l+k] == txt[r-k]:
                    k += 1
                else:
                    success = False
                    break
            if success:
                if (r-l+1) > maior:
                    maior = r-l+1
                    
==================================================                    
                    
A estratégia do gemini envolve que:
- todo palindromo tem um centro
- começando do centro, veja se as quinas tem mesmo caractere
Assim, o algoritmo fica O(n²)
Código:
maior = 1
for c in range(N): # center
    l, r = c, c # left e right
    success = True
    
    # verifica pro caso que o tamanho do
    # palindromo eh impar
    while (l >= 0 and r < N and txt[l] == txt[r]):
        l -= 1
        r += 1
        
    if (l < 0): l = 0; r -= 1
    if (r >= N): l += 1; r = N-1
    
    if txt[l] == txt[r]:
        if (r-l+1 > maior):
            maior = r-l+1
    
    # verifica pro caso que o tamanho do
    # palindromo eh par
    l, r = c-1, c
    while (l >= 0 and r < N and txt[l] == txt[r]):
        l -= 1
        r += 1 
        
    if (l < 0): l = 0; r -= 1
    if (r >= N): l += 1; r = N-1
    
    if txt[l] == txt[r]:
        if (r-l+1 > maior):
            maior = r-l+1
            
=================================================
Estratégia de programação dinâmica (do gemini também):
- Temos um vetor P que salva se é palindromo da posição i a j.
  Por exemplo, se de i à j for palindromo, P[i][j] = True. Se nao,
  P[i][j] = False
- Note que, se i=j, P[i][j] = True (mesma posição = mesma letra = palindromo)
- Estratégia Divida e Conquiste: 
    Para P[a][b] ser palindromo, P[a+1][b-1] precisa ser palindromo e
    texto[a] == texto[b]
(o código foi usado DP)
"""


## Código usando DP ##
N = int(input())
txt = list(input())

# Inicializo P[i][i] como True  e    P[i][j] = False (i != j)
P = [[True if i==j else False for j in range(N)] for i in range(N)]

maior = 1
# começaremos do fim até o início para
# computar os menores subconjuntos até os maiores.
# Isso é uma forma de garantir que o valor 
# (P[i+1][j-1]) já tenha sido calculado (se for palíndromo)
for i in range(N-1, -1, -1):
    for j in range(N-1, i, -1):
        # se for a mesma letra
        if txt[i] == txt[j]: 
            # se o subconjunto entre eles for palíndromo
            # ou se forem duas letras consecutivas (tipo 'aa', 'bb')
            if P[i+1][j-1] or (j - i == 1):
                P[i][j] = True
                
                # não precisa dessa linha abaixo, já que o loop
                # nunca lerá P[j][i] (o loop só lê quando j>i):
                # P[j][i] = True 
                
                if (j-i+1) > maior:
                    maior = j-i+1
                    
print(maior)