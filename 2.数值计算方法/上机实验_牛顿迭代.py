#coding = "UTF-8"
#牛顿迭代法求解方程
from math import fabs, log,e

def fx(x):#方程函数定义
    return e**x+3*x*x*x-2*x*x+log(x,e)-1

def fx1(x):
    return e**x+9*x*x-4*x+1/x

#参数定义
x=0.5
MAX=10
exp=1e-4
k=0
x1=1
#迭代主体
while(k<MAX and fabs(x-x1)>exp):#迭代结束条件
    x1=x
    x=x-fx(x)/fx1(x)
    k=k+1
    print(k,x,x-x1)
print("最终结果:",x,"\n迭代次数:",k," ")#输出迭代结果
