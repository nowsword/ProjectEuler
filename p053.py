import datetime
import combine

def main():
    VALUE = int(1e6)
    flag = False
    res = 0
    for n in range(1, 101):
        if not flag:
            r = n // 2
            val = combine.C(n, r)
            if val > VALUE:
                flag = True
                for beg in range(r - 1, -1, -1):
                    if combine.C(n, beg) <= VALUE:
                        beg += 1
                        break
                res += n - 2 * beg + 1
                beg -= 1
        else:
            for r in range(beg, -1, -1):
                if combine.C(n, r) <= VALUE:
                    r += 1
                    break
            res += n - 2 * r + 1
            beg = r - 1
    return res

beg = datetime.datetime.now()
ans = main()
end = datetime.datetime.now()

print("answer:", ans)
print("time:", end - beg)
