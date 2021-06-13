from math import e, cos, sin
import numpy as np


def f(x):
    # for calculation of function in point x
    return (sin(x ** 4 + 5 * x - 6)) / (2 * e(-2 * x + 5))


def fTag(x):
    # for calculation of function prime in point x
    return (5 / 2) * (e(2 * x - 5) * cos((x ** 4) - 6 + 5 * x) + 2 * e(2 * x - 5) * (x ** 3) * cos(
        (x ** 4) - 6 + 5 * x) + math.e(2 * x))


def newton(x0, x1, eps):
    # Newton Raphson Method
    min = x0
    max = x1
    xi = x0
    iter = 1
    xiList = []
    fxList = []
    fTagxList = []

    while True:
        fxi = f(xi)
        fTagxi = df(xi)

        if (xi < min or xi > max) and xi < 0:
            xi = x1
        if xi < min or xi > max:
            break
        if fTagxi == 0:
            print("No solution found.")
            break
        if abs(fxi) <= eps:
            for i in range(len(xiList)):
                print(f"iteration = {i + 1} xi = {xiList[i]}, f(xi) = {fxList[i]}, f'(xi) = {fTagxList[i]}")
            print("*" * 50)
            print(f"Section [{min:.1f} ,{max:.1f}]: Found solution after {iter} iterations: {xi}")
            print("*" * 50)
            break

        xiList.append(xi)
        fxList.append(f(xi))
        fTagxList.append(df(xi))
        xi = xi - fxi / fTagxi
        iter += 1


if __name__ == "__main__":
    epsilon = 1e-6
    step = 0.1
    min_range = -1.1
    max_range = 2
    newton_section_list = []

    # Check if there is a root in a certain value range (in increments of 0.1)
    for i in np.arange(min_range, max_range, step):
        i = round(i, 2)
        if f(i) * f(i + 0.1) <= 0:
            newton_section_list.append((i, i + step))

    # Finding roots by Newton Raphson method:
    print("-" * 70)
    print("Roots :")
    print("-" * 70)

    # Sending X0 for which a root approximation is found
    if len(newton_section_list) == 0:
        print("cannot use Newton Raphson method")
    else:
        for section in newton_section_list:
            newton(section[0], section[1], epsilon)
