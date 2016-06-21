import datetime
from combine import factorial

def main(num):
    return sum(map(int, str(factorial(num))))

try:
    para = int(input())
except:
    para = 100

beg = datetime.datetime.now()
ans = main(para)
end = datetime.datetime.now()

print("answer:", ans)
print("time:", end - beg)
