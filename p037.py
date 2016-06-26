import datetime
from prime import is_prime

def from_right(num):
    string = str(num)
    length = len(string)
    for beg in range(length):
        if not is_prime(int(string[beg:])):
            return False
    return True

def main():
    L = [[2, 3, 5, 7]]
    size = 1
    while True:
        l = []
        for i in L[size - 1]:
            num = i * 10
            for j in [1, 3, 7, 9]:
                if is_prime(num + j):
                    l.append(num + j)
        if len(l) == 0:
            break
        L.append(l)
        size += 1

    res = 0
    for (i, l) in enumerate(L):
        if i == 0:
            continue
        for x in l:
            if x % 10 in (3, 7) and from_right(x):
                res += x
    return res

beg = datetime.datetime.now()
ans = main()
end = datetime.datetime.now()

print("answer:", ans)
print("time:", end - beg)
