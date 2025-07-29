# Resolução 1 do Relógio
min_in_seg = 60

hora_in_min = 60
hora_in_seg = 60 * 60

H = int(input())
M = int(input())
S = int(input())
T = int(input())



t_h = T // hora_in_seg
T -= t_h * hora_in_seg

t_m = T // min_in_seg
T -= t_m * min_in_seg

t_s = T

S += t_s
M += S // 60
S %= 60

M += t_m
H += M // 60
M %= 60

H += t_h
H %= 24


print(H)
print(M)
print(S)