import datetime
import prime

primes = None
record = None

def dfs(pos, size):
    if pos == size:
        string = ''.join(record)
        if prime.is_prime(int(string)):
            primes[size][string] = True
        return

    digits = '1379'
    for i in digits:
        record[pos] = i
        dfs(pos + 1, size)

def main(le):
    global primes, record
    primes = [{} for i in range(le + 1)]
    circulars = [[] for i in range(le + 1)]
    circulars[1] = [2, 3, 5, 7]

    res = len(circulars[1])
    for size in range(2, le + 1):
        record = [None] * size
        dfs(0, size)
        for string in primes[size]:
            if primes[size][string]:
                num = 1
                primes[size][string] = False
                for i in range(size - 1):
                    string = string[-1:] + string[:-1]
                    if string in primes[size] and primes[size][string]:
                        num += 1
                        primes[size][string] = False
                if num == size:
                    circulars[size].append(int(string))
        res += size * len(circulars[size])
        if prime.is_prime(int('1' * size)):
            res += 1
    return res

try:
    para = int(input())
except:
    para = 6

beg = datetime.datetime.now()
ans = main(para)
end = datetime.datetime.now()

print("answer:", ans)
print("time:", end - beg)
