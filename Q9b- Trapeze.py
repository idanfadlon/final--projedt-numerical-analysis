from datetime import *
from math import e, sin

def f(x):
    # for calculation of function in point x
    return (sin(x ** 4 + 5 * x - 6)) / (2 * e**(-2 * x + 5))

def trapArea(a,b):
    return 0.5*(b-a)*(f(a)+f(b))

def trapeze():
    a=-0.5
    b=0.5
    sec=0.001
    previ=a
    i=a+sec
    sum=0
    while i<=b:
        sum+=trapArea(previ,i)
        previ=i
        i+=sec
    now = datetime.now()
    str = '{0}{1}{2}'.format(now.day, now.hour, now.minute)
    print(f"{sum}00000{str}")
trapeze()