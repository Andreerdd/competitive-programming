"""
SegmentTree com Classe

Mesmo conceito de SegmentTree, mas é usado
classe. Melhor para implementações avançadas
de SegmentTree.
"""

class Node:
    def __init__(self, val=0, tl=0, tr=0, left=None, right=None):
        self.val = val
        self.tl = tl # tree left
        self.tr = tr # tree right
        self.left = left
        self.right = right

vals = [1, 2, 3, 4, 5]
N = len(vals)


def build(tl=0, tr=N-1):
    if tl == tr:
        me = Node(val=vals[tl], tl=tl, tr=tr, left=None, right=None)
        return me

    mid = (tl+tr) // 2

    left = build(tl, mid)
    right = build(mid+1, tr)

    me = Node(val=left.val+right.val, tl=tl, tr=tr, left=left, right=right)
    return me


def update(idx, val, me: Node):
    tl = me.tl
    tr = me.tr
    if tl == tr:
        me.val = val
        vals[idx] = val
        return


    mid = (tl+tr) // 2

    if tl <= idx <= mid: update(idx, val, me.left)
    else: update(idx, val, me.right)

    me.val = me.left.val+me.right.val


def query(l: int, r: int, me: Node):

    # se ultrapassou
    if me.tr < l or me.tl > r: return 0

    # se tá totalmente dentro
    if me.tl >= l and me.tr <= r: return me.val

    return query(l, r, me.left) + query(l, r, me.right)



def main():
    root = build()
    print(query(2, 4, root))
    update(2, -3, root)
    print(query(2, 4, root))

main()