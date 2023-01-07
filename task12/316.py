for k in range(1, 700):
    s = '>' + 22 * '1' + k * '2' + 23 * '3'
    while '>1' in s or '>2' in s or '>3' in s:
        if '>1' in s:
            s = s.replace('>1', '2>', 1)
        if '>2' in s:
            s = s.replace('>2', '21>', 1)
        if '>3' in s:
            s = s.replace('>3', '11>', 1)
    sum = 0
    for el in s[:-1]:
        sum += int(el)
    if sum > 2023:
        print(k)
        break







