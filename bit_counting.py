def count_bits(n):
    bits = bin(n)
    arr = [str(x) for x in str(bits)]
    return arr.count("1") 
