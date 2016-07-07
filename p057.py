import datetime
import fractions

def main():
    x = fractions.Fraction(1)
    res = 0
    for i in range(1000):
        x = 1 / (x + 1) + 1
        if len(str(x.numerator)) > len(str(x.denominator)):
        	res += 1
    return res

beg = datetime.datetime.now()
ans = main()
end = datetime.datetime.now()

print("answer:", ans)
print("time:", end - beg)