import datetime
import prime

def main(num):
    x = 1
    for i in range(num):
        x = prime.next_prime(x)
    return x

try:
    para = int(input())
except:
    para = 10001

beg = datetime.datetime.now()
ans = main(para)
end = datetime.datetime.now()

print("answer:", ans)
print("time:", end - beg)
