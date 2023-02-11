s = set()
for n in range(500, 5000):
    g = bin(n)[2:]
    s1 = g[1:]
    s2 = s1.lstrip('0')
    if not s2:
        s2 = '0'
    s3 = int(s2, 2)
    r = n - s3
    s.add(r)
print(s, len(s))
