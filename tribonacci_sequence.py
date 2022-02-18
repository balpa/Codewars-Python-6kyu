def tribonacci(signature, n):
    if n == 1:
        return [signature[0]]
    elif n == 0:
        return []
    elif n == 2:
        return [signature[0], signature[1]]
    else:
        pass 
    for x in range(0,n-3):
        b = x+1
        c = b+1
        signature.append(signature[x]+signature[b]+signature[c])
        
    return signature
