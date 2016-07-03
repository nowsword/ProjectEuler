import datetime

def Royal_Flush(hand):
    for i in range(5):
        if hand[i][0] != 10 + i:
            return False
        if hand[i][1] != hand[0][1]:
            return False
    return True

def Straight_Flush(hand):
    for i in range(5):
        if hand[i][0] != hand[0][0] + i:
            return False
        if hand[i][1] != hand[0][1]:
            return False
    return hand[0][0]

def Four_of_a_Kind(hand):
    for i in range(2):
        if hand[i][0] == hand[i + 1][0] == hand[i + 2][0] == hand[i + 3][0]:
            return hand[i][0]
    return False

def Full_House(hand):
    if hand[2][0] == hand[1][0]:
        if hand[0][0] == hand[1][0] and hand[3][0] == hand[4][0]:
            return hand[2][0]
        return False
    if hand[2][0] == hand[3][0]:
        if hand[4][0] == hand[3][0] and hand[0][0] == hand[1][0]:
            return hand[2][0]
        return False
    return False

def Flush(hand):
    for i in range(1, 5):
        if hand[i][1] != hand[0][1]:
            return False
    return tuple(hand[i][0] for i in range(4, -1, -1))

def Straight(hand):
    for i in range(5):
        if hand[i][0] != hand[0][0] + i:
            return False
    return hand[0][0]

def Three_of_a_Kind(hand):
    for i in range(3):
        if hand[i][0] == hand[i + 1][0] == hand[i + 2][0]:
            return hand[i][0]
    return False

def Two_Pairs(hand):
    L = list(range(5))
    res = []
    for i in range(3, -1, -1):
        if hand[i][0] == hand[i + 1][0]:
            res.append(hand[i][0])
            L.remove(i)
            L.remove(i + 1)
    if len(L) == 1:
        res.append(hand[L[0]][0])
        return tuple(res)
    return False

def One_Pair(hand):
    for i in range(4):
        if hand[i][0] == hand[i + 1][0]:
            return hand[i][0]
    return False

def High_Card(hand):
    return tuple(hand[i][0] for i in range(4, -1, -1))

def win_first(poker):
    func_list = (Royal_Flush, Straight_Flush, Four_of_a_Kind,
                 Full_House, Flush, Straight, Three_of_a_Kind,
                 Two_Pairs, One_Pair, High_Card)
    for func in func_list:
        A = func(poker[0])
        B = func(poker[1])
        if A:
            if B:
                return A > B
            return True
        elif B:
            return False
    return False

def main(strings):
    D = {str(x):x for x in range(2, 10)}
    D['T'] = 10
    D['J'] = 11
    D['Q'] = 12
    D['K'] = 13
    D['A'] = 14

    res = 0
    for string in strings:
        L = string.split()
        hand1 = [(D[x[0]], x[1]) for x in L[:5]]
        hand2 = [(D[x[0]], x[1]) for x in L[5:]]
        hand1.sort()
        hand2.sort()
        poker = (tuple(hand1), tuple(hand2))

        if win_first(poker):
            res += 1
    return res

file = open('p054.in')
strings = list(file)
file.close()

beg = datetime.datetime.now()
ans = main(strings)
end = datetime.datetime.now()

print("answer:", ans)
print("time:", end - beg)
