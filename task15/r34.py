for a in range(1, 100):
    if all((5 * k + 6 * n > 57) + ((k <= a) * (n < a)) for k in range(1, 100) for n in range(1, 100)):
        print(a)
    