s = open('24_6757.txt').read()
s = s.replace('FCE', '!').replace('CFE', '!')
cur_len = 0
mx_len = 0
for el in s:
    if el == '!':
        cur_len += 1
        if mx_len < cur_len:
            mx_len = cur_len
    else:
        cur_len = 0
print(mx_len)