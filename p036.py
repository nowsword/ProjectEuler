import datetime

def is_palindromic(string):
    length = len(string)
    for i in range(length // 2):
        if string[i] != string[-i - 1]:
            return False
    return True

def get_complete(half, size):
    oppo = ''.join(reversed(half))
    if size % 2:
        return half + oppo[1:]
    return half + oppo

def main(le):
    maps = []
    maps.append([str(i) for i in range(1, 10)])
    for i in range((le - 1) // 2):
        L = [i + str(j) for i in maps[-1] for j in range(10)]
        maps.append(L)

    res = 0
    for size in range(1, le + 1):
        for half in maps[(size - 1) // 2]:
            num = int(get_complete(half, size))
            if is_palindromic(bin(num)[2:]):
                res += num
    return res

try:
    para = int(input())
except:
    para = 6

beg = datetime.datetime.now()
ans = main(para)
end = datetime.datetime.now()

print("answer:", ans)
print("time:", end - beg)
