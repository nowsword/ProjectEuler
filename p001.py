import datetime

def main(lt):
    return sum(x for x in range(lt) if x % 3 == 0 or x % 5 == 0)

try:
    para = int(input())
except:
    para = 1000

beg = datetime.datetime.now()
ans = main(para)
end = datetime.datetime.now()

print("answer:", ans)
print("time:", end - beg)
