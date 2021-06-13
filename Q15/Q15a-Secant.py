#9a
import numpy as np
from math import e, sin
from datetime import *

RootsList=[]
def f(x):
    # for calculation of function in point x
    return (x * e**(-x**2+5*x-3) )*(x**2 +3*x-5)


def secant_method(a, b, eps):
    xr_1 = 0
    min = a
    max = b
    Iteration = 1
    flag = True
    xr_1List = []
    xr_List = []
    fxList = []

    while flag:
        if f(a) == f(b):
            break

    #calc next point
        xr_1 = a - (b - a) * f(a) / (f(b) - f(a))

        if xr_1 > max or xr_1 < min:
            xr_1 = None
            break
    #update lists
        xr_List.append(a)
        xr_1List.append(b)
        fxList.append(f(a))
        a = b
        b = xr_1
        Iteration += 1
        flag = abs(xr_1-a) > eps
    if xr_1 is not None:
        for i in range(len(xr_List)):
            print(f"step = {i + 1} xR = {xr_List[i]}, xR+1 = {xr_1List[i]}, f(xR) = {fxList[i]}")
        now = datetime.now()
        str = '{0}{1}{2}'.format(now.day, now.hour, now.minute)
        RootsList.append('{0}00000{1}'.format(xr_1,str))
        print(f" Found root after {Iteration} Iteration in segment [{min:.2f} ,{max:.2f}]: root is {xr_1}")



def main9():
    epsilon = 0.0000000000001
    start = -1.5
    end = 1.5
    step = 0.1
    secant_section_list = []

    for i in np.arange(start, end, step):
        i = round(i, 2)
        if f(i) * f(i + 0.1) <= 0:
            secant_section_list.append((i, i + step))

    print("Roots by secant method ")

    if len(secant_section_list) == 0:
        print("No roots were found using a secant method")
    else:
        for section in secant_section_list:
            secant_method(section[0], section[1], epsilon)
    for i in range (len(RootsList)):
        print(RootsList[i]+'\n')
main9()