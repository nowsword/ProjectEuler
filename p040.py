import datetime
import bisect

def get_digit(L, index):
    if index == 0:
        return 0
    size = bisect.bisect_left(L, index)
    num = 10 ** (size - 1) + (index - L[size - 1] - 1) // size
    pos = (index - L[size - 1] - 1) % size
    return int(str(num)[pos])

def main():
    L = [0]
    SUM = 0
    size = 1
    count = 9
    while SUM < int(1e6):
        SUM += size * count
        L.append(SUM)
        size += 1
        count *= 10

    res = 1
    k = 1
    for i in range(7):
        res *= get_digit(L, k)
        k *= 10
    return res

beg = datetime.datetime.now()
ans = main()
end = datetime.datetime.now()

print("answer:", ans)
print("time:", end - beg)
