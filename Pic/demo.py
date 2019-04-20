# -*- coding: utf-8 -*-
# @File  : demo.py
# @Author: 郭迎辉
# @Time  : 2019/3/25/0259:36
# @Desc  :
# from PIL import Image
# im = Image.open('C:\\Users\\Administrator\\Desktop\\2.jpg')# type:Image.Image
# # assert isinstance(im, Image.Image)
# im.show()
# rec = (100,100,400,400)
# region = im.rotate(45)
# # im2 = im.convert('L')#灰度化，由彩色变为黑白
# im2 = im.paste(region,rec)
# region.save('C:\\Users\\Administrator\\Desktop\\fenge4.jpg')
# region.show()
from skimage import io,data
from PIL import Image
img=Image.open("C:\\Users\\Administrator\\Desktop\\2.jpg")
img_array=img.load()
print(img_array[1,3,3])

