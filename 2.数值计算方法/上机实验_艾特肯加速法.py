#coding = "UTF-8"
#艾特肯加速法求解方程
from math import fabs, log,e

def fx(x):#方程函数定义
    return e**x+3*x*x*x-2*x*x+log(x,e)-1

def gx(x):#迭代方程
    return ((2/3)*x*x-log(x,e)/3+1/3-e**x/3)**(1/3)

"""
def gx(x):#迭代方程
    return ((e**x+3*x*x*x+log(x,e)-1)/2)**0.5
"""
#参数定义
max=10
k=0
x0,x1,x=0.5,0.5,1
exp=1e-4
#迭代主体
while(fabs(x-x1)>exp and k<max):
    x1=x0
    x=x0-(((gx(x0)-x0)**2)/(gx(gx(x0))-2*gx(x0)+x0))
    x0=x
    k=k+1
    print(k,x)
print("最终结果:",x,"\n迭代次数:",k," ")#输出迭代结果
