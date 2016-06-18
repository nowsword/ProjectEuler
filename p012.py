import datetime
import prime

def main(gt):
    i = 0
    num = 0
    while True:
        i += 1
        num += i
        L = prime.resolve(num)
        res = 1
        for (a, b) in L:
            res *= b + 1
        if res > gt:
            return num

try:
    para = int(input())
except:
    para = 500

beg = datetime.datetime.now()
ans = main(para)
end = datetime.datetime.now()

print("answer:", ans)
print("time:", end - beg)
