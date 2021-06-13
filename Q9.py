from datetime import *
from decimal import getcontext, Decimal


import math
import sympy as sy
from sympy import exp
from sympy.utilities.lambdify import lambdify

x = sy.symbols('x')

def printRoots(rootsList):
    if None in rootsList:
        return
    for i in range(len(rootsList)):
        print("Root: {0}    Iterations: {1}\n".format(rootsList[i][0], rootsList[i][1]))


def Bisection_Method(polynomial, start_point, end_point, epsilon):
    check = findSuspects(polynomial, start_point, end_point)
    roots = []

    for i in range(len(check)):  # for every suspected section found
        a = check[i][0]
        b = check[i][1]
        roots.append(subBisection(a, b, polynomial, epsilon))

    p_prime = polynomial.diff(x)
    check = findSuspects(p_prime, start_point, end_point)
    for i in range(len(check)):  # for every suspected section found
        a = check[i][0]
        b = check[i][1]
        tup = subBisection(a, b, polynomial, epsilon)
        res = polynomial.subs(x, tup[0])
        if res + epsilon >= 0 and res - epsilon <= 0:
            print("Root: {0}    Iterations: {1}\n".format(0, tup[1]))
        else:
            continue
    for i in range(len(roots) - 1):
        if roots[i][0] + epsilon >= 0 and roots[i][0] - epsilon <= 0:
            del roots[i]

    printRoots(roots)


def subBisection(a, b, p, eps):
    maxIter = int(math.ceil((-1) * (math.log(eps / (b - a)) / math.log(2))))
    iter = 0
    while abs(b - a) > eps:
        if maxIter >= iter:
            iter += 1
            c = (a + b) / 2
            fa = p.subs(x, a)
            fb = p.subs(x, b)
            fc = p.subs(x, c)
            if fa * fc > 0:  # ignore left section
                a = c
            else:
                b = c
        else:
            print("Cannot solve by bisection method!\n")
            return
    return (c, iter)


def Newton_Raphson(polynomial, start_point, end_point, epsilon):
    check = findSuspects(polynomial, start_point, end_point)
    roots = []
    p_prime = polynomial.diff(x)
    for i in range(len(check)):  # for every suspected section found
        a = check[i][0]
        b = check[i][1]
        roots.append(subNewtonRaphson(a, b, polynomial, epsilon, p_prime))

    p_sec_prime = p_prime.diff(x)
    check = findSuspects(p_prime, start_point, end_point, )
    if None not in check:
        for i in range(len(check)):  # for every suspected section found
            a = check[i][0]
            b = check[i][1]
            tup = subNewtonRaphson(a, b, polynomial, epsilon, p_sec_prime)
            res = polynomial.subs(x, tup[0])
            if res + epsilon >= 0 and res - epsilon <= 0:
                roots.append(tup)
            else:
                continue

        for i in range(len(roots) - 1):
            if roots[i][0] + epsilon >= 0 and roots[i][0] - epsilon <= 0:
                del roots[i]

    printRoots(roots)


def subNewtonRaphson(a, b, p, eps, p_prime):
    maxIter = int(math.ceil((-1) * (math.log(eps / (b - a)) / math.log(2))))
    iter = 0
    c = (a + b) / 2
    while True:
        if maxIter >= iter:
            iter += 1
            fc = p.subs(x, c)
            fTagC = p_prime.subs(x, c)
            prevC = c
            c = prevC - (fc / fTagC)
            if fc == 0 or abs(c - prevC) <= eps:
                return (c, iter)
            else:
                continue
        else:
            print("Cannot solve by Newton-Raphson method!\n")
            return


def Secant_Method(polynomial, start_point, end_point, epsilon):
    check = findSuspects(polynomial, start_point, end_point)
    roots = []
    p_prime = polynomial.diff(x)
    for i in range(len(check)):  # for every suspected section found
        a = check[i][0]
        b = check[i][1]
        roots.append(subSecant(a, b, polynomial, epsilon))

        check = findSuspects(p_prime, start_point, end_point, )

        for i in range(len(check)):  # for every suspected section found
            a = check[i][0]
            b = check[i][1]
            tup = subSecant(a, b, polynomial, epsilon)
            res = polynomial.subs(x, tup[0])
            if res + epsilon >= 0 and res - epsilon <= 0:
                roots.append(tup)
            else:
                continue

        printRoots(roots)


def subSecant(a, b, p, eps):
    maxIter = int(math.ceil((-1) * (math.log(eps / (b - a)) / math.log(2))))
    iter = 0
    i = 1
    nexti = 2
    while abs(nexti - i) > eps:
        if maxIter >= iter:
            iter += 1
            fi = p.subs(x, i)
            fNexti = p.subs(x, nexti)
            temp = nexti
            nexti = float(i-(fi*((nexti-i)/(fNexti-fi))))
            i = temp
            if abs(fi) <= eps:
                break
        else:
            print("Cannot solve by Secant Method!\n")
            return
    return (i, iter)


def findSuspects(polynomial, start, end):
    suspect = []
    sections = 0.1
    i = round(start + sections, 2)
    r1 = polynomial.subs(x, start)

    while i <= end:
        r2 = polynomial.subs(x, i)
        if r1 * r2 < 0:
            suspect.append((round(i - sections, 2), i))
        if r2 == 0:
            suspect.append((round(i - sections, 2), i + sections))
        r1 = r2
        i = round(i + sections, 2)

    floatList = []
    for i in range(len(suspect)):
        floatList.append((float(suspect[i][0]), float(suspect[i][1])))
    return floatList

def main():
    polynomial = sy.exp((math.sin(x ** 4 + 5 * x - 6)) / (2 * math.e ** (-2 * x + 5)))
    start = -1.5
    end = 1.5
    epsilon = 0.0001
    Bisection_Method(polynomial, start, end, epsilon)
    Newton_Raphson(polynomial, start, end, epsilon)
    Secant_Method(polynomial, start, end, epsilon)

main()

