# Árvore Geradora Mínima

Imagine um grafo qualquer com $v$ vértices (nós) conectados por arestas de
forma que a $i$-ésima aresta tenha peso $p_i$. Qual é a melhor forma de conectar
todos os $v$ vértices e minimizar a soma total dos pesos das arestas usadas?

Note que, para responder a essa pergunta, nós precisamos de um grafo que:
- Seja possível ir de qualquer nó a outro qualquer nó;
- O peso total _(soma de todos os pesos das arestas usadas)_ seja 
o menor possível.

Perceba que, nesse caso, teríamos um grafo de **árvore**. A essa árvore, damos
o título de Árvore Geradora de Custo Mínimo _(ou AGM, Árvore Geradora Mínima)_.

Para formar uma AGM _(ou MST, do inglês "Minimal Spanning Tree")_, precisamos,
então, de um algoritmo que priorize as arestas com menor peso (se não, podemos
fazer uma conexão de 2 nós usando arestas com pesos maiores do que o necessário).
Logo, para o nosso algoritmo, o primeiro passo é **ordenar as arestas em função
do peso**.

Com as arestas já ordenadas, podemos começar a unir os vértices a partir dessas
conexões. Nesse momento, precisamos saber se já conectamos dois nós. Um algoritmo
que nos satisfaz, nesse caso, é o Union-Find _(encontrar o pai e unir dois vértices
é prático)_. Portanto, um pseudocódigo para essa parte do algoritmo seria:

```
def construir_AGM(arestas_ordenadas):
    mst <- []
    para cada aresta ar em arestas_ordenadas:
        a, b, peso <- ar
        
        se pai(a) != pai(b) então
            unir(a, b)
            
            Adiciona ar na mst
        fim se
    fim para
        
    retorna mst
```

Ao executar essa função `construir_AGM()`, você terá construído a respectiva AGM.
Você pode conferir o código completo aqui: 
[Algoritmo de Kruskal.py](Algoritmo%20de%20Kruskal.py).
