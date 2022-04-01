# -*- coding:utf-8 -*-
'''
@File    :   Jacobi.py
@Time    :   2022/04/01 09:35:58
@Author  :   hyh
@Version :   1.0
@Contact :   1360895771@qq.com
@Desc    :   高斯赛德尔迭代
'''
# here put the import lib
from numpy import *
def g_s(a,b,x0,eps):
    D = diag(diag(a))
    L = -tril(a,-1)
    U = -triu(a,1)
    B = linalg.inv(D-L)*U
    f = linalg.inv(D-L)*b
    y = B*x0+f
    print(y)
    print(B*y + f)
    n = 1
    #while linalg.norm(y-x0)>=eps:
    #for i in range(5):
    x=y.copy()
    y = B*x + f
    n=n+1
    return x0

a = array ([[14.000,2.0,1.0,5.0],
              [8.0,17.0,2.0,10.0],
              [4.0,18.0,3.0,6.0],
              [12.0,26.0,11.0,20.0]])
b = array([[1.000],[2.0],[3.0],[4.0]])
x0 = array([[0.000,0.0,0.0,0.0],
            [0.0,0.0,0.0,0.0],
            [0.0,0.0,0.0,0.0],
            [0.0,0.0,0.0,0.0]])
y = g_s(a,b,x0,0.00001)
print(y)