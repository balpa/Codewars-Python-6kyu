def duplicate_encode(word):
    arr = [x.lower() for x in word]
    final = []
    for x in range(len(arr)):
        if arr.count(arr[x]) > 1:
            final.append(")")
        else:
            final.append("(")
    return ''.join(final)
