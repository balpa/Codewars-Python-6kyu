def solution(s):
    list = [x for x in s]
    final = []
    
    for x in range(len(list)):
        if list[x] == list[x].upper():
            final.append(" ")
        final.append(list[x])
    
    return ''.join(final)
