for n in range(0, 100):
    s = '>' + 39 * '0' + n * '1' + 39 * '2'
    while '>1' in s or '>2' in s or '>0' in s:
        if '>1' in s:
            s = s.replace('>1', '22>', 1)
        if '>2' in s:
            s = s.replace('>2', '2>', 1)
        if '>0' in s:
            s = s.replace('>0', '1>', 1)
    summa = 0
    for el in s[0:len(s)-1]:
        summa += int(el)
    is_prime = True
    for i in range(2, summa):
        if summa % i == 0:
            is_prime = False
    if is_prime:
        print(s)
        print(summa)
        print(n)
        break