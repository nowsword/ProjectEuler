import datetime
from prime import is_prime, next_prime

def prime_family(x, num):
    MAX = 10 - num
    L = [[] for i in range(MAX + 1)]
    array = list(str(x))
    for i in range(len(array)):
        k = int(array[i])
        if k <= MAX:
            L[k].append(i)

    for i in range(MAX + 1):
        size = len(L[i])
        if size == 0:
            continue
        key_max = 2 ** size
        for key in range(1, key_max):
            key_array = []
            key_count = 0
            while key:
                if key % 2:
                    key_array.append(key_count)
                key //= 2
                key_count += 1

            count = 10 - i
            for j in range(i + 1, 10):
                str_j = str(j)
                for k in key_array:
                    array[L[i][k]] = str_j
                if not is_prime(int(''.join(array))):
                    count -= 1
                    if count < num:
                        break
            else:
                return True
    return False

def main(num):
    x = 1
    while True:
        x = next_prime(x)
        if prime_family(x, num):
            return x

try:
    para = int(input())
except:
    para = 8

beg = datetime.datetime.now()
ans = main(para)
end = datetime.datetime.now()

print("answer:", ans)
print("time:", end - beg)
