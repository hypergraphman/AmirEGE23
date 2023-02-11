n = 0
r = 0
while r <= 77:
    n += 1
    s1 = bin(n)[2:]
    s2 = s1 + str(s1.count('1') % 2)
    s3 = s2 + str(s2.count('1') % 2)
    r = int(s3, 2)
print(n, r)