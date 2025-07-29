# Pede os 2 números
B, C = map(int, input().split())

# mano eu nao acredito q é isso:
# Suponha A, B e C, de modo que A < B < C (ou seja, B é a mediana)
# Note que a mediana precisa ser igual a média, portanto:
# B = A + B + C / 3 ---> 2B = A + C. Como queremos achar A, temos
# A = 2B - C
print(2*B - C)