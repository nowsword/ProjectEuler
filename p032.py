import datetime
from permutation import all_permutations

def get_num(L):
    return int(''.join(L))

def main():
    string = ''.join(map(str, range(1, 10)))
    gener = all_permutations(string)
    S = set()
    for permu in gener:
        a1 = get_num(permu[:1])
        b1 = get_num(permu[1:-4])
        a2 = get_num(permu[:2])
        b2 = get_num(permu[2:-4])
        c = get_num(permu[-4:])
        if a1 * b1 == c or a2 * b2 == c:
            S.add(c)
    return sum(S)

beg = datetime.datetime.now()
ans = calc()
end = datetime.datetime.now()

print("answer:", ans)
print("time:", end - beg)
