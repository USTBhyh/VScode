from random import randint
from time import sleep
from turtle import*
from math import*
#预设
title('龟兔赛跑')
bgcolor(0.5, 0.5, 0.5)  # 背景
screensize(800,1000)  # 画布尺寸
#雪地
def snowfield():
    SCREEN_LENGTH = 1800
    SCREEN_WIDTH = 1000
    for i in range(150):
        pensize(randint(10, 18))
        x_zhou = randint(-SCREEN_LENGTH/2, SCREEN_LENGTH/2)#雪地的宽
        y_zhou = randint(-SCREEN_WIDTH / 2, -SCREEN_WIDTH / 2 + 100)#雪地的高
        pencolor('white')
        pu()
        goto(x_zhou, y_zhou)
        pd()
        seth(0)
        forward(randint(20, 50))
#草地
def ground():
    SCREEN_LENGTH = 1800
    SCREEN_WIDTH = 1000
    for i in range(100):
        pensize(randint(6, 12))
        x_zhou = randint(-SCREEN_LENGTH / 2,SCREEN_LENGTH / 2)#草地的宽
        y_zhou = randint(-SCREEN_WIDTH / 2, -SCREEN_WIDTH / 2 + 100)#草地的宽
        g = -y_zhou / 1000    # 颜色随y轴变
        pencolor(0, g, 0)
        pu()
        goto(x_zhou, y_zhou)
        pd()
        seth(0)
        left(randint(80, 100))
        forward(randint(10, 20))

#画白兔
def white_rabbit(x):
    RADIUS = 50
    ANGLE = 50
    B_X = 600 - x
    B_Y = -320
    hideturtle()
    speed(4)
    pensize(1)
    # 头部
    color('white')
    pu()
    goto(B_X, B_Y)
    pd()
    begin_fill()
    circle(RADIUS, 360)
    end_fill()
    # 耳朵
    pu()
    goto(RADIUS * sin(2 * ANGLE) + B_X, RADIUS * cos(2 * ANGLE) + RADIUS + B_Y)
    pd()
    seth(120)
    begin_fill()
    circle(-50, 60)
    circle(-10, 120)
    circle(-50, 55)
    pu()
    seth(0)
    forward(15)
    pd()
    seth(120)
    circle(-50, 55)
    circle(-10, 120)
    circle(-50, 62)
    end_fill()
    # 眼睛
    color('red')
    pu()
    seth(0)
    goto(RADIUS * sin(ANGLE) + B_X, RADIUS + B_Y)
    pd()
    begin_fill()
    circle(-5)
    pu()
    forward(2 * RADIUS * sin(ANGLE))
    pd()
    circle(5)
    end_fill()
    # 身体
    color('white')
    pu()
    seth(0)
    goto(RADIUS * sin(ANGLE) - 10 + B_X, 10 + B_Y)
    seth(-130)
    pd()
    begin_fill()
    circle(130, 30)  
    circle(12, 140)  
    circle(-160, 40)  
    circle(-50, 75)  
    circle(10, 140)  
    circle(100, 45)  
    # 尾巴
    seth(0)
    circle(10)
    # 背部
    seth(155)
    circle(160, 35)
    end_fill()
    # 前腿
    pu()
    goto(B_X, -42 + B_Y)
    pd()
    seth(-50)
    begin_fill()
    fd(25)
    circle(8, 110)
    fd(40)
    end_fill()
    # 后腿
    pu()
    goto(145 + B_X, -50 + B_Y)
    pd()
    seth(-85)
    begin_fill()
    fd(15)
    circle(-5, 150)
    fd(3)
    end_fill()

#乌龟
def m_turtle(y):
    B_X = 750 - y/2
    B_Y = -480
    #龟壳
    pensize(4)
    color('green')
    pu()
    goto(B_X, B_Y)
    pd()
    right(90)
    begin_fill()
    circle(-80, -180)
    end_fill()
    right(90)
    fd(160)
    right(90)
    circle(-80,-60)
    right(90)
    pencolor('black')
    fd(40)
    left(60)
    fd(40)
    back(40)
    right(120)
    fd(40)
    right(60)
    fd(40)
    back(40)
    left(120)
    fd(40)
    right(60)
    pu()
    fd(40)
    pd()
    pensize(1)
    #头
    color('green')
    begin_fill()
    fd(40)
    circle(-100,20)
    circle(-10,135)
    circle(-80,60) 
    end_fill()
    goto(B_X, B_Y)
    pu()
    goto(B_X-230, B_Y+10)
    pd()
    #脚
    color('black')
    begin_fill()
    circle(5,360)
    end_fill()
    pu()
    home()
    goto(B_X, B_Y)
    left(180)
    fd(30)
    pd()
    color('black')
    begin_fill()
    circle(10, -150)
    circle(18, -125)
    end_fill()
    pu()
    home()
    goto(B_X, B_Y)
    left(180)
    fd(130)
    pd()
    begin_fill()
    circle(10, 150)
    circle(18, 125)
    end_fill()
    pu()
    home()
    goto(B_X, B_Y)
    pd()
    #尾巴
    color('green')
    begin_fill()
    fd(15)
    circle(50,20)
    circle(5,135)
    circle(40,60)
    end_fill()

def draw():
    tracer(False)
    reset()
    hideturtle()
    speed(0)
    sleep(10)
    snowfield()
    ground()
    for i in range(0,2500,30):
        x = 0
        clear()
        snowfield()
        ground()
        pu()
        home()
        pd()
        m_turtle(i)
        if i<=900:
            pu()
            home()
            pd()
            white_rabbit(i)
        else:
            pu()
            home()
            pd()
            white_rabbit(900)
        update()
        sleep(0.2)
