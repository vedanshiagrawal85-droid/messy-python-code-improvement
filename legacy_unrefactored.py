# Legacy / Messy Script (Hard to read, monolithic, no error handling)
def p(d):
    t = 0
    c = 0
    res = []
    for i in d:
        if i['s'] == 'A':
            t += i['g']
            c += 1
            res.append(i['n'].upper())
    avg = t / c if c != 0 else 0
    return avg, res

data = [{'n': 'alice', 'g': 85, 's': 'A'}, {'n': 'bob', 'g': 72, 's': 'B'}, {'n': 'vedanshi', 'g': 92, 's': 'A'}]
print(p(data))
