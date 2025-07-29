# Estratégia: Matemática

N = int(input())

cubos = N ** 3

faces = 6

# os cubos sem nada são os cubos dentro do cubo.
# dentro do cubo, há um cubo de lado N - 2
# (-2 pois retiramos a superfície)
sem_nada = (N - 2) ** 3

# os cubos pintados só com 1 face são os cubos
# no meio de cada face. A quantidade de cubos
# no meio de uma face é (N - 2) ^ 2
uma_face = faces * ( (N - 2) ** 2 )

# os cubos pintados com 3 faces são os das
# quinas, que são sempre 8.
tres_faces = 8


"""
As 2 formas de calcular a quantidade de duas_faces:
"""
# os cubos pintados com 2 faces são os
# que sobraram.
duas_faces = cubos - sem_nada - uma_face - tres_faces

# Se quiser calcular a quantidade de cubos com 2 faces pintadas,
# basta perceber que eles estão nas bordas/arestas do cubo, exceto
# os que estão nas quinas (que são pintados por 3 faces).
# Como, em cada "aresta", existem N-2 desses e, em cada
# face, existem 4 "arestas", o total de duas faces é
# faces * (4 * (N-2)). No entanto, uma "aresta" pertence
# a duas faces e, logo, estamos contando cada cubo 2 vezes.
# para corrigir isso, dividimos por 2.

duas_faces = faces * (4 * (N - 2)) // 2

print(sem_nada)
print(uma_face)
print(duas_faces)
print(tres_faces)

