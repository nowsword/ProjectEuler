import datetime
from prime import is_prime

def sorted_digit(num):
    return ''.join(sorted(str(num)))

def main():
    L = list(filter(lambda x: is_prime(x), range(1000, 10000)))
    S = set(L)
    size = len(L)

    for i in range(size - 2):
        a = L[i]
        for j in range(i + 1, size - 1):
            b = L[j]
            if a == 1487 and b == 4817:
                continue
            c = 2 * b - a
            if c > L[-1]:
                break
            if c in S and sorted_digit(a) == sorted_digit(b) == sorted_digit(c):
                return str(a) + str(b) + str(c)

beg = datetime.datetime.now()
ans = main()
end = datetime.datetime.now()

print("answer:", ans)
print("time:", end - beg)
