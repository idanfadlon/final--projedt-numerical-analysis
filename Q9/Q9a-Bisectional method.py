from datetime import *
from math import e,sin,log,ceil,cos

import numpy as np
from sympy.utilities.lambdify import lambdify
import sympy as sp

roots = []

def f(x):
    # for calculation of function in point x
    return (sin(x ** 4 + 5 * x - 6)) / (2 * e**(-2 * x + 5))


def fTag(x):
    # for calculation of function prime in point x
    return (5 / 2) * (e**(2 * x - 5) * cos((x ** 4) - 6 + 5 * x) + 2 * e**(2 * x - 5) * (x ** 3) * cos((x ** 4) - 6 + 5 * x) + e**(2 * x))

def Bisection_Method(start_point, end_point, epsilon):


    value=subBisection(start_point, end_point, epsilon)
    if value != None:
        roots.append(value)
        return

    return



def subBisection(a, b,  eps):
    maxIter = int(ceil((-1) * (log(eps / (b - a)) / log(2))))
    iter = 0
    start=a
    end=b
    while abs(b - a) > eps:
        if maxIter >= iter:
            iter += 1
            c = (a + b) / 2
            fa = f(a)
            fc = f(c)
            if fa * fc > 0:  # ignore left section
                a = c
            else:
                b = c
            print(
                "step={0}  a = {1}| b = {2}| c = {3}|f(a)={3}|f(b)={4}|f(c)={5}\n".format(iter, a, b, c, fa, fc, f(b)))
        else:
            print("Cannot solve by bisection method!\n")
            return
    now = datetime.now()
    str = '{0}{1}{2}'.format(now.day, now.hour, now.minute)
    print(" Found root after {0} Iteration in segment [{1} ,{2}]: ".format(iter, start, end, )+f'root is {c}00000{str}')
    return f'{c}00000{str}'


def main():
    epsilon = 0.00000001
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
            Bisection_Method(section[0],section[1],epsilon)
    print("\nAll rotts:\n")
    for i in range(len(roots)):
        print(roots[i] + '\n')

main()