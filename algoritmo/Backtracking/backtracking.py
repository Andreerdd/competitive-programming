"""
Mostra todas as permutações de um vetor de 1 até N
"""

N = int(input())
total = []

def backtrack(i, curr=[]):
    if i > N:
        if curr not in total:
            total.append(curr)
        return
    
    # Ignora ele
    backtrack(i+1, curr)
    
    # Conta com ele
    newcurr = curr.copy()
    newcurr.append(i)
    total.append(newcurr)
    backtrack(i+1, newcurr)
    

backtrack(1)
print(total)
    