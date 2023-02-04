for a in range(1, 1000):
    if all((x % a == 0) or ((x % 23 == 0) <= (not (50 <= x <= 70))) for x in range(1, 1000)):
        print(a)