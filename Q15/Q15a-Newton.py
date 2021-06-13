from math import e, cos, sin
import numpy as np
from sympy.utilities.lambdify import lambdify
import sympy as sp
x =sp.symbols('x')
f = (x * e**(-x**2+5*x-3) )*(x**2 +3*x-5)
f_prime = f.diff(x)


def f1(n):
    # for calculation of function in point x
    return f.subs(x,n)


def fTag(n):
    # for calculation of function prime in point x
    return f_prime.subs(x,n)
b=-2*e**(-x**2+5*x-3)*x**4-e**(-x**2+5*x-3)*x**3+28*e**(-x**2+5*x-3)*x**2-19*e**(-x**2+5*x-3)*x-5*e**(-x**2+5*x-3)
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
        fxr_1 = f1(xr_1)
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
        fxList.append(f1(xr_1))
        fTagxList.append(fTag(xr_1))
        xr_1 = xr_1 - (fxr_1 / fTagxr_1)
        step += 1


def main():
    epsilon = 1e-7
    step = 0.1
    min_range = 0
    max_range = 1.5
    section_list = []

    # Check if there is a root in a certain value range (in increments of 0.1)
    for i in np.arange(min_range, max_range, step):
        i = round(i, 2)
        if f1(i) * f1(i + 0.1) <= 0:
            section_list.append((i, i + step))

    # Finding roots by Newton Raphson method:
    # Sending X0 for which a root approximation is found
    if len(section_list) == 0:
        print("cannot use Newton Raphson method")
    else:
        for section in section_list:
            newton(section[0], section[1], epsilon)
main()