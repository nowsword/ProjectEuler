import datetime

def main(strings, size):
    return str(sum(map(int, strings)))[:size]
 
file = open('p013.in')
strings = file.read().splitlines()
file.close()

try:
    para = int(input())
except:
    para = 10

beg = datetime.datetime.now()
ans = main(strings, para)
end = datetime.datetime.now()

print("answer:", ans)
print("time:", end - beg)
