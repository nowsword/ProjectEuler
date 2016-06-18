import datetime

def change(char):
    if char != '0':
        return int(char)
    return 11

def main(string, size):
    length = len(string)
    value = -1
    maxvalue = -1
    for l in range(length - size + 1):
        r = l + size - 1
        if l == 0:
            temp = 1
            for i in range(l, r + 1):
                temp *= change(string[i])
            value = temp
        else:
            value = value // change(string[l - 1]) * change(string[r])
        maxvalue = max(maxvalue, value if value % 11 != 0 else 0)
    return maxvalue 

file = open('p008.in')
string = ''.join([line[:-1] for line in file])
file.close()

try:
    para = int(input())
except:
    para = 13

beg = datetime.datetime.now()
ans = main(string, para)
end = datetime.datetime.now()

print("answer:", ans)
print("time:", end - beg)
