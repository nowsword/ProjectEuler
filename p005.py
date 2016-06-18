import datetime
import prime

def main(le):
    res = 1
    for i in range(2, le + 1):
        if res % i != 0:
            res *= prime.min_prime_divisor(i)
    return res

try:
    para = int(input())
except:
    para = 20

beg = datetime.datetime.now()
ans = main(para)
end = datetime.datetime.now()

print("answer:", ans)
print("time:", end - beg)
