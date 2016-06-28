import datetime
import bisect

L = [1]

def is_triangle_num(num):
    length = len(L)
    last = L[-1]
    if num <= last:
        return num == L[bisect.bisect_left(L, num)]
    while True:
        length += 1
        last += length
        L.append(last)
        if last == num:
            return True
        if last > num:
            return False

def is_triangle_word(word):
    return is_triangle_num(sum(map(lambda letter: ord(letter) - ord('A') + 1 ,word[1:-1])))

def main(words):
    return len(list(filter(is_triangle_word, words)))

file = open('p042.in')
words = file.readline().strip().split(',')
file.close()

beg = datetime.datetime.now()
ans = main(words)
end = datetime.datetime.now()

print("answer:", ans)
print("time:", end - beg)
