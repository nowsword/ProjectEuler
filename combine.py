from functools import reduce

_factorials = [1]
_factorials_size = 1

def factorial(n):
    global _factorials, _factorials_size
    if n < 0:
        return
    if n < _factorials_size:
        return _factorials[n]
    for i in range(_factorials_size, n + 1):
        _factorials.append(_factorials[-1] * i)
    _factorials_size = n + 1
    return _factorials[-1]

def _range_product(l, r):
    if l >= r:
        return
    if l <= 0 <= r - 1:
        return 0
    return reduce(lambda a, b: a * b, range(l, r))

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
