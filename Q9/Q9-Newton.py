from math import e, cos, sin
import numpy as np


def f(x):
    # for calculation of function in point x
    return (sin(x ** 4 + 5 * x - 6)) / (2 * e**(-2 * x + 5))


def fTag(x):
    # for calculation of function prime in point x
    return (5 / 2) * (e**(2 * x - 5) * cos((x ** 4) - 6 + 5 * x) + 2 * e**(2 * x - 5) * (x ** 3) * cos((x ** 4) - 6 + 5 * x) + e**(2 * x))


def newton(a, b, eps):
    # Newton Raphson Method
    min = a
    max = b
    xr_1 = a
    step = 1
    xr_1List = []
    fxList = []
    fTagxList = []

    while True:
        fxr_1 = f(xr_1)
        fTagxr_1 = fTag(xr_1)

        if (xr_1 < min or xr_1 > max) and xr_1 < 0:
            xr_1 = b
        if xr_1 < min or xr_1 > max:
            break
        if fTagxr_1 == 0:
            print("No roots foun\n")
            break

        if abs(fxr_1) < eps:
            for i in range(len(xr_1List)):
                print(f"step = {i + 1} xR+1 = {xr_1List[i]}, f(xR+1) = {fxList[i]}, f'(xR+1) = {fTagxList[i]}")
            print(f"Found root after {step} iterations in segment [{min:.1f} ,{max:.1f}]: root is {xr_1}")

            break

        xr_1List.append(xr_1)
        fxList.append(f(xr_1))
        fTagxList.append(fTag(xr_1))
        xr_1 = xr_1 - (fxr_1 / fTagxr_1)
        step += 1


def main():
    epsilon = 1e-7
    step = 0.1
    min_range = -1.5
    max_range = 1.5
    section_list = []

    # Check if there is a root in a certain value range (in increments of 0.1)
    for i in np.arange(min_range, max_range, step):
        i = round(i, 2)
        if f(i) * f(i + 0.1) <= 0:
            section_list.append((i, i + step))

    # Finding roots by Newton Raphson method:
    # Sending X0 for which a root approximation is found
    if len(section_list) == 0:
        print("cannot use Newton Raphson method")
    else:
        for section in section_list:
            newton(section[0], section[1], epsilon)
