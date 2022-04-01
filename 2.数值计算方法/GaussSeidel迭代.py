# -*- coding:utf-8 -*-
'''
@File    :   Jacobi迭代.py
@Time    :   2022/04/01 08:58:44
@Author  :   hyh
@Version :   1.0
@Contact :   1360895771@qq.com
@Desc    :   GaussSeidel迭代法
'''
# here put the import lib
import math
import copy
import numpy as np
a = input("请输入自变量X的个数mu,以及方程个数nu:")
mu, nu = [int(i) for i in a.split(" ")]
b = input("请输入要求的误差精度e:")
e = float(b)
print(str(mu) + "  " + str(nu)+" "+str(e))

L, D, U = [], [], []  # 初始化LDU矩阵
for p in range(nu):
    L.append([]), D.append([]), U.append([])
    for q in range(mu):
        x_in = float(input("请输入第%d行第%d列的系数:" % (p + 1, q + 1)))
        if p > q:
            L[p].append(x_in), D[p].append(0), U[p].append(0)
        elif p == q:
            L[p].append(0), D[p].append(x_in), U[p].append(0)
        else:
            L[p].append(0), D[p].append(0), U[p].append(x_in)
L, D, U = np.array(L), np.array(D), np.array(U)

X_Current = []  # 自变量x矩阵
for q in range(mu):
    x_in = float(input("请输入X%d的初值为:" %q))
    X_Current.append(x_in)
X_Current = np.array(X_Current).T  # 将X行向量转置为列向量,便于后面矩阵的计算；

b_Const = []  # 因变量y矩阵
for p in range(nu):
    y_in = float(input("请输入第%d个方程的Y值:" % (p + 1)))
    b_Const.append(y_in)
b_Const = np.array(b_Const).T  # 将X行向量转置为列向量,便于后面矩阵的计算；

# 计算D+L
D_L = copy.deepcopy(L)
for p in range(nu):
    for q in range(mu):
        D_L[p][q] = D[p][q]+L[p][q]

G2 = np.dot(-np.linalg.inv(D_L), U)  # np.linalg.inv(D+L)求矩阵的逆
d2 = np.dot(np.linalg.inv(D_L), b_Const)


# x^(k+1) = G1*x^(k) + d1
X_New = copy.deepcopy(X_Current)  #  导入copy库，深度拷贝X_Current作为X_New的初始化；

epoch = 0  # 迭代次数
while 1:
    flag = 0  # 误差精度标记,统计达到精度要求的x数目，当X_New同一个epoch里所有的x迭代结果均达到精度时，输出X_New
    X_Current = X_New
    X_New = np.dot(G2, X_Current)
    for p in range(mu):
        X_New[p] = X_New[p] + d2[p]
        if math.fabs(X_New[p]-X_Current[p]) < e:
            flag += 1
    epoch += 1
    if epoch > 50:  # 根据GaussSeidel迭代收敛特性，设定迭代上限为50次；
        print("GaussSeidel迭代不收敛!")
        epoch = 0
        break

    if flag == mu:
        print("GaussSeidel迭代结果如下:")
        print(X_New)
        break

