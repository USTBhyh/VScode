# -*- coding:utf-8 -*-
'''
@File    :   bar_code.py
@Time    :   2022/03/27 10:01:42
@Author  :   hyh
@Version :   1.0
@Contact :   1360895771@qq.com
@Desc    :   None
'''
# here put the import lib
from turtle import*



if __name__ == '__main__':
    pass

def draw_bar_code(stu_number):
    binnum = bin(stu_number)
    num = str(binnum)[2:]
    print(num)
    penup()
    X, Y= 0, 0
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
    goto(-10,-10)
    write(num,move = True, align="left", font=('微软雅黑',5,'bold'))

draw_bar_code(420271500000)
exitonclick()