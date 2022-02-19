def digital_root(n):
    current = [int(x) for x in str(n)]
    currentsum = sum(current)
    
    while currentsum > 9:
        current = [int(x) for x in str(currentsum)]
        currentsum = sum(current)
    
    return currentsum
