# A operação Bitwise Left-Shift é feita com <<. Essa operação muda a
# representação binária do operando esquerdo para a esquerda pelo número
# de posições especificadas pelo operando direito. Por exemplo, 1 << 5
# representa 10000, e 5 << 2 representa 101 << 2 = 10100(binário) = 20(decimal)

# A operação Bitwise Right-Shift é feita com >>. Os bits do número binário
# à direita do operador são deslocados para a direita pelo número de posições
# especificadas pelo número inteiro no lado direito do operador >>. Assim,
# 4 >> 1 = 100 >> 1 = 10(binário) = 2(decimal); da mesma forma,
# 20 >> 2 = 10100 >> 2 = 101(binário) = 5(decimal).

# Para chegar se o bit k de um número N está ligado, use: N & 2^k   (and binário)
def estaLigado(N, k):
    return N & (1 << k) # 2^k = 1 << k

# Para ligar o bit k de um número N, use: N | 2^k     (or binário)
def ligar(N, k):
    return N | (1 << k)

