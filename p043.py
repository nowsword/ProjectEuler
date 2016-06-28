import datetime

def complete_string(num):
    string = str(num)
    return '0' * (3 - len(string)) + string

record = [None] * 11
vis = None
MOD = (None, None, 2, 3, 5, 7, 11, 13, 17)

def dfs(index):
    if index == 1:
        x = vis.index(True)
        if not x:
            return 0
        record[index] = str(x)
        return int(''.join(record[1:]))
    res = 0
    for x in range(10):
        if vis[x]:
            record[index] = str(x)
            if int(''.join(record[index: index + 3])) % MOD[index] == 0:
                vis[x] = False
                res += dfs(index - 1)
                vis[x] = True
    return res

def main():
    global record, vis
    res = 0
    for x in range(0, 1000, MOD[-1]):
        x_str = complete_string(x)
        vis = [x_str.count(str(i)) == 0 for i in range(10)]
        if vis.count(False) == 3:
            record[8:] = x_str
            res += dfs(7)
    return res

beg = datetime.datetime.now()
ans = main()
end = datetime.datetime.now()

print("answer:", ans)
print("time:", end - beg)
