a = list(map(int, open('17_6752.txt')))
count = 0
for el in a:
    if el % 3 == 0:
        count += 1
mx = -float('inf')
k = 0
for p1, p2 in zip(a, a[1:]):
    if (p1 < 0 or p2 < 0) and p1 + p2 < count:
        if p1 + p2 > mx:
            mx = p1 + p2
        k += 1
print(k, mx)