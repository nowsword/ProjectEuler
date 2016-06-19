from functools import reduce

def _range_product(l, r):
    if l >= r:
        return
    if l <= 0 <= r - 1:
        return 0
    return reduce(lambda a, b: a * b, range(l, r))

def factorial(n):
    if n < 0:
        return
    res = _range_product(2, n + 1)
    return res if res != None else 1

def A(n, m):
    if n < 0 or m < 0 or m > n:
        return 0
    res = _range_product(n - m + 1, n + 1)
    return res if res != None else 1

def C(n, m):
    if n < 0 or m < 0 or m > n:
        return 0
    if 2 * m > n:
        m = n - m
    return A(n, m) // factorial(m)
