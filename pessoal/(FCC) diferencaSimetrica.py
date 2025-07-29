def sym(*args):
    # tuple -> list
    args = list(args)
    
    # Obtém os 2 primeiros
    a = args[0]
    b = args[1]
    s = []
    
    for v in a+b:
        if (v in a and not (v in b)) or (v in b and not (v in a)):
            if v not in s: s.append(v)
    if len(args) > 2:
        s = sym(s, args[2:][0])
    return s

print(sorted(sym([1, 2, 3], [5, 2, 1, 4], [1, 2])))