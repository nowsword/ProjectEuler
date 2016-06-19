import datetime

D = {1: 1}
def get(num):
    if num in D:
        return D[num]
    if num % 2 == 0:
        ans = get(num // 2) + 1
    else:
        ans = get(num * 3 + 1) + 1
    D[num] = ans
    return ans

def main(lt):
    maxvalue = 0
    res = 0
    for i in range(1, lt):
        temp = get(i)
        if temp > maxvalue:
            maxvalue = temp
            res = i
    return res

try:
    para = int(input())
except:
    para = int(1e6)

beg = datetime.datetime.now()
ans = main(para)
end = datetime.datetime.now()

print("answer:", ans)
print("time:", end - beg)
