import datetime

def main(le):
    D = {}
    D[1] = 'one' 
    D[2] = 'two'
    D[3] = 'three'
    D[4] = 'four'
    D[5] = 'five'
    D[6] = 'six'
    D[7] = 'seven'
    D[8] = 'eight'
    D[9] = 'nine'
    D[10] = 'ten'
    D[11] = 'eleven'
    D[12] = 'twelve'
    D[13] = 'thirteen'
    D[14] = 'fourteen'
    D[15] = 'fifteen'
    D[16] = 'sixteen'
    D[17] = 'seventeen'
    D[18] = 'eighteen'
    D[19] = 'nineteen'
    D[20] = 'twenty'
    D[30] = 'thirty'
    D[40] = 'forty'
    D[50] = 'fifty'
    D[60] = 'sixty'
    D[70] = 'seventy'
    D[80] = 'eighty'
    D[90] = 'ninety'
    for i in range(2, 10):
        for j in range(1, 10):
            D[i * 10 + j] = D[i * 10] + ' ' + D[j]
    for i in range(1, 10):
        D[i * 100] = D[i] + ' hundred'
        for j in range(1, 100):
            D[i * 100 + j] = D[i] + ' hundred and ' + D[j]
    D[1000] = D[1] + ' thousand'
    return sum(map(lambda x: len(D[x]) - D[x].count(' '), range(1, le + 1)))

try:
    para = int(input())
except:
    para = 1000

beg = datetime.datetime.now()
ans = main(para)
end = datetime.datetime.now()

print("answer:", ans)
print("time:", end - beg)
