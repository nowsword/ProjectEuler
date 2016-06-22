import datetime

def get_cycle_length(x):
    D = {}
    num = 1
    pos = 0
    while True:
        if num in D:
            return pos - D[num]
        D[num] = pos
        num = num % x * 10
        if num == 0:
            return 0
        pos += 1

def main(lt):
    maxvalue = 0
    num = 0
    for i in range(1, lt):
        temp = get_cycle_length(i)
        if temp > maxvalue:
            maxvalue = temp
            num = i
    return num

try:
    para = int(input())
except:
    para = int(1e3)

beg = datetime.datetime.now()
ans = main(para)
end = datetime.datetime.now()

print("answer:", ans)
print("time:", end - beg)
