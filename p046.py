import datetime
from prime import is_prime

def yes(num):
    for i in range(1, num + 1):
        x = 2 * i ** 2
        if x >= num:
            break
        if is_prime(num - x):
            return True
    return False

def main():
    x = 1
    while True:
        x += 2
        if not is_prime(x) and not yes(x):
            return x

beg = datetime.datetime.now()
ans = main()
end = datetime.datetime.now()

print("answer:", ans)
print("time:", end - beg)
