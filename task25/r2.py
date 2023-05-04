def divs(n):
    d = {1, n}
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return sorted(d)


for j in range(174457, 174505 + 1):
    t = divs(j)
    if len(t) == 4:
        print(t[1], t[2])