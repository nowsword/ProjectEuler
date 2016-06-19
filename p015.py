import datetime
from combine import C

def main(size):
    return C(2 * size, size)

try:
    para = int(input())
except:
    para = 20

beg = datetime.datetime.now()
ans = main(para)
end = datetime.datetime.now()

print("answer:", ans)
print("time:", end - beg)
