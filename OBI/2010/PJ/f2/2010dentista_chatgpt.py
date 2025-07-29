N = int(input())
entradas = [tuple(map(int, input().split())) for _ in range(N)]

# Ordenar pelo horário de término (Y)
entradas.sort(key=lambda x: x[1])

res = 0
ultimo_fim = 0  # Mantém o fim da última consulta escolhida

for inicio, fim in entradas:
    if inicio >= ultimo_fim:
        res += 1
        ultimo_fim = fim  # Atualiza o fim da última consulta escolhida

print(res)