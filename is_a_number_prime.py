def is_prime(num):
    n = num
    if n == 1 or n < 1:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
