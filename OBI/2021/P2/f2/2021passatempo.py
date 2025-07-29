# acho q : número de colunas = número de variáveis

# A estratégia óbvia é descobrir uma variável por vez

# Como achar a linha/coluna inicial?
#   Uma matriz L*C que, a posição matriz[l][c] guarda um dicionário
# que contém a quantidade de cada variável. (outro dicionário vai
# cuidar da soma das linhas e colunas)
#   Se essa linha/coluna tem apenas 1 variável, ela já é instanteaneamente
# adicionada à fila para verificar agora

# Como descobrir as proximas linhas e colunas?
#   Se, após descobrir uma variável e substituir ela nas
# outras linhas e colunas, a respectiva linha/coluna tiver
# 1 variável só, essa linha/coluna é adicionada à fila

# Como salvar o valor descoberto?
#   Um dicionário guardará o valor da estrutura {"<var>": val}



# Pede o número de linhas e de colunas
L, C = map(int, input().split())

# Tabuleiro Linha x Coluna
tabuleiro_linhas =  [{} for _ in range(0, L)] 
tabuleiro_colunas = [{} for _ in range(0, C)]

# Guarda as somas
somas_linhas = [0] * L
somas_colunas = [0] * C

# Vetor que cuida da linha/coluna que será verificada
verificacao = []

# Dicionário dos valores conhecidos
valores = {}

def substituir(_var, valor):
    # verifica se tem alguma linha com essa variável
    for x in range(0, L):
        if _var in tabuleiro_linhas[x]:
            qntd = tabuleiro_linhas[x][_var]
            somas_linhas[x] -= qntd * valor
            tabuleiro_linhas[x].pop(_var)
            
            # Verifica se agora tem 1 variável nessa linha. Se sim, adiciona no verificacao
            # Se não, faz nada, pois:
            #       se for 0, já verificou a variável dessa linha (vai verificar atoa)
            #       se for 2 ou +, não adianta nada
            if (len(tabuleiro_linhas[x]) == 1):
                verificacao.append({'x': x})
            elif (len(tabuleiro_linhas[x]) == 0):
                verificacao.remove({'x': x})
            
    # verifica agora uma colunas
    for y in range(0, C):
        if _var in tabuleiro_colunas[y]:
            qntd = tabuleiro_colunas[y][_var]
            somas_colunas[y] -= qntd * valor
            tabuleiro_colunas[y].pop(_var)
            
            # Verifica se agora tem 1 variável nessa coluna. Se sim, adiciona no verificacao
            # Se não, faz nada, pois:
            #       se for 0, já verificou a variável dessa coluna (vai verificar atoa)
            #       se for 2 ou +, não adianta nada
            if (len(tabuleiro_colunas[y]) == 1):
                verificacao.append({'y': y})
            elif (len(tabuleiro_colunas[y]) == 0):
                verificacao.remove({'y': y})

# Pede os elementos e armazena eles nas linhas
for x in range(0, L):
    entrada = input().split()
    
    vs = entrada[:-1]
    soma = int(entrada[-1]) # último elemento é a soma
    
    # Já salva a soma obtida
    somas_linhas[x] = soma 
    
    # Coloca cada variável na matriz
    for y in range(0, C):
        vl = vs[y]
        
        # Linhas
        if vl in tabuleiro_linhas[x]:
            # Essa variável já existe na linha
            tabuleiro_linhas[x][vl] += 1
        else:
            # Essa variável não existe na linha, então adicionamos
            tabuleiro_linhas[x][vl] = 1
            
        # Colunas
        if vl in tabuleiro_colunas[y]:
            # Essa variável existe na coluna
            tabuleiro_colunas[y][vl] += 1
        else:
            # Essa variável não existe na coluna
            tabuleiro_colunas[y][vl] = 1
    
    # Determina se esse vai ser ou não um dos primeiros a
    # serem verificados
    if (len(tabuleiro_linhas[x]) == 1):
        # Se tiver apenas 1 variável
        verificacao.append({'x': x})
    
# Se tiver colunas com apenas 1 variável, adiciona elas ao
# vetor de verificacao
for y in range(0, C):
    if (len(tabuleiro_colunas[y]) == 1):
        verificacao.append({'y': y})

# Pede a soma das colunas
somas_colunas = list(map(int, input().split()))
        
# A estratégia aqui é:
#   Verifica todas as linhas/colunas que, AGORA, estão com 1 variável.
# Após definir o valor dessa variável, a variável nas linhas/colunas
# com essa variável será substituida pelo seu valor!
#   Nesse sentido, o loop abaixo só termina quando não for possível
# verificar mais nenhuma linha ou coluna!
i = 0 # variável que vai cuidar do que tá olhando agora
while (len(verificacao) > 0 and i < len(verificacao)):
    _var = '' # indefinido por enquanto
    valor_var = -1
    if 'x' in verificacao[i]: # Se for linha
        pos = verificacao[i]['x']
        
        # transforma em lista pra obter o nome da variável
        _var = list(tabuleiro_linhas[pos])
        if not _var:
            continue
        _var = _var[0]
        
        # Obtém a quantidade
        qntd = tabuleiro_linhas[pos][_var]
        
        # Determina o valor da variável
        valor_var = int(somas_linhas[pos] / qntd)
        
        # Retira essa linha da contagem de linhas (pois já verificou tudo dela),
        # ter ela seria só perda de tempo
        tabuleiro_linhas[pos] = {}
        
        # Substitui nas linhas e colunas
        substituir(_var, valor_var)
    else: # se não é linha, só pode ser coluna
        pos = verificacao[i]['y']
        
        # transforma em lista pra obter o nome da variável
        _var = list(tabuleiro_colunas[pos])
        if not _var:
            continue
        _var = _var[0]
        
        # Obtém a quantidade
        qntd = tabuleiro_colunas[pos][_var]
        
        # Obtém o valor daquela variável
        valor_var = int(somas_colunas[pos] / qntd)
        
        # Retira a coluna pra n perder tempo
        tabuleiro_colunas[pos] = {}
        
        # Substitui nos outros lugares
        substituir(_var, valor_var)
    
    # Adiciona no dicionário
    valores[_var] = valor_var    
        
    i += 1 # Pula pra próxima verificação

# Organiza as keys em ordem alfabética
sorted_keys = sorted(list(valores.keys()))

# Printa o resultado
for k in sorted_keys:
    print(k, valores[k])