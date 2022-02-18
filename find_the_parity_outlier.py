def find_outlier(integers):
    arr = list(map(lambda x : x % 2, integers))
    print(arr)
    if arr.count(1) > 1:
        return integers[arr.index(0)]
    elif arr.count(0) > 1:
        return integers[arr.index(1)]
    else:
        pass
