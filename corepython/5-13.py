# -*- coding: utf-8 -*-
# 转换。写一个函数把由小时和分钟表示的时间转换为只用分钟表示的时间。
#思路：写个函数，将小时拆分用分钟表示，在

def test(h, m):
    min = h * 60 + m
    return min


#while True:
h = input("请输入小时：")
m = input("请输入分钟：")
if (h < 23 and h > -1) and (m < 60 and m > -1):
    print 'The time is %d minuters' % test(h, m)
else:
    print 'input error'