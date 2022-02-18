def string_breakers(n, st): 
    st = st.replace(" ","")
    final = []
    x = n
    for i in range(0,len(st),n):
        final.append(st[i:n])
        n += x
    return '\n'.join(final)
