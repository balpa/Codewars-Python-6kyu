def find_uniq(arr):
    res = []
    sub = set(arr)
    subb = [x for x in sub]
    for x in range(len(subb)):
        if arr.count(subb[x]) == 1:
            return subb[x]
