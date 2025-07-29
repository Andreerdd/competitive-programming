# Programação Dinâmica
###### Recomendo ler na NOIC :)

## Introdução
Basic.amente, a estratégia é dividir para conquistar.

Por exemplo:

``
Faça uma função que calcule o n-ésimo valor de fibonacci. A função de fibonacci
é a função f(n) = f(n-1) + f(n-2), com f(1) = f(0) = 1.
``

Intuitivamente, o código ficaria:
```Python
def fib(n):
    if n == 1 or n == 0: return 1 
    # Ou até: if n < 2: return 1
    
    return fib(n-1) + fib(n-2)
```
No entanto, é fácil perceber que vamos calcular vários valores repetidamente, pois,
por exemplo, $fib(n-1) = fib(n-2) + fib(n-3)$, e já calcularíamos o valor de $fib(n-2)$
na função. Nesse sentido, é possível notar que, se lembrarmos dos nossos cálculos,
poderíamos obter um desempenho muito maior que evitaria recalcular muitos valores. Em
Programação Dinâmica, o nome disso é **Memoization**.

O nosso código ficaria assim ao implementar essa idéia de memória:
```Python
memoria = {}
def fib(n):
    # Verifica se já calculou. Se já calculou, retorna
    # o valor já calculado
    if n in memoria: return memoria[n]
    
    # Se chegou até aqui, não calculou esse valor.
    # Então, calcula e guarda na memória.
    memoria[n] = fib(n-1) + fib(n-2)
    
    # Retorna o valor calculado
    return memoria[n]
```
A complexidade desse código é $O(n)$. Comparado ao código de antes, que tinha complexidade
$O(2^n)$, fizemos um grande avanço.

Existem outras técnicas de Programação Dinâmica. Por exemplo, podemos apenas guardar os
últimos 3 valores para calcular o fibonacci de um número.


## Fibonacci cansado
**Considere o problema:**

O atleta Pisano está treinando em uma longa escadaria com $n$ degraus numerados
de $0$ (solo) até $n$ (topo). Ele começa no degrau $0$ e deseja alcançar o degrau
$n$, realizando apenas dois tipos de movimentos:
- Subir 1 degrau de cada vez.
- Subir 2 degraus de uma vez (um passo largo).

No entanto, devido ao esforço de um treino anterior, Pisano está exausto e não 
consegue dar dois passos largos consecutivos. Ou seja, não é permitido subir 
dois degraus de cada vez duas vezes seguidas.

Sua tarefa é determinar de quantas maneiras diferentes Pisano pode chegar ao 
topo da escada (degrau $n$), obedecendo às regras acima.

Inicialmente, vamos ignorar a exaustão de Pisano e considerar que ele pode
subir 2 degraus várias vezes seguidas. Assim, podemos perceber que a quantidade
de maneiras para ele chegar no degrau $i$ é a quantidade de vezes que ele pode
chegar no degrau $i-1$, anterior ao $i$, mais a quantidade de vezes que ele pode
chegar no degrau $i-2$, anterior ao $i-1$. Isso se dá pois, a partir do degrau
$i-1$, Pisano precisa subir apenas 1 degrau para chegar no degrau $i$ e, a partir
do degrau $i-2$, Pisano precisa subir 2 degraus para chegar no degrau $i$. Logo,
$f(i) = f(i-1) + f(i-2)$ -- _Isso te lembra alguma coisa?_. Essa igualdade é
exatamente Fibonacci! Ou seja, para resolver essa versão simplificada do
problema, basta fazer um código que calcule Fibonacci.

Vamos voltar ao problema que considera a exaustão de Pisano, ou seja, ele não
consegue dar dois passos largos consecutivos. Antes de ver as soluções que irei
propor aqui, tente pensar na sua solução.

### 1ª Solução




## KnapSack
O problema intitulado "KnapSack", ou problema da mochila, é considerado um dos mais comuns
em Programação Dinâmica. Em suma, seu enunciado é:

De maneira geral, um ladrão irá roubar uma casa com uma mochila que suporta 
um peso $s$. Ele vê $n$ objetos na casa e sabe estimar o peso $p_i$ e o valor $v_i$ de 
cada objeto $i$. Com essas informações, qual o maior valor que o ladrão pode 
roubar sem rasgar sua mochila?

A estratégia, aqui, é calcular todos os casos de forma eficiente. Imaginemos todos os
objetos em uma linha reta (assim como em um vetor). Se estamos na posição $i$, qual é o
melhor caso pegando apenas os itens na nossa frente?

