# -*- coding:utf-8 -*-
'''
@File    :   文件读写.py
@Time    :   2022/03/24 08:10:22
@Author  :   hyh
@Version :   1.0
@Contact :   1360895771@qq.com
@Desc    :   None
'''
# here put the import lib
import operator
import re
from unittest import result

f1=open('rt.txt','rt')
f2=open('wt.txt','wt')
f2.write(f1.read().upper())#read()函数：默认读取所有字符
f1.close()
f2.close()

with open('wt.txt') as f3:
    f3.read().lower()

#找出最长行
f1 = open('zenofpython.txt','rt')
max=0
for line in f1:
    if len(line)>max:
        max=len(line)
f1.close()
print('最长行长度为:',max)

#python写法
#with open('rt.txt') as f:
#   print(max(map(len,f)))
""" 
def find_len_of_longest_line(filename):
    input=open(filename)
    len_list = [len(line)for line in input]
    input.close()
    print("result=",max(len_list))

find_len_of_longest_line('zenofpython.txt')
 """
#error:'int' object is not callable
#总学习时间及日平均时间



#综合练习--词频统计
# dic={}
# with open('zenofpython.txt') as f:
#     words=f.read().split()
#     for word in words:
#         if word not in dic:
#             dic[word]=1
#         else:
#             dic[word]=dic[word]+1
# print(dic)
#
with open('zenofpython.txt') as f:
    words=f.read().split()
    word_list=set(words)
    word_fre={
        i:words.count(i) for i in word_list
    }
#result = sorted(word_fre.items(),key=operator.itemgetter(1),reverse=True)
result = [(v,k)for k,v in word_fre.items()]
result.sort()
for v,k in result[:-10:-1]:
    print(f"Word{k},occurs {v} times")
#from collections import Counter

#matplotlib绘图库
import matplotlib
#jieba 中文分词函数库