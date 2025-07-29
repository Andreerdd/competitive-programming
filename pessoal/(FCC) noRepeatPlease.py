"""
Return the number of total permutations of the provided string that don't have repeated consecutive letters. 
Assume that all characters in the provided string are each unique.

For example, aab should return 2 because it has 6 total permutations (aab, aab, aba, aba, baa, baa), 
but only 2 of them (aba and aba) don't have the same letter (in this case a) repeating.
"""

# O(n!)     :-(
def permuta(s: str):
    if len(s) == 1: return s
    results = []
    
    for i in range(len(s)):
        cch = s[i]
        rch = s[:i] + s[i+1:]
    
        for p in permuta(rch):
            results.append(cch + p)
    
    return results
        

# time O(n²)
def permAlone(s: str) -> int:
    # descobre todas as permutacoes
    perms = permuta(s)
    l = len(s)
    
    n = len(perms)
    
    # verifica uma por uma
    for p in perms:
        for i in range(l):
            if i > 0:
                if p[i] == p[i-1]:
                    n -= 1;
                    break;
                
    return n
                
    
    
        
        
    

permAlone('aab');