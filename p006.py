import datetime

def main(le):
    return sum(range(le + 1)) ** 2 - sum(x ** 2 for x in range(le + 1))

try:
    para = int(input())
except:
    para = 100

beg = datetime.datetime.now()
ans = main(para)
end = datetime.datetime.now()

print("answer:", ans)
print("time:", end - beg)
