import datetime

def main(numbers):
    size = len(numbers)
    for i in range(size - 2, -1, -1):
        for j in range(i + 1):
            numbers[i][j] += max(numbers[i + 1][j], numbers[i + 1][j + 1])
    return numbers[0][0]

file = open('p067.in')
numbers = [list(map(int, line.split())) for line in file]
file.close()

beg = datetime.datetime.now()
ans = main(numbers)
end = datetime.datetime.now()

print("answer:", ans)
print("time:", end - beg)
