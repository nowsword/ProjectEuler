import datetime
import math

def get_max_exp(le):
    val = 1
    exp = 0
    while val <= le:
        val *= 2
        exp += 1
    return exp - 1

def main(le):
    #求出每一层的指数集合大小
    size = get_max_exp(le)
    count = [None]
    S = set()
    for i in range(1, size + 1):
        Sx = set(range(i * 2, i * le + 1, i))
        S = S.union(Sx)
        count.append(len(S))
    #求出每一层里之前已经出现过的数的个数
    over = [None] * 2
    NUM = le - 1
    for i in range(2, size + 1):
        over.append(NUM - (count[i] - count[i - 1]))
    #求出可能出现重叠的所有底数
    MAX = int(math.sqrt(le))
    L = list(range(2, MAX + 1))
    S = set(range(2, MAX + 1))
    for i in L:
        base = i
        while True:
            base *= i
            if base > MAX:
                break
            if base in S:
                S.remove(base)
    #求出发生重叠的次数
    total = 0
    for i in S:
        base = i
        for j in range(2, size + 1):
            base *= i
            if base > le:
                break
            total += over[j]
    return NUM ** 2 - total

try:
    para = int(input())
except:
    para = 100

beg = datetime.datetime.now()
ans = main(para)
end = datetime.datetime.now()

print("answer:", ans)
print("time:", end - beg)
