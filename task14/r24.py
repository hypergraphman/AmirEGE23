def n_to_p(n, p):
    r = ''
    while n > 0:
        d = '0123456789ABCDEF'[n % p]
        r = d + r
        n = n // p
    return r


print(n_to_p(64**10 + 2**90 - 16, 8).count('7'))
