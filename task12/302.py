from time import time

st = time()
for x in range(100):
    for y in range(100):
        for z in range(100):
            if (x + 2 * y + 3 * z == 111 and
               x + y + 3 * z == 101 and
               y + z == 35):
                print(x + y + z + 2)
print(time() - st)