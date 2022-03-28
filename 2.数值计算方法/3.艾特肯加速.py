

from traceback import print_tb


def gx(x):
    return (10/(x+4))**0.5

x0=1.5
e=1e-4

for i in range(10):
    y=gx(x0)
    z=gx(y)
    a=(y-x0)**2
    b=z-2*y+x0
    c=x0-a/b
    print(x0,c,c-x0)
    x0=c
    
