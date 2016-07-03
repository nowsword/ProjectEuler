import datetime

def palindrome(num):
    string = str(num)
    length = len(string)
    for i in range(length // 2):
        if string[i] != string[length - i - 1]:
            return False
    return True

def Lychrel(num):
    for i in range(49):
        x = int(''.join(reversed(str(num))))
        num += x
        if palindrome(num):
            return False
    return True

def main():
    RANGE = int(1e4)
    res = 0
    for i in range(RANGE):
        if Lychrel(i):
            res += 1
    return res

beg = datetime.datetime.now()
ans = main()
end = datetime.datetime.now()

print("answer:", ans)
print("time:", end - beg)
