#!/usr/bin/env python
# encoding: utf-8

#author:jiao
#date:2015.12.20

"""
第 0001 题:使用 Python 如何生成 200 个激活码（或者优惠券）
NO.0001 generate 200 coupon code using Python

程序不仅在屏幕上打印出200个优惠码，还输出一份到couponList.txt文件中
not only print the code on screen, but save the code in couponList.txt

"""

import random,string

couponNum=200
couponLen=12
couponListSvae = file("couponList.txt","w")
for i in range(couponNum):
    couponList="".join(
            random.sample((string.letters.upper()+string.digits),couponLen))
    print(couponList)
    couponListSvae.write(couponList+"\n")

couponListSvae.close()
