n = 99
r = 0
while r != 40:
    n += 1
    d1 = n % 10
    d2 = n // 10 % 10
    d3 = n // 100
    a = [d1 * 10 + d2, d2 * 10 + d1, d3 * 10 + d2, d2 * 10 + d3, d1 * 10 + d3, d3 * 10 + d1]
    mx = 0
    mn = 100
    for el in a:
        if 10 <= el <= 99:
            if el > mx:
                mx = el
            if el < mn:
                mn = el
    r = mx - mn
print(n, r)
    