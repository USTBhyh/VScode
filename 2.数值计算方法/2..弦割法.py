from math import fabs


def fx(x):
    return x*x*x-3*x*x-x+9
e=1e-4
a,b,c=-2,-1,0
for i in range(10):
        print(a,b)
        c=a-(fx(a)/(fx(a)-fx(b)))*(a-b)
        b=a
        a=c
        print(c,fx(c))
