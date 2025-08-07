# Busca Binária

Imagine a seguinte questão:

Dado um vetor $v$ de inteiros de tamanho $N$ ordenado e $Q$ perguntas no estilo
_"Qual a posição do inteiro $i$ no vetor?"_, imprima a posição no vetor de cada
número $i$ (é garantido que todos os números $i$ estarão no vetor). Por exemplo, 
no vetor $v=[1,2,3,4,5]$, se as perguntas forem, respectivamente, 
"Qual a posição do inteiro 1 no vetor?" e "Qual a posição do inteiro 4 está no vetor?", 
a saída deverá ser:
```
0
3
```

Para resolver essa questão, você pode simplesmente percorrer o vetor usando um loop
for para cada pergunta e imprimir a posição de cada número $i$. Essa solução é razoável
quando o vetor não é tão grande ($N < 2000$, por exemplo), e/ou não há muitas perguntas 
($Q < 2000$, por exemplo) pois sua complexidade é $O(Q\cdot N)$. No entanto, 
e se o intervalo de $N$ for algo como $N \leq 10^{6}$ e de $Q$ for $Q \leq 10^{5}$? 
Você não conseguirá passar por todos casos!

Para resolver esse problema, usaremos uma informação muito importante: 
o vetor está ordenado. 

Inicialmente, note que nosso "intervalo de dúvida" está entre $[0, N-1]$, 
pois não sabemos onde o 9 está, mas sabemos que ele está no vetor. 

Assim, digamos que nós escolhemos uma posição $p$ aleatória dentro desse intervalo
de dúvida. Se $v[p]$ for menor que o valor que estamos procurando atualmente, 
podemos afirmar que qualquer valor antes da posição $p$ do vetor não será o valor que 
estamos procurando. Por exemplo, imagine o vetor $v=[6,7,8,9,10,11]$ e a pergunta 
*"O inteiro 9 está no vetor?"*. Digamos que $p = 2$, ou seja, $v[p]=8$, como $v[p] < 9$ (pois $8 < 9$), é possível
afirmar que o elemento 9 não vai estar na posição $p$, nem $p - 1$, nem $p - 2$, até o
início do vetor, pois todos os valores nessas posições também serão menores que 9. Note,
portanto, que, sabendo dessa informação, não precisaríamos passar por todas as posições
antes de $p$. A partir disso, podemos afirmar que o 9 está depois de $p$ e, também,
que o nosso intervalo de dúvida está entre $[p+1, N-1]$, ou seja, $[3, N-1]$.

Continuando nesse exemplo, vamos dizer que o valor de $p$, depois dessa verificação,
seja $p = 4$. Como $v[p] > 9$, (pois $v[p] = 10$), sabemos que o 9 não está depois da
posição $p$, visto que, como o vetor está ordenado, qualquer valor
em uma posição depois de $p$ também será maior que 9. Desse modo, sabendo dessa
informação, não precisaríamos passar por todas as posições depois de $p$. A partir
disso, podemos afirmar que o 9 está antes de $p$ e, também, que o nosso intervalo
de dúvida, agora, está entre $[3, p-1]$, ou seja, $[3, 3]$.

Portanto, como 9 não está antes da posição $2$ e nem depois da posição $4$, ele precisa 
estar depois de 2 e antes de 4, assim como nosso intervalo de dúvida mostra (o intervalo
de dúvida está entre $[3, 3]$). Logo, ele precisaria estar
na posição 3. Verificando $v[3]$, concluímos que 9 está sim no vetor _(uma vez
que $v[3] = 9$)_. Assim, imprimiríamos $3$.

Note que, dessa maneira que fizemos, nós só olhamos 2 posições do vetor, o que
deixou nossa verificação quase $O(1)$! No entanto, eu, propositalmente, escolhi as
posições logo antes e logo depois do 9 para mostrar o melhor caso dessa nossa estratégia
de "verificar se é maior ou menor do que o nosso _número alvo_". Em uma situação real,
como saber quais os melhores valores para verificar? A resposta é: em média, se
optarmos por sempre escolher o meio do intervalo que estamos em dúvida, vamos reduzir
pela metade o tamanho do intervalo de dúvida, transformando a complexidade do nosso
código em $O(\log{n})$.

Essa estratégia que acabamos de desenvolver é chamada de **Busca Binária** ou
**Pesquisa Binária**.

Em Python, o código desse algoritmo fica assim:
```Python
def buscaBinaria(x) -> int:
    """
    Obtém a posição do elemento x no vetor v

    :param x: o elemento que se quer achar a posição
    :return: a posição do elemento x. Se não encontrar, retorna -1
    """

    # o intervalo de dúvida
    l, r = 0, N-1

    # enquanto o limite esquerdo do intervalo for
    # menor que o direito, ainda não sabemos a posição
    # do elemento x. Portanto, continuamos a procurar.
    while l <= r:
        meio = (l+r)//2 # calculamos o meio do intervalo

        # verificamos se o elemento do meio não é nosso alvo
        if v[meio] == x:
            return meio

        # vemos se o elemento no meio é maior que o nosso alvo
        elif v[meio] > x:
            # o elemento x está à esquerda do meio
            r = meio-1

        # vemos se o elemento no meio é menor que o nosso alvo
        elif v[meio] < x:
            # o elemento x está à direita do meio
            l = meio+1

    # se chegou até aqui, não encontrou o elemento
    return -1
```

Veja a solução completa da questão dada no início fica assim:
```Python
N, Q = map(int, input().split())

# Obtém o vetor
v = list(map(int, input().split()))

# A função de busca binária
def buscaBinaria(x) -> int:
    """
    Obtém a posição do elemento x no vetor v

    :param x: o elemento que se quer achar a posição
    :return: a posição do elemento x. Se não encontrar, retorna -1
    """

    # o intervalo de dúvida
    l, r = 0, N-1

    # enquanto o limite esquerdo do intervalo for
    # menor que o direito, ainda não sabemos a posição
    # do elemento x. Portanto, continuamos a procurar.
    while l <= r:
        meio = (l+r)//2 # calculamos o meio do intervalo

        # verificamos se o elemento do meio não é nosso alvo
        if v[meio] == x:
            return meio

        # vemos se o elemento no meio é maior que o nosso alvo
        elif v[meio] > x:
            # o elemento x está à esquerda do meio
            r = meio-1

        # vemos se o elemento no meio é menor que o nosso alvo
        elif v[meio] < x:
            # o elemento x está à direita do meio
            l = meio+1

    # se chegou até aqui, não encontrou o elemento (se tivesse
    # achado, ia retornar no "if v[meio] == x") 
    return -1

# Obtém as perguntas
for _ in range(Q):
    i = int(input())
    print(buscaBinaria(i))
```