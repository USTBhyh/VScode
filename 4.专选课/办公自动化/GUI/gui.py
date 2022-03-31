# -*- coding:utf-8 -*-
'''
@File    :   gui.py
@Time    :   2022/03/31 08:08:26
@Author  :   hyh
@Version :   1.0
@Contact :   1360895771@qq.com
@Desc    :   鼠标键盘自动化
'''
# here put the import lib
import pyautogui as ag
from pyautogui import hotkey

#鼠标
# ag.moveTo(100,200,duration=0.25)#移动到绝对坐标(x,y)
# ag.moveRel(10,20,duration=0.25)#相对坐标
# x,y = ag.position()#获得鼠标的位置

# #异常处理(通过CTRL+C停止)
# try:
#     pass
# except KeyboardInterrupt:
#     pass

# #鼠标点击
# ag.click(x,y,button="left")#x,y单击左键
# ag.doubleClick()
# ag.mouseDown()
# ag.mouseUp()
# #click = up + down

# #鼠标拖动
# ag.drag()
# ag.dragRel()
# #参数与moveTo相似

#截图
im = ag.screenshot()
im.save("capture.png")

#定位(局部图像)
ag.locateOnScreen("want.png")

#键盘
ag.typewrite("hello world")#一般按键
ag.typewrite(['a','b','left','X'])#特殊键,left:左方向键
ag.hotkey('ctrl','alt','shift','s')#按参数从左到右依次模拟按键，倒序模拟释放

ag.keyDown('shift')
ag.press('1')
ag.keyUp('shift')#相当于shift-1,即"!"键 
