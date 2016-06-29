import datetime
from prime import resolve

def main(size):
    count = 0
    num = 1
    while True:
        if len(resolve(num)) == size:
            count += 1
            if count == size:
                return num - size + 1
        else:
            count = 0
        num += 1

try:
    para = int(input())
except:
    para = 4

beg = datetime.datetime.now()
ans = main(para)
end = datetime.datetime.now()

print("answer:", ans)
print("time:", end - beg)
