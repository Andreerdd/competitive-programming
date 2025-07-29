# Estratégia: Union-Find
#
# Inicialmente, vamos processar os monstros do menor para o
# maior em função de seu poder.
# Vamos organizar os monstros em grupos de forma que,
# dado um dos componentes m do grupo, a soma do poder de
# todos os outros componentes do grupo é igual ou maior
# que m. Assim, garantimos que sempre há um componente que,
# partindo desse elemento, é possível matar os outros.
# Além disso, se um monstro m entrar em um grupo v em que a soma
# dos poderes de todos os monstros do grupo v for menor que o
# poder desse monstro m, por causa do jeito que processamos, o
# poder máximo dos componentes desse grupo já foi obtido. Portanto,
# podemos criar um novo grupo com apenas o monstro m e com a soma
# dos poderes do grupo antigo + o poder do monstro m.

N,M = map(int, input().split())

monstros = {}           # os monstros
monstrosOrdenados = []  # os monstros em ordem de poder
parent = {}             # parent[x] = o pai da posição x no grupo que ele participa
componentes = {}        # componentes[y] = os componentes do grupo que y é pai
soma = {}               # soma[z] = a soma do grupo que z é pai
respostas = {}          # respostas[w] = poder máximo obtido se começar de w

# Obtém os monstros
for l in range(N):
    linha = list(map(int, input().split()))
    for c in range(M):
        pos = (l, c)
        poder = linha[c]

        monstros[pos] = poder
        parent[pos] = pos
        componentes[pos] = [pos]
        soma[pos] = poder
        respostas[pos] = poder
        monstrosOrdenados.append((poder, pos))


monstrosOrdenados.sort(key=lambda x: x[0])

def find(v):
    if parent[v] == v:
        return v
    parent[v] = find(parent[v]) # compressão
    return parent[v]

# une o grupo a ao grupo b
def union(a, b):
    pa = find(a)
    pb = find(b)

    if pa == pb: return # se tiverem o mesmo pai

    # prioriza ser o novo pai quem tiver mais elementos
    # (para ter a menor mudança possível, economizando desempenho)
    if len(componentes[pa]) > len(componentes[pb]):
        pa, pb = pb, pa

    # o pai da "raiz do grupo a" é a "raiz do grupo b"
    parent[pa] = pb

    # passa os componentes do grupo a para o b
    componentes[pb].extend(componentes[pa])

    # adiciona o poder do grupo a no grupo b
    soma[pb] += soma[pa]

    # limpa o grupo a (pois ele não existe mais, agora seus
    # elementos pertencem ao grupo b)
    componentes[pa].clear()

movimentos = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for monstroAtual in monstrosOrdenados:
    # poder e posição do monstro atual
    p, pos = monstroAtual
    l,c = pos

    # verifica os vizinhos
    for i,j in movimentos:
        viz = (l+i, c+j)

        # verifica se o vizinho está fora do tabuleiro
        if viz[0] < 0 or viz[0] >= N or viz[1] < 0 or viz[1] >= M:
            continue

        # verifica se tá ativo. A única forma de estar ativo
        # é se o poder do vizinho for menor que o monstro atual.
        if not (monstros[viz] <= p): continue # o vizinho não está ativo ainda

        vizpai = find(viz)

        # verifica se o monstro atual consegue entrar no grupo do vizinho
        if p <= soma[vizpai]:
            # apenas une ao grupo, já que o monstro atual não
            # pode fazer nada (todos os componentes do grupo do vizinho
            # podem matar o monstro atual. Isso é garantido, já que
            # podem matar entre si para conseguir o poder para matar
            # o vizinho)
            union(pos, vizpai)

        # se o poder do monstro atual for maior que a soma
        # de todos os poderes, nem se todos os monstros do
        # grupo "matarem entre si", vão obter o poder
        # necessário para matar o vizinho.
        else:
            # fixa a resposta dos componentes do grupo
            for comp in componentes[vizpai]:
                respostas[comp] = soma[vizpai]
            # limpa todos os componentes do vizinho
            componentes[vizpai].clear()
            # une o vizinho e o atual
            union(pos, vizpai)


# Obtém a resposta do último grupo
ultpai = find(monstrosOrdenados[-1][1])
for comp in componentes[ultpai]:
    respostas[comp] = soma[ultpai]

# Imprime a resposta
for l in range(N):
    linha_out = [str(respostas[(l, c)]) for c in range(M)]
    print(" ".join(linha_out))

