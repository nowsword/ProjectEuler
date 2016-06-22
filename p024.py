import datetime
import permutation

def main(rank):
    return ''.join(map(str, permutation.get_permutation(range(10), rank)))

try:
    para = int(input())
except:
    para = int(1e6)

beg = datetime.datetime.now()
ans = main(para)
end = datetime.datetime.now()

print("answer:", ans)
print("time:", end - beg)
