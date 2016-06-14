import math

_prime_list = [2]
_prime_end = 2

def _min_prime_divisor_in_end(x):
    '''x > 1'''
    sqrtx = int(math.sqrt(x))
    for i in _prime_list:
        if i > sqrtx:
            return
        if x % i == 0:
            return i

def _is_prime_in_end(x):
    '''x > 1'''
    div = _min_prime_divisor_in_end(x)
    return div == None

def _extend_prime_end(le):
    global _prime_list, _prime_end
    while True:
        x = _prime_end + 1
        if x > le:
            return
        res = _is_prime_in_end(x)
        _prime_end += 2
        if res:    
            _prime_list.append(x)
            yield x    

def is_prime(x):
    if x <= 1:
        return False
    res = _is_prime_in_end(x)
    sqrtx = int(math.sqrt(x))
    if not res or _prime_end >= sqrtx:
        return res
    gener = _extend_prime_end(sqrtx)
    try:
        while True:
            k = next(gener)
            if x % k == 0:
                return False
    except StopIteration:
        return True

def next_prime(x):
    if x < 2:
        return 2
    k = x + 1 if x % 2 == 0 else x + 2
    while not is_prime(k):
        k += 2
    return k

def range_primes(a, b=None):
    if b == None:
        l = 2
        r = a
    else:
        l = max(a, 2)
        r = b
    k = l + 1 if l % 2 == 0 else l
    res = [x for x in range(k, r, 2) if is_prime(x)]
    if l <= 2 < r:
        res.insert(0, 2)
    return res

def min_prime_divisor(x):
    if x <= 1:
        return
    div = _min_prime_divisor_in_end(x)
    if div != None:
        return div
    sqrtx = int(math.sqrt(x))
    if _prime_end >= sqrtx:
        return x
    gener = _extend_prime_end(sqrtx)
    try:
        while True:
            k = next(gener)
            if x % k == 0:
                return k
    except StopIteration:
        return x

def max_prime_divisor(x):
    last = None
    while True:
        div = min_prime_divisor(x)
        if div == None:
            return last
        while x % div == 0:
            x //= div
        last = div

def resolve(x):
    res = []
    while True:
        div = min_prime_divisor(x)
        if div == None:
            return res
        num = 0
        while x % div == 0:
            x //= div
            num += 1
        res.append((div, num))
