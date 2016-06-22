def _partition(L, l, r, *, cmp):
    if r - l < 2:
        return
    key = L[l]
    beg = l + 1
    end = r - 1
    while beg <= end:
        while beg <= end and cmp(L[beg], key) <= 0:
            beg += 1
        while end >= beg and cmp(L[end], key) >= 0:
            end -= 1
        if beg < end:
            (L[beg], L[end]) = (L[end], L[beg])
            beg += 1
            end -= 1
    (L[l], L[end]) = (L[end], L[l])
    _partition(L, beg, r, cmp=cmp)
    _partition(L, l, end, cmp=cmp)

def _origin_cmp(a, b):
    if a == b:
        return 0
    return -1 if a < b else 1

def _reverse_cmp(cmp):
    return lambda a, b: -cmp(a, b)

def sort(L, *, cmp=None, reverse=False):
    if not cmp:
        cmp = _origin_cmp
    if reverse:
        cmp = _reverse_cmp(cmp)
    _partition(L, 0, len(L), cmp=cmp)

def sorted(L, *, cmp=None, reverse=False):
    Lx = list(L)
    sort(Lx, cmp=cmp, reverse=reverse)
    return Lx
