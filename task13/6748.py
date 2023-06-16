g = {
    'а': 'бг',
    'б': 'д',
    'в': 'абдгж',
    'г': 'ж',
    'ж': 'е',
    'е': 'влк',
    'д': 'ие',
    'л': 'к',
    'к': 'ж',
    'и': 'ел',
}


def f(s, p):
    if len(p) > 1 and p[0] == p[-1]:
        return 1
    if len(p) != len(set(p)):
        return 0
    c = 0
    for v in g[s]:
        c += f(v, p + v)
    return c


print(f('е', 'е'))