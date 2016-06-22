import sort
from combine import factorial

def all_permutations_count(L):
    size = L if isinstance(L, int) else len(L)
    return factorial(size)

_Lx = None
_vis = None
_record = None
_SIZE = None

def _dfs(floor):
    if floor == _SIZE:
        yield tuple(_record)
        return
    for i in range(_SIZE):
        if _vis[i]:
            _vis[i] = False
            _record[floor] = _Lx[i]
            for x in _dfs(floor + 1):
                yield x
            _vis[i] = True

def all_permutations(L, *, cmp=None):
    global _Lx, _vis, _record, _SIZE
    _SIZE = len(L)
    _Lx = sort.sorted(L, cmp=cmp)
    _vis = [True] * _SIZE
    _record = [None] * _SIZE
    return _dfs(0)

def get_permutation(L, rank, *, cmp=None):
    size = len(L)
    total = all_permutations_count(size)
    if rank <= 0 or rank > total:
        return
    Lx = sort.sorted(L, cmp=cmp)
    res = []
    rank -= 1
    while size:
        total //= size
        size -= 1
        res.append(Lx.pop(rank // total))
        rank %= total
    return tuple(res)

from bisect import bisect_left

def _get_rank_list(L, *, cmp=None):
    def origin_cmp(a, b):
        if a == b:
            return 0
        return -1 if a < b else 1
    def make_cmp(cmp):
        if not cmp:
            cmp = origin_cmp
        return lambda a, b: cmp(a[1], b[1])

    Lx = [[i, x] for i, x in enumerate(L)]
    sort.sort(Lx, cmp=make_cmp(cmp))
    for (i, x) in enumerate(Lx):
        x[1] = i
    sort.sort(Lx, cmp=lambda a, b: a[0] - b[0])
    return tuple(x[1] for x in Lx)

def get_rank(L, *, cmp=None):
    Lx = _get_rank_list(L, cmp=cmp)

    size = len(L)
    total = all_permutations_count(size)
    L_rank = list(range(size))
    rank = 1
    for x in Lx:
        total //= size
        size -= 1
        pos = bisect_left(L_rank, x)
        L_rank.pop(pos)
        rank += pos * total
    return rank

def next_permutation(L, *, cmp=None):
    Lx = list(_get_rank_list(L, cmp=cmp))
    
    size = len(L)
    for i in range(size - 1, 0, -1):
        if Lx[i - 1] < Lx[i]:
            pos = i - 1
            key = Lx[pos]
            break
    else:
        return

    Ly = Lx[pos + 1:]
    sort.sort(Ly)
    x = bisect_left(Ly, key)
    (Lx[pos], Ly[x]) = (Ly[x], Lx[pos])
    Lx = Lx[:pos + 1] + Ly

    L_sorted = sort.sorted(L, cmp=cmp)
    return tuple(L_sorted[x] for x in Lx)

def prev_permutation(L, *, cmp=None):
    Lx = list(_get_rank_list(L, cmp=cmp))
    
    size = len(L)
    for i in range(size - 1, 0, -1):
        if Lx[i - 1] > Lx[i]:
            pos = i - 1
            key = Lx[pos]
            break
    else:
        return

    Ly = Lx[pos + 1:]
    sort.sort(Ly)
    x = bisect_left(Ly, key) - 1
    (Lx[pos], Ly[x]) = (Ly[x], Lx[pos])
    Ly.reverse()
    Lx = Lx[:pos + 1] + Ly

    L_sorted = sort.sorted(L, cmp=cmp)
    return tuple(L_sorted[x] for x in Lx)
