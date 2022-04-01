# -*- coding:utf-8 -*-
'''
@File    :   Jacobi.py
@Time    :   2022/04/01 09:35:58
@Author  :   hyh
@Version :   1.0
@Contact :   1360895771@qq.com
@Desc    :   雅可比迭代法
'''
# here put the import lib
from numpy import *
def jacobi(a,b,x0,eps):
    D = diag(diag(a))
    L = -tril(a,-1)
    U = -triu(a,1)
    B = D/(L+U)
    print(B)
    f = D/b
    y = B*x0+f
    n = 1
    while linalg.norm(y-x0)>=eps:
        x0=y
        y=B*x0+f
        n=n+1
    return x0

a = array ([[14,2,1,5],
              [8,17,2,10],
              [4,18,3,6],
              [12,26,11,20]])
b = arange(1,5)
x0 = array([0,0,0,0])
x1 = jacobi(a,b,x0,0.0001)
