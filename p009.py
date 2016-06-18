import datetime

def main(num):
    for a in range(1, num // 3):
        for b in range(a + 1, num // 2 if num % 2 == 0 else num // 2 + 1):
            c = num - a - b
            if a ** 2 + b ** 2 == c ** 2:
                return a * b * c

try:
    para = int(input())
except:
    para = 1000

beg = datetime.datetime.now()
ans = main(para)
end = datetime.datetime.now()

print("answer:", ans)
print("time:", end - beg)
