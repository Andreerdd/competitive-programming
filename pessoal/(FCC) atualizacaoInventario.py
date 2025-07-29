def updateInventory(arr2, arr1):
    items = {arr1[n][1]: arr1[n][0] for n in range(len(arr1))}
    
    for i in arr2:
        if not (i[1] in items):
            items[i[1]] = i[0]
        else:
            items[i[1]] += i[0]
            
    res = []
    for name in items:
        val = items[name]
        res.append([val, name])
    
    return sorted(res, key=lambda x: x[1])
    
    
        

# Exemplo de listas de inventário
curInv = [
    [21, "Bowling Ball"],
    [2, "Dirty Sock"],
    [1, "Hair Pin"],
    [5, "Microphone"]
]

newInv = [
    [2, "Hair Pin"],
    [3, "Half-Eaten Apple"],
    [67, "Bowling Ball"],
    [7, "Toothpaste"]
]

updateInventory(curInv, newInv)