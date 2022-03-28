#coding = "UTF-8"
#弦割法求解方程
from math import fabs, log,e

def fx(x):#方程函数定义
    return e**x+3*x*x*x-2*x*x+log(x,e)-1

#参数定义
exp=1e-4
x1,x0,x2=1,0.5,1
x=0
k=0
max=20
#迭代主体
while(fabs(x-x2)>exp and k<max):
    x2=x1
    x=x1-(fx(x1)/(fx(x1)-fx(x0)))*(x1-x0)
    x0=x1
    x1=x
    k=k+1
    print(k,x,x1,x0," ")
print("最终结果:",x,"\n迭代次数:",k," ")