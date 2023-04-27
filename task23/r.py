def f(s, e, c):
    if s == e and c < 0:
        return 1
    if s == e and c >= 0:
        return 0
    if s > e or s % 10 == 5:
        return 0
    return f(s + 1, e, c + 1) + f(s * 2, e, c - 1)


print(f(2, 14) * f(14, 29))