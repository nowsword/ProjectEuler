import datetime

def T(n):
  return n * (n + 1) // 2

def P(n):
  return n * (3 * n - 1) // 2

def H(n):
  return n * (2 * n - 1)

def index(val, func):
    if val <= 0:
        return 0
    beg = 1
    end = val
    while beg <= end:
        mid = (beg + end) // 2
        val_mid = func(mid)
        if val_mid == val:
            return mid
        if val_mid > val:
            end = mid - 1
        else:
            beg = mid + 1
    return 0

def main():
    n = 143
    while True:
        n += 1
        val = H(n)
        if index(val, T) and index(val, P):
            return val

beg = datetime.datetime.now()
ans = main()
end = datetime.datetime.now()

print("answer:", ans)
print("time:", end - beg)
