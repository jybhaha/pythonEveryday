#!/usr/bin/env python
# encoding: utf-8

from PIL import Image, ImageDraw, ImageFont
"""
OS:UBUNTU14.04
This program use the fons of UBUNTU14 in the "usr/share/fonts/truetype/droid"
"""

def addNumToImg(fileName):
    img = Image.open(fileName)
    x, y=img.size
    #填写绝对路径
    ttf = ImageFont.truetype("/usr/share/fonts/truetype/droid/DroidSerif-Italic.ttf", size = x /5)
    draw = ImageDraw.Draw(img)

    draw.text((3*x/4,0), font=ttf,fill='red',text='99')
    img.save("myPhoto2.jpg")

if __name__ == '__main__':
    addNumToImg('myPhoto.jpg')
