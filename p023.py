import datetime
from prime import all_divisors

def main():
    MAX = 28123
    abundants = []
    for i in range(1, MAX + 1):
        if sum(all_divisors(i)) - i > i:
            abundants.append(i)
    size = len(abundants)
    S = set()
    for i in range(size):
        for j in range(i, size):
            x = abundants[i] + abundants[j]
            if x > MAX:
                break
            S.add(x)
    SUM = (1 + MAX) * MAX // 2
    return SUM - sum(S)

beg = datetime.datetime.now()
ans = main()
end = datetime.datetime.now()

print("answer:", ans)
print("time:", end - beg)
