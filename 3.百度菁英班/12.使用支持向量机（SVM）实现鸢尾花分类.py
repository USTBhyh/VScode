# -*- coding:utf-8 -*-
'''
@File    :   12.使用支持向量机(SVM)实现鸢尾花分类.py
@Time    :   2022/03/30 16:29:45
@Author  :   hyh
@Version :   1.0
@Contact :   1360895771@qq.com
@Desc    :   
'''
# here put the import lib
import numpy as np
from matplotlib import colors
from sklearn import svm 
from sklearn import model_selection
import matplotlib.pyplot as plt
import matplotlib as mpl
#加载数据，切分数据集
# ======将字符串转化为整形==============
def iris_type(s):
    it = {b'Iris-setosa':0, b'Iris-versicolor':1,b'Iris-virginica':2} 
    return it[s]
    
# 1 数据准备
# 1.1 加载数据
data = np.loadtxt('data/data2301/iris.data',  # 数据文件路径i
                  dtype=float,    # 数据类型
                  delimiter=',',  # 数据分割符
                  converters={4:iris_type}) # 将第五列使用函数iris_type进行转换
# 1.2 数据分割
x, y = np.split(data, (4, ), axis=1) # 数据分组 第五列开始往后为y 代表纵向分割按列分割
x = x[:, :2]
x_train, x_test, y_train, y_test=model_selection.train_test_split(x, y, random_state=1, test_size=0.2)
print(x.shape,x_train.shape,x_test.shape)
