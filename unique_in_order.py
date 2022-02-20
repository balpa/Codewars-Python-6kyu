def unique_in_order(iterable):
    if len(iterable) == 0:
        return []
    arr = [x for x in iterable]
    final = [] 
    final.append(arr[0])
    c = 0
    
    for x in range(len(arr)-1):
        if arr[x+1] != final[c]:
            final.append(arr[x+1])
            c += 1
    return final
