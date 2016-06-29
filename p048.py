import datetime

def main(le):
    res = 0
    for i in range(1, le + 1):
        res += i ** i
    return str(res)[-10:]

try:
    para = int(input())
except:
    para = 1000

beg = datetime.datetime.now()
ans = main(para)
end = datetime.datetime.now()

print("answer:", ans)
print("time:", end - beg)
