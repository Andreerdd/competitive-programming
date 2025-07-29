"""
SegmentTree

Dado um vetor com N elementos, ache o menor elemento no intervalo
[i, j], com 0 <= i < j <= N.
"""

inf = 10e7

N = int(input())
v = list(map(int, input().split()))
tree = [0 for _ in range(4 * N)]

def build(tl=0, tr=N-1, no: int = 0):
    if tl == tr:
        tree[no] = v[tl]
        return

    mid = (tl + tr) >> 1
    build(tl, mid, 2*no+1)
    build(mid+1, tr, 2*no+2)

    tree[no] = min(tree[2*no+1], tree[2*no+2])

def query(l, r, tl=0, tr=N-1, no: int = 0):

    # fora do intervalo
    if tr < l or tl > r: return inf

    if tl >= l and tr <= r: return tree[no]

    mid = (tl + tr) >> 1

    return min(query(l, r, tl, mid, 2*no+1), query(l, r, mid+1, r, 2*no+2))

def main():
    build()
    print(query(1, N-1))

main()