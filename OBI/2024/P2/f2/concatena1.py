# Estratégia:
# Se o intervalo pedido vai de l até r, e temos a e b nesse intervalo
# a soma desses 2 elementos estará na forma 10*a+b e 10*b+a.
# Nesse sentido, olhemos só para todas as somas que o elemento v[l] fará:
# (v[l]*10 + v[l+1]) + (v[l+1]*10 + v[l]) = 11(v[l] + v[l+1])
# (v[l]*10 + v[l+2] + (v[l+2]*10 + v[l]) = 11(v[l] + v[l+2])
# ...
# (v[l]*10 + v[r]) + (v[r]*10 + v[l]) = 11(v[l] + v[r])
# Note que, se somarmos tudo, vamos ter (l-r) elementos v[l]
# (pois, para cada elemento no intervalo que não seja v[l], ele
# será "somado" com v[l] em algum momento). Assim, a soma de todos
# os elementos v[l] será 11*(l-r)*v[l]. Generalizando para todos os
# elementos, temos que a soma do intervalo será:
#  11*(l-r)*( v[l] + v[l+1] + ... v[r] ).
#
# Otimização:
# Para não precisarmos somar de v[l] até v[r] toda vez que houver
# um pedido, podemos salvar a soma dos elementos de 0 até i em
# um vetor "soma". Logo, a soma dos elementos de l até r será:
# v[r] - v[l-1] = (v[0] + ... + v[r]) - (v[0] + ... + v[l-1]),
# de modo que só sobrará v[l] + v[l+1] + ... v[r].
#   Observação: se l = 0, l-1 = -1, o que, nesse caso, é uma posição
#   inválida. Portanto, se l <= 0, não retiramos a parte "v[l-1]"
#   (o que está certo na soma de intervalos/prefixos).


N, Q = map(int, input().split())
v = list(map(int, input().split()))
soma = [v[0]]
for i in v[1:]:
    soma.append(i + soma[-1])

while Q > 0:
    l, r = map(int, input().split())
    l -= 1
    r -= 1

    csoma = soma[r]
    if l > 0: csoma -= soma[l-1]

    print(csoma * 11 * (r-l))

    Q -= 1