Com esse raciocínio, podemos fazer uma função que considera o melhor caso se pegarmos ou
não pegarmos o objeto atual (de posição $i$):
```Python
N = ... # a quantidade de objetos
peso = [...] # os pesos dos objetos
valor = [...] # os valores dos objetos

# i: a posição atual
# aguenta: quanto a mochila ainda aguenta
def pegar(i, aguenta):
    # Verificamos se já chegamos ao final
    if i >= N: return 0
    
    # O caso que não pega o objeto atual (continua
    # aguentando a mesma quantidade)
    nao_pega = pegar(i+1, aguenta)
    
    # O caso que aguenta
    pega = -1
    if aguenta >= peso[i]: # Só pode pegar se aguentar o peso
        # Se pegar, diminui o peso que aguenta e soma o valor do objeto
        pega = valor[i] + pegar(i+1, aguenta-peso[i])
    
    # Retorna o máximo entre não pegar ou pegar
    return max(nao_pega, pega)
```
Note que, nesse caso, a complexidade é $O(2^n)$, pois, para cada objeto, temos duas
escolhas: pegar ou não pegar. Assim, o número de casos cresce exponencialmente
com o número de objetos. Esse caso facilmente ultrapassa o tempo limite dos corretores.

Para não calcularmos os mesmos casos várias vezes, podemos usar a técnica de
**Memoization**. Assim, guardamos os casos já calculados e evitamos recalcular eles.
Para isso, podemos criar um vetor $dp[i][aguenta]$ que guarda o valor máximo que o ladrão
pode pegar considerando os objetos $i$ até o final e a mochila que aguenta $aguenta$.
Assim, o código ficaria:
```Python
N = ... # a quantidade de objetos
peso = [...] # os pesos dos objetos
valor = [...] # os valores dos objetos

maxs = 10010 # o máximo de peso que a mochila aguenta

# Inicializamos o vetor com -1 para indicar que
# não foi calculado ainda
dp = [[-1 for _ in range(maxs)] for _ in range(N)]

# i: a posição atual
# aguenta: quanto a mochila ainda aguenta
def pegar(i, aguenta):
    # Verificamos se já chegamos ao final
    if i >= N: return 0
    
    # Verifica se já calculou. Se já, retorna o 
    # valor já calculado
    if dp[i][aguenta] != -1: return dp[i][aguenta]
    
    # O caso que não pega o objeto atual (continua
    # aguentando a mesma quantidade)
    nao_pega = pegar(i+1, aguenta)
    
    # O caso que aguenta
    pega = -1
    if aguenta >= peso[i]: # Só pode pegar se aguentar o peso
        pega = valor[i] + pegar(i+1, aguenta-peso[i])
    
    # Guarda o valor máximo no vetor dp
    dp[i][aguenta] = max(nao_pega, pega)
    
    # Retorna o valor máximo
    return dp[i][aguenta]
```
O nosso código agora tem complexidade $O(n \cdot s)$, onde $n$ é a quantidade de objetos
e $s$ é o peso máximo que a mochila aguenta. Isso porque, para cada objeto, temos que
calcular o máximo de peso que a mochila aguenta. Assim, o número de casos é
limitado pelo número de objetos vezes o peso máximo que a mochila aguenta.
Esse código é muito mais eficiente que o anterior.

Verifique esse código no arquivo [KnapSack.py](Prática/KnapSack.py).

## Maior Subsequência Comum
Dadas duas sequências $s_1$ e $s_2$, uma de tamanho $n$ e outra de tamanho $m$,
qual a maior subsequência comum às duas?



Por exemplo, se $s_1=[1, 2, 3, 4, 5]$ e $s_2 = [1, -2, 3, -4, -5, 5]$,
a maior subsequência é $[1, 3, 5]$ (pois esses elementos aparecem
na mesma ordem nas duas sequência _-- mas não necessariamente seus elementos são
adjacentes_).

Vamos definir uma função que retorna a maior subsequência que termina em $j$
em $s_1$ e $k$ em $s_2$.
Aqui, podemos dividir nosso raciocínio da seguinte forma:
- Se $s1[j] = s2[k]$, vamos ver se existe alguma subsequência já feita anterior 
a esses valores $j$ e $k$ e adicionamos +1 a ela _(se não houver, o tamanho da
subsequência será 1)_.
- Se $s1[j]\neq s2[k]$, vamos ver se existe alguma subsequência anterior a $j$
e $k$ retirando 1 de um desses valores e obteremos a maior dessas subsequências.

Você pode ver esse código no arquivo [Maior Subsequencia Comum.py](Pr%C3%A1tica/Maior%20Subsequencia%20Comum.py)
 