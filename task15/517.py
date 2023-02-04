for a in range(1, 1000):
    is_a = True
    for x in range(51, 10000, 51):
        for y in range(78, 10000, 78):
            for z in range(115, 10000, 115):
                if not ((z % 115 == 0 or y % 78 == 0 or x % 51 == 0) <= (x * y * z % a == 0)):
                    is_a = False
    if is_a:
        print(a)