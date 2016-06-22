import datetime
import prime

def get(a, b):
    n = 2
    while True:
        x = n ** 2 + n * a + b
        if not prime.is_prime(x):
            return n
        n += 1

def main():
    MAX = 1000
    L1 = prime.range_primes(MAX)
    L2 = prime.range_primes(2 * MAX)
    La = {sum - b - 1 for sum in L2 for b in L1}
    Lb = L1
    
    maxvalue = 0
    res = None
    for a in La:
        for b in Lb:
            temp = get(a, b)
            if temp > maxvalue:
                maxvalue = temp
                res = a * b
    return res

beg = datetime.datetime.now()
ans = main()
end = datetime.datetime.now()

print("answer:", ans)
print("time:", end - beg)
