# -*- coding:utf-8 -*-
import os

"""
合并多个txt
"""

# 获取目标文件夹的路径
path = "D:\practice\output\\1-officetable"
# 获取当前文件夹中的文件名称列表
filenames = os.listdir(path)
result = "D:\practice\output\\1-officetable\\result_newkitchen.txt"
# 打开当前目录下的result.txt文件，如果没有则创建
file = open(result, 'w+', encoding="utf-8")
# 向文件中写入字符

# 先遍历文件名
for filename in filenames:
    filepath = path + '/'
    filepath = filepath + filename
    # 遍历单个文件，读取行数
    for line in open(filepath, encoding="utf-8"):
        file.writelines(line)
    file.write('\n')    # 关闭文件
