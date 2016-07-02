import datetime

def get_digit_count(num):
    L = [0] * 10
    string = str(num)
    for ch in string:
        L[int(ch)] += 1
    return L

def x6_same(num):
    L = get_digit_count(num)
    for i in range(2, 7):
        x = num * i
        if get_digit_count(x) != L:
            return False
    return True


NUM = None

def dfs(index, size):
    if index == size:
        num = int(''.join(NUM))
        if x6_same(num):
            return num
        return 0

    if index == 1:
        R = range(7)
    elif index == size - 1:
        R = range(1, 10)
    else:
        R = range(10)
    for i in R:
        NUM[index] = str(i)
        res = dfs(index + 1, size)
        if res:
            return res
    return 0

def main():
    global NUM
    size = 4
    while True:
        NUM = [None] * size
        NUM[0] = '1'
        res = dfs(1, size)
        if res:
            return res
        size += 1

beg = datetime.datetime.now()
ans = main()
end = datetime.datetime.now()

print("answer:", ans)
print("time:", end - beg)
