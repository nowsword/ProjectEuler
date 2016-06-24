import datetime
from fractions import Fraction

def main():
    res = 1
    for A in range(10, 100):
        if A % 10 == 0:
            continue
        L1 = (A // 10, A % 10)
        for B in range(A + 1, 100):
            if B % 10 == 0:
                continue
            L2 = (B // 10, B % 10)

            base = Fraction(A, B)
            if L1[0] == L2[1] and Fraction(L1[1], L2[0]) == base:
                res *= base
            elif L1[1] == L2[0] and Fraction(L1[0], L2[1]) == base:
                res *= base
    return res.denominator

beg = datetime.datetime.now()
ans = main()
end = datetime.datetime.now()

print("answer:", ans)
print("time:", end - beg)
