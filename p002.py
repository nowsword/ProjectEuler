import datetime

def even_fib(le = None):
    a = 1
    b = 1
    while True:
        c = a + b
        if le and c > le:
            return
        yield c
        a = b + c
        b = c + a

def main(le):
    return sum(even_fib(le))

try:
    para = int(input())
except:
    para = int(4e6)

beg = datetime.datetime.now()
ans = main(para)
end = datetime.datetime.now()

print("answer:", ans)
print("time:", end - beg)
