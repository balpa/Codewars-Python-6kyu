def array_diff(a, b):
    final = []
    if a == []:
        return []
    elif b == []:
        return a
    else:
        for x in range(len(b)):
            final = [elem for elem in a if elem not in b]
    return final
