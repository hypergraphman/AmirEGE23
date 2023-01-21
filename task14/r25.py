def n_to_p(n, p):
    r = ''
    while n > 0:
        d = '0123456789ABCDEF'[n % p]
        r = d + r
        n = n // p
    return r


print(n_to_p(49**7 + 7**21 - 7, 7).count('6'))