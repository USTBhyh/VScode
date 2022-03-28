#coding = "UTF-8"
#二分法求解方程
from math import fabs, log,e


def fx(x):#方程函数定义
    return e**x+3*x*x*x-2*x*x+log(x,e)-1

#参数定义
MAX=50
exp=1e-4
a,b,k=0,1,1
y1=fx(b)

while(1):
    x=(a+b)/2
    y=fx(x)
    if fabs(y)<exp:
        break
    if y1*y<0:
        b=x
    else:a,y1=x,y
    if b-a<exp:
        break
    else:k=k+1
print(k,x,y,sep=" ")
