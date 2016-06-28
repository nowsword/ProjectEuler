'''An = 3 * n - 2   => [1, 4, 7, 10, 13, ...]
Pn = sum(A[1, n]) = n * (3 * n - 1) // 2   => [1, 5, 12, 22, 35, ...]
1 <= j <= k
P_k - P_j = D = P_x   => sum(A[j + 1, k]) == sum(A[1, x])
P_j + P_k = P_y   => sum(A[1, j]) == sum(A[k + 1, y])
Pn % 3   ==> [1, 2, 0, 1, 2, 0, ...]'''

import datetime

def P(n):
    return n * (3 * n - 1) // 2

def P_index(val):
    if val <= 0:
        return 0
    beg = 1
    end = val
    while beg <= end:
        mid = (beg + end) // 2
        P_mid = P(mid)
        if P_mid == val:
            return mid
        if P_mid > val:
            end = mid - 1
        else:
            beg = mid + 1
    return 0

def main():
    size = 1
    while True:
        D = P(size)
        for d in range(size - 3, 0, -3):
            val = D - P(d)
            if val % (3 * d):
                continue
            beg = val // (3 * d) + 1

            j = beg - 1
            k = j + d
            if P_index(P(j) + P(k)):
                return D
        size += 1

beg = datetime.datetime.now()
ans = main()
end = datetime.datetime.now()

print("answer:", ans)
print("time:", end - beg)
