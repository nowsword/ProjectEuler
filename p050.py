import datetime
import prime

def main(lt):
    MAX_SIZE = 0
    MAX_VAL = None
    L = [2]
    beg = 0
    while True:
        end = beg
        SUM = L[beg]
        if SUM >= lt:
            break
        while True:
            end += 1
            if end == len(L):
                L.append(prime.next_prime(L[-1]))
            SUM += L[end]
            if SUM >= lt:
                break
            if prime.is_prime(SUM) and end - beg + 1 > MAX_SIZE:
                MAX_SIZE = end - beg + 1
                MAX_VAL = SUM
        if end - beg <= MAX_SIZE:
            break
        beg += 1
    return MAX_VAL

try:
    para = int(input())
except:
    para = int(1e6)

beg = datetime.datetime.now()
ans = main(para)
end = datetime.datetime.now()

print("answer:", ans)
print("time:", end - beg)
