import datetime
from combine import factorial

maps = None
digit_count = None

def dfs(digit, rest, size):
    if rest == 0:
        all_digits = digit_count[:digit]
        key = sum(x * maps[i] for (i, x) in enumerate(all_digits))
        key_str = str(key)
        key_array = [key_str.count(str(i)) for i in range(digit)]
        return key if key_array == all_digits else 0

    if digit == 0:
        beg = 0
        end = rest - 1
    elif digit == 9: 
        beg = rest
        end = rest
    else:
        beg = 0
        end = rest

    res = 0
    for num in range(beg, end + 1):
        digit_count[digit] = num
        res += dfs(digit + 1, rest - num, size)
    return res

def main():
    global maps
    maps = [factorial(x) for x in range(10)]
    max_size = 2
    digit = maps[9]
    digit_sum = digit * max_size
    while True:
        if len(str(digit_sum)) < max_size:
            max_size -= 1
            break
        digit_sum += digit
        max_size += 1

    global digit_count
    digit_count = [None] * 10
    res = 0
    for size in range(2, max_size + 1):
        res += dfs(0, size, size)
    return res

beg = datetime.datetime.now()
ans = main()
end = datetime.datetime.now()

print("answer:", ans)
print("time:", end - beg)
