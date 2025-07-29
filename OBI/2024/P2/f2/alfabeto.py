K, N = map(int, input().split())
alfabeto = set(input())
msg = set(input())
if msg == alfabeto or msg.issubset(alfabeto):
    print('S')
else:
    print('N')