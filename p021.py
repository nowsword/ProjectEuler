import datetime
from prime import all_divisors

def get(x):
    return sum(all_divisors(x)) - x

def main(lt):
    res = 0
    for i in range(1, lt):
        x = get(i)
        if x > i and get(x) == i:
            res += i + x if x < lt else i
    return res

try:
    para = int(input())
except:
    para = int(1e4)

beg = datetime.datetime.now()
ans = main(para)
end = datetime.datetime.now()

print("answer:", ans)
print("time:", end - beg)
