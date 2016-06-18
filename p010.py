import datetime
import prime

def main(lt):
    return sum(prime.range_primes(lt))

try:
    para = int(input())
except:
    para = int(2e6)

beg = datetime.datetime.now()
ans = main(para)
end = datetime.datetime.now()

print("answer:", ans)
print("time:", end - beg)
