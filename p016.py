import datetime

def main(exp):
    return sum(map(int, str(2 ** exp)))

try:
    para = int(input())
except:
    para = 1000

beg = datetime.datetime.now()
ans = main(para)
end = datetime.datetime.now()

print("answer:", ans)
print("time:", end - beg)
