# Resolução 2 do Relógio
min_in_seg = 60

hora_in_min = 60
hora_in_seg = 60 * 60

H = int(input())
M = int(input())
S = int(input())
T = int(input())

total = H * hora_in_seg + M * min_in_seg + S # total de segundos do jogo original
total += T

# Quantas horas tem em "total" segundos
H = total // hora_in_seg
total -= H * hora_in_seg # retira o que já contou

# Quantos minutos tem em "total" segundos
M = total // min_in_seg
total -= M * min_in_seg # retira o que já contou

# O que sobrou são os segundos
S = total

# Imprime formatado
print(H % 24)
print(M % 60)
print(S % 60)

