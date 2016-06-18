import datetime

def main(numbers, size):
    lengthx = len(numbers)
    lengthy = len(numbers[0])
    maxvalue = -1
    for i in range(0, lengthx - size + 1):
        for j in range(0, lengthy):
            temp = 1
            for k in range(size):
                temp *= numbers[i + k][j]
            maxvalue = max(maxvalue, temp)
    for i in range(0, lengthx):
        for j in range(0, lengthy - size + 1):
            temp = 1
            for k in range(size):
                temp *= numbers[i][j + k]
            maxvalue = max(maxvalue, temp)
    for i in range(0, lengthx - size + 1):
        for j in range(0, lengthy - size + 1):
            temp = 1
            for k in range(size):
                temp *= numbers[i + k][j + k]
            maxvalue = max(maxvalue, temp)
    for i in range(0, lengthx - size + 1):
        for j in range(size - 1, lengthy):
            temp = 1
            for k in range(size):
                temp *= numbers[i + k][j - k]
            maxvalue = max(maxvalue, temp)
    return maxvalue

file = open('p011.in')
numbers = [list(map(int, line.split())) for line in file]
file.close()

try:
    para = int(input())
except:
    para = 4

beg = datetime.datetime.now()
ans = main(numbers, para)
end = datetime.datetime.now()

print("answer:", ans)
print("time:", end - beg)
