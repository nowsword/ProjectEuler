import datetime
import prime

def main(num):
    return prime.max_prime_divisor(num)

try:
    para = int(input())
except:
    para = 600851475143

beg = datetime.datetime.now()
ans = main(para)
end = datetime.datetime.now()

print("answer:", ans)
print("time:", end - beg)
