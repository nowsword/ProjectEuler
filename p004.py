import datetime

def ispalindrome(string):
    length = len(string)
    for i in range(length // 2):
        if string[i] != string[length - i - 1]:
            return False
    return True

def main(size):
    return max([i * j for i in range(10 ** (size - 1), 10 ** size)
        for j in range(i, 10 ** size) if ispalindrome(str(i * j))])

try:
    para = int(input())
except:
    para = 3

beg = datetime.datetime.now()
ans = main(para)
end = datetime.datetime.now()

print("answer:", ans)
print("time:", end - beg)
