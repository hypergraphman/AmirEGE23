alf = '01234567'
c = 0
for a1 in alf:
    for a2 in alf:
        for a3 in alf:
            for a4 in alf:
                for a5 in alf:
                    word = a1 + a2 + a3 + a4 + a5
                    if word[0] != '0' and word.count('6') == 1 and '26' not in word and '46' not in word and '06' not in word and '62' not in word and '64' not in word and '60' not in word:
                        c += 1
print(c)
from itertools import product
alf = '01234567'
c = 0
for letters in product(alf, repeat=5):
    word = ''.join(letters)
    if word[0] != '0' and word.count('6') == 1 and all(x not in word for x in ['06', '60', '26', '62', '46', '64']):
        c += 1
print(c)
