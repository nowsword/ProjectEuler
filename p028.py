import datetime

def main(size):
    res = 1
    for i in range(size, 1, -2):
        num = i * i
        for j in range(4):
            res += num
            num -= i - 1
    return res

try:
    para = int(input())
except:
    para = 1001

beg = datetime.datetime.now()
ans = main(para)
end = datetime.datetime.now()

print("answer:", ans)
print("time:", end - beg)
