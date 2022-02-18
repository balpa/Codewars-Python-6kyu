def odd_row(n):
    arr = []
    for x in range(1,n+n,2):
        arr.append((n**2)-n+x)
    return arr
