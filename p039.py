import datetime
import math

def main(le):
    D = {}
    for a in range(1, le // 3 + 1):
        for b in range(a + 1, le // 2 if le % 2 == 0 else le // 2 + 1):
            x = a ** 2 + b ** 2
            y = int(math.sqrt(x))
            p = a + b + y
            if y ** 2 == x and p <= le:
                D.setdefault(p, 0)
                D[p] += 1
    return sorted(D, key=lambda x: D[x], reverse=True)[0]

try:
    para = int(input())
except:
    para = 1000

beg = datetime.datetime.now()
ans = main(para)
end = datetime.datetime.now()

print("answer:", ans)
print("time:", end - beg)
