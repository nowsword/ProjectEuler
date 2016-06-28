import datetime
from permutation import all_permutations
from prime import is_prime

def main():
    '''[sum(range(1, x + 1)) % 3 for x in range(1, 10)] => [1, 0, 0, 1, 0, 0, 1, 0, 0]'''
    MAX = 0
    x = ''.join(map(str,range(1, 5)))
    gener = all_permutations(x)
    for num in gener:
        if num[-1] in ('1', '3', '7', '9'):
            num = int(''.join(num))
            if is_prime(num):
                MAX = max(MAX, num)
    x = ''.join(map(str,range(1, 8)))
    gener = all_permutations(x)
    for num in gener:
        if num[-1] in ('1', '3', '7', '9'):
            num = int(''.join(num))
            if is_prime(num):
                MAX = max(MAX, num)
    return MAX

beg = datetime.datetime.now()
ans = main()
end = datetime.datetime.now()

print("answer:", ans)
print("time:", end - beg)
