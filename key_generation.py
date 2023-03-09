from random import randint
from math import gcd


def extanded_evkl(a, b):
    a, b = max(a, b), min(a, b)
    x2 = 1
    x1 = 0
    y2 = 0
    y1 = 1
    while b > 0:
        q = a // b
        r = a - q * b
        x = x2 - q * x1
        y = y2 - q * y1
        a = b
        b = r
        x2 = x1
        x1 = x
        y2 = y1
        y1 = y
    d = a
    x = x2
    y = y2
    if d == 1:
        return y2
    return d


def is_ez(n):
    for i in range(2, 10 ** 2):
        a = randint(2, n - 1)
        r = pow(a, n - 1, n)
        if r != 1:
            return False
    return True


def key_generation(bits=1024):
    p = randint(2 ** bits, 2 ** (bits + 1))
    q = randint(2 ** bits, 2 ** (bits + 1))
    while not is_ez(p):
        p += 1
    while not is_ez(q):
        q += 1
    print('p', p)
    print('q', q)
    n = p * q
    print('n', n)
    eiler_funk = (p - 1) * (q - 1)
    print('eil', eiler_funk)
    e = randint(2, eiler_funk - 1)
    while gcd(e, eiler_funk) != 1:
        e += 1
        if e > eiler_funk:
            e = randint(2, eiler_funk - 1)
    print('e', e)
    d = pow(e, -1, eiler_funk)
    print('d', d)
    # print(e * d % eiler_funk)
    # d = extanded_evkl(eiler_funk, e)
    open_key = (e, n)
    closed_key = (d, n)
    with open('keys.txt', 'w') as f:
        f.write(str(e) + '\n')
        f.write(str(n) + '\n')
        f.write(str(d) + '\n')
    return open_key, closed_key


keys = key_generation()
e = keys[0][0]
d = keys[1][0]

print('e', keys[0][0])
print('n', keys[0][1])
print('d', keys[1][0])
# print('n', keys[1][1])

