from datetime import *
from math import e, sin


def f(x):
    # for calculation of function in point x
    return (sin(x ** 4 + 5 * x - 6)) / (2 * e ** (-2 * x + 5))


def trapArea(a, b):
    # calculates trapeze area
    return 0.5 * (b - a) * (f(a) + f(b))


def trapeze():
    a = -0.5
    b = 0.5
    sec = 0.001
    previ = a
    i = a + sec
    sum = 0
    while i <= b:
        sum += trapArea(previ, i)
        previ = i
        i += sec
    now = datetime.now()
    str = '{0}{1}{2}'.format(now.day, now.hour, now.minute)
    print(f"Trapeze Method Answer:{sum}00000{str}\n\n")


trapeze()


def createMat(size):
    newMat = []
    for i in range(size):
        newMat.append([])
        for j in range(size):
            newMat[i].append(0)
    return newMat


def rumberg(a, b, n):
    r = createMat(n + 1)
    h = b - a
    r[0][0] = 0.5 * h * (f(a) + f(b))

    powerOf2 = 1
    for i in range(1, n + 1):
        h = 0.5 * h
        sum = 0.0
        powerOf2 = 2 * powerOf2
        for k in range(1, powerOf2, 2):
            sum = sum + f(a + k * h)
        r[i][0] = 0.5 * r[i - 1][0] + sum * h

        powerOf4 = 1
        for j in range(1, i + 1):
            powerOf4 = 4 * powerOf4
            r[i][j] = r[i][j - 1] + (r[i][j - 1] - r[i - 1][j - 1]) / (powerOf4 - 1)

    return r


def main_rumberg():
    start = -0.5
    end = 0.5
    n = 10

    temp_return_val = rumberg(start, end, n)
    temp_return_val = temp_return_val[-1][-1]
    epsilon = 1e-6
    while epsilon > 1e-6:
        n += 1
        return_val = rumberg(start, end, n)
        return_val = return_val[-1][-1]
        epsilon = abs(temp_return_val - return_val)
        if epsilon >= 1e-6:
            temp_return_val = return_val
        else:
            n -= 1

    rumberg_temp = rumberg(start, end, n)

    for i in range(len(rumberg_temp)):
        for j in range(len(rumberg_temp)):
            if rumberg_temp[i][j] != 0:
                print(rumberg_temp[i][j], end=" ")
        print(" ")

    print(f"Section [{start}, {end}] is divided into n = {int(n)} "
          f"sections in order to achieve the accuracy of {epsilon}")
    now = datetime.now()
    str = '{0}{1}{2}'.format(now.day, now.hour, now.minute)
    print(f"Rumberg Method Answer = {temp_return_val}00000{str}")


main_rumberg()
