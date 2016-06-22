import datetime

def fib():
    a = 1
    b = 1
    yield a
    yield b
    while True:
        (a, b) = (b, a + b)
        yield b

def main(num):
    gener = fib()
    index = 0
    while True:
        index += 1
        x = next(gener)
        if len(str(x)) == num:
            return index

try:
    para = int(input())
except:
    para = int(1e3)

beg = datetime.datetime.now()
ans = main(para)
end = datetime.datetime.now()

print("answer:", ans)
print("time:", end - beg)
