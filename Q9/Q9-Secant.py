#9b
import numpy as np
from math import e, sin



def secant_method(x0, x1, tol):
    x2 = 0
    min = x0
    max = x1
    iter = 1
    flag = True
    x1List = []
    x0List = []
    fxList = []

    while flag:
        if f(x0) == f(x1):
            print("Divide by zero error!")
            break

    #calc next iteration
        x2 = x0 - (x1 - x0) * f(x0) / (f(x1) - f(x0))
        if x2 > max or x2 < min:
            x2 = None
            break
    #update lists
        x0List.append(x0)
        x1List.append(x1)
        fxList.append(f(x0))
        x0 = x1
        x1 = x2
        iter += 1

        flag = abs(f(x2)) > tol
    if x2 is not None:
        for x0 in range(len(x0List)):
            print(f"iteration = {x0 + 1} x0 = {x0List[x0]}, x1 = {x1List[x0]}, f(x0) = {fxList[x0]}")
        print(f"Section [{min:.2f} ,{max:.2f}]: Found solution after {iter} iterations: {x2}")


def f(x):
    # for calculation of function in point x
    return (sin(x ** 4 + 5 * x - 6)) / (2 * e(-2 * x + 5))


def main9():
    epsilon = 0.0001
    start = -1.1
    end = 2
    step = 0.01
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

main9()