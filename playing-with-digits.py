def dig_pow(n, p):
    sq = []
    num = [int(x) for x in str(n)]
    for x in range(len(num)):
        sq.append(num[x]**p)
        p += 1
    sumarr = sum(sq)
    k = sumarr/n
    if sumarr % n == 0:
        return sumarr/n
    elif sumarr % n != 0:
        return -1
