# -*- coding:utf-8 -*-
'''
@File    :   上机实验_高斯消元法.py
@Time    :   2022/04/01 08:06:57
@Author  :   hyh
@Version :   1.0
@Contact :   1360895771@qq.com
@Desc    :   高斯消元法
'''
# here put the import lib
import numpy as np
def Gauss(a):
    for i in range(4):
        m = a[i+1][i]/a[i][i]

a = np.array ([14,2,1,5],
              [8,17,2,10],
              [4,18,3,6],
              [12,26,11,20])
b = [1,2,3,4]
n = 4
