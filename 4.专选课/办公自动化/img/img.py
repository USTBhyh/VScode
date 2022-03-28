# -*- coding:utf-8 -*-
'''
@File    :   img.py
@Time    :   2022/03/28 09:08:13
@Author  :   hyh
@Version :   1.0
@Contact :   1360895771@qq.com
@Desc    :   
'''
# here put the import lib
#import PIL  #Pillow库用PIL导入
from PIL import Image

img = Image.open("1.jpg")
print(img.size)
print(img.format)

img1 = Image.open('horse.jpg')
for i in range(2):
    for j in range(4):
        img1.paste(img1,(0+i*100,0+j*100))
img2 = Image.open("校徽.jpg")
img1.paste(img1,(img1.width-img2.width,img1.height-img2.height))
img1.save('eight_horse.jpg')