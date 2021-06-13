from datetime import *


def random(start, end, param):
    sec = datetime.now()
    sec = sec.second
    total = sec + param
    while True:
        if total >= end:
            total -= param
        if total <= start:
            total += param
        if total >= start and total <= end:
            break

    return total


def main():
    aviya = 209203991
    idan = 208057505
    lihi = 206902736
    matan = 205639800

    print("question chosen from 1-9 : {} ".format(random(1, 9, aviya % 10)))
    print("question chosen from 10-18 : {} ".format(random(10, 18, idan % 10)))
    print("question chosen from 10-18 : {} ".format(random(10, 18, matan // 100 % 10)))
    print("question chosen from 19-30 : {} ".format(random(19, 30,lihi % 10 )))
    print("question chosen from 19-30 : {} ".format(random(19, 30, aviya % 10)))
    print("question chosen from 31-36 : {} ".format(random(31, 36, idan % 10)))
    now=datetime.now()
    str='{0}{1}{2}'.format(now.day,now.hour,now.minute)
    print(str)

main()
