from turtle import pencolor


class circle:
    '''Class definition for a circle...'''
#方法的第一个参数时专用的，一般用名字self
    def __init__(self,radius):#初始化函数
        self.radius = radius
    def getradius(self):
        return self.radius

#实例化
c1  =circle(10)#自动调用初始化函数
c1.getradius()#相当于circle.getradius(c1)

#继承 class 类名(被继承的类名):
class Characterlesscircle_son(circle):#平凡继承(无意义)
    pass
class DrawableCircle(circle):
    def __init__(self,radius,encolor):
        super().__init__(radius)#相当于变量表
        self.pencolor = pencolor
    def draw(self):
        pass