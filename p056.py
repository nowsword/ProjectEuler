import datetime

def get_digit_sum(num):
    return sum(map(int, str(num)))

def main():
    MAX = 0
    for base in range(2, 100):
        num = 1
        for exp in range(1, 100):
            num *= base
            MAX = max(MAX, get_digit_sum(num))
    return MAX

beg = datetime.datetime.now()
ans = main()
end = datetime.datetime.now()

print("answer:", ans)
print("time:", end - beg)