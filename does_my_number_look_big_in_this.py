def narcissistic( value ):
    arr = [x for x in str(value)]
    leng = len(arr)
    for i in range(len(arr)):
        arr[i] = int(arr[i])**int(leng)
    summ = sum(arr)
    if summ == value:
        return True
    else:
        return False
