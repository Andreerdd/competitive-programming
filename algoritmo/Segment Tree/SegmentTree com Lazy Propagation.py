"""
O Lazy Propagation garante que um nó (e seus filhos) só serão
atualizados se precisar. Isso se dá pois quando precisamos fazer
muitas atualizações em um vetor e estas são feitas em um intervalo,
podemos adiar algumas atualizações e realizá-las apenas quando
necessárias.

Para isso, guardamos as atualizações de um nó em um vetor (aqui,
chamado lz) com o mesmo tamanho de tree, o vetor da árvore, de modo que
as atualizações necessárias do nó tree[k] estão guardadas em lz[k].
"""