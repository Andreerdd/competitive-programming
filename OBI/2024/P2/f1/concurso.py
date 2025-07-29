N,C = map(int,input().split())
v = list(map(int,input().split()))

v.sort()

# Da posição N-C até a última posição do vetor,
# há N - (N-C) = C pessoas, a quantidade de pessoas
# que o chefe quer que passe. Portanto, se a nota
# v[N-C] for a nota de corte, passarão C pessoas pelo
# menos.
print(v[N-C])



# Observação: eu pensei se seria uma boa ideia
# usar uma solução sem sort. No entanto, até
# a solução sem sort disponibilizada no site da OBI
# aborda algo com tempo ~O(n²). Essa solução aqui
# pode ter O(n log n) se o sort() estiver na média.