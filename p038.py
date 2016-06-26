import datetime

def ok(num):
    if num % 10 == 5:
        return False
    string = str(num)
    if string.count('0'):
        return False
    for x in range(1, 10):
        if string.count(str(x)) > 1:
            return False
    return True

def main():
    STRING = '123456789'
    MAX = 0

    x = 1
    string = ''.join([str(x * i) for i in range(1, 10)])
    MAX = max(MAX, int(string))
    x = 9
    string = ''.join([str(x * i) for i in range(1, 6)])
    MAX = max(MAX, int(string))

    for x in range(10, 100):
        if not ok(x):
            continue
        string = ''.join([str(x * i) for i in range(1, 5)])
        if ''.join(sorted(string)) == STRING:
            MAX = max(MAX, int(string))
    for x in range(100, 1000):
        if not ok(x):
            continue
        string = ''.join([str(x * i) for i in range(1, 4)])
        if ''.join(sorted(string)) == STRING:
            MAX = max(MAX, int(string))
    for x in range(1000, 10000):
        if not ok(x):
            continue
        string = ''.join([str(x * i) for i in range(1, 3)])
        if ''.join(sorted(string)) == STRING:
            MAX = max(MAX, int(string))
    return MAX

beg = datetime.datetime.now()
ans = main()
end = datetime.datetime.now()

print("answer:", ans)
print("time:", end - beg)
