alf = 'УОА'
k = 1
for s1 in alf:
    for s2 in alf:
        for s3 in alf:
            for s4 in alf:
                for s5 in alf:
                    word = s1 + s2 + s3 + s4 + s5
                    print(k, word)
                    k = k + 1