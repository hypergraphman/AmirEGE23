print('x y z')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            f = (x or not y or not z) and (not x or y)
            if not f:
                print(x, y, z, int(f))