from math import fabs


def fx(x):
    return x*x*x+4*x*x-10

def fx1(y):
    return 3*y*y+8*y

e=1e-5

a=1.5
for i in range(10):
    b=0
    if(fabs(a-b)>e):
        b=a
        a=a-fx(a)/fx1(a)
        print(a,b,a-b)
    else:
        print("!")
