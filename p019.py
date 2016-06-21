import datetime

def isLeapYear(year):
    return year % 400 == 0 if year % 100 == 0 else year % 4 == 0

def main():
    res = 0
    day = 1
    for year in range(1900, 2001):
        for month in range(1, 13):
            if day == 0 and year != 1900:
                res += 1
            if month in (1, 3, 5, 7, 8, 10, 12):
                num = 31
            elif month != 2:
                num = 30
            else:
                num = 29 if isLeapYear(year) else 28
            day = (day + num) % 7
    return res 

beg = datetime.datetime.now()
ans = main()
end = datetime.datetime.now()

print("answer:", ans)
print("time:", end - beg)
