import datetime

def get(name):
    return sum(ord(x) - ord('A') + 1 for x in name if x != '"')

def main(names):
    names.sort()
    return sum((x + 1) * get(name) for (x, name) in enumerate(names))

file = open('p022.in')
string = file.readline().strip()
names = string.split(',')
file.close()

beg = datetime.datetime.now()
ans = main(names)
end = datetime.datetime.now()

print("answer:", ans)
print("time:", end - beg)
