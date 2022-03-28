# -*- coding:utf-8 -*-
'''
@File    :   成语接龙.py
@Time    :   2022/03/26 19:49:07
@Author  :   hyh
@Version :   1.0
@Contact :   1360895771@qq.com
@Desc    :   专选课作业：成语接龙
'''
# here put the import lib
import pypinyin as py
import random
from sympy import false, true
import Tortoise_and_rabbit_race
from turtle import*

#处理文本：读取文本数据，并存储在列表中
def getlist(filename):
    chengyu = []
    file = open(filename+".txt",'rt',encoding="utf-8")
    for line in file:
        list = line.split()
        chengyu.append(list[0])
    file.close()
    return chengyu

#随机获取成语列表中以指定字符开始的成语
def get_chengyu(list,startchengyu):
    end = startchengyu[-1:] #获取输入成语的最后一个字
    end_py = py.lazy_pinyin(end) #转换为拼音
    start_chengyu = [w for w in list if (py.lazy_pinyin(w[:1]) == end_py and not(w.startswith(end)) ) ] #匹配获得所有开头符合要求的成语
    if(start_chengyu):
        target_chengyu = start_chengyu[random.randint(0,len(start_chengyu)-1)]
        return target_chengyu
    else:
        return false

#进行指定次数的成语接龙
def jielong(n,start_chengyu):
    ed_chengyu = []
    for i in range(int(n)):
        if(get_chengyu(chengyulist,start_chengyu) and get_chengyu(chengyulist,start_chengyu) not in ed_chengyu):
        #判断是否出现过或者无法匹配
            pre_chengyu = start_chengyu
            start_chengyu = get_chengyu(chengyulist,start_chengyu)
            ed_chengyu.append(start_chengyu)
            result.append(start_chengyu)
        else:
            jielong(int(n)-i,pre_chengyu)
            break

#绘制学号条形码
def draw_bar_code(stu_number):
    binnum = bin(stu_number)
    num = str(binnum)[2:]
    print(num)
    penup()
    X, Y= 360, -320
    w, h= 3, 50
    for n in num:
       fillcolor("black" if n == "1" else "white")
       begin_fill()
       goto(X,Y)
       goto(X+w,Y)
       goto(X+w,Y+h)
       goto(X,Y+h)
       goto(X,Y)
       end_fill()
       X += w
    goto(350,-330)
    write(num,move = True, align="left", font=('微软雅黑',5,'bold'))


if __name__ == '__main__':

    #处理文本，获取成语列表
    File="7.公选课\作业\成语接龙"
    chengyulist = getlist(File)

    #测试用
    #file = open("成语.txt","wt",encoding="utf-8")
    #for chengyu in chengyulist:
    #    file.write(chengyu)
    #file.close()

    #获取接龙的开始成语
    #start_chengyu = input("请输入进行接龙的第一个词语:")
    start_chengyu = "龟兔赛跑"

    #根据用户需求进行一定次数的成语接龙
    #n = input("请输入接龙次数:")
    n = 10
    #print(get_chengyu(chengyulist,start_chengyu))

    result=[]
    jielong(n,start_chengyu)#调用递归函数jielong实现指定次数的接龙

    #绘图部分（调用了上次作业的模块）
    Tortoise_and_rabbit_race.draw()
    penup()
    #绘制接龙成语及个人信息
    for j in range(10):
        goto(350,200-50*j)
        write(result[j]+"\n\n",move = True, align="left", font=('宋体',20,'normal'))
    goto(280,-250)
    write("计201 侯云浩 42027150",move = True, align="left", font=('宋体',20,'normal'))
    #绘制条形码
    draw_bar_code("0000042027150")
    exitonclick()