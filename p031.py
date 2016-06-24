import datetime

def main(num):
    S = (1, 2, 5, 10, 20, 50, 100, 200)
    size = len(S)
    dp = [None] * (num + 1)
    for i in range(num + 1):
        dp[i] = [None] * size
    for i in range(size):
        dp[0][i] = 1
    for i in range(num + 1):
        dp[i][0] = 1

    for i in range(1, num + 1):
        for j in range(1, size):
            MAX = i // S[j]
            res = 0
            for k in range(MAX + 1):
                res += dp[i - k * S[j]][j - 1]
            dp[i][j] = res
    return dp[num][size - 1]

try:
    para = int(input())
except:
    para = 200

beg = datetime.datetime.now()
ans = main(para)
end = datetime.datetime.now()

print("answer:", ans)
print("time:", end - beg)
