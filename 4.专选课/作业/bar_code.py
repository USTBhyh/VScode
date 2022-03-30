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
""" from pystrich.ean13 import EAN13Encoder
encoder = EAN13Encoder("4202715020223")
encoder.save("pyStrich.png")
 """

code_table={
    "left":{
        0:'0001101',
        1:'0011001',
        2:'0010011',
        3:'0111101',
        4:'0100011',
        5:'0110001',
        6:'0101111',
        7:'0111011',
        8:'0110111',
        9:'0001011'
    },
    "right":{
        0:'1110010',
        1:'1100110',
        2:'1101100',
        3:'1000010',
        4:'1011100',
        5:'1001110',
        6:'1010000',
        7:'1000100',
        8:'1001000',
        9:'1110100'
    }
}
def make_code(number):
    START_END = "01010"
    MID = "101"
    output = START_END
    for i in number[:6]:
        output += code_table["left"][i]
    output +=MID
    for i in number[6:]:
        output += code_table['right'][i]
    output += START_END
    return output

def draw_bar_code(stu_number):
    num = str(stu_number)
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
    #write(num,move = True, align="left", font=('微软雅黑',5,'bold'))

ori_number=[4,2,0,2,7,1,5,0]
code_number = make_code(ori_number)
draw_bar_code(code_number)

exitonclick()