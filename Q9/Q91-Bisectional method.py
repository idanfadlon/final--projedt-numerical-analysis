from math import e,sin


def f(x):
    # for calculation of function in point x
    return (sin(x ** 4 + 5 * x - 6)) / (2 * e**(-2 * x + 5))

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

def printRoots(rootsList):
    if None in rootsList:
        return
    for i in range(len(rootsList)):
        print("Root: {0}    Iterations: {1}\n".format(rootsList[i][0], rootsList[i][1]))
