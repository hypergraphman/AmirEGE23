from itertools import permutations

sourse = '111222333'
a = set()
for s in permutations(sourse):
    s = ''.join(s)
    while '21' in s or '31' in s or '32' in s:
        if '21' in s:
            s = s.replace('21', '12', 1)
        if '31' in s:
            s = s.replace('31', '13', 1)
        if '32' in s:
            s = s.replace('32', '23', 1)
    a.add(s)
print(a)