# -*- coding: utf-8 -*-
#求出0~20之间所有偶数,奇数
x = range(0,21)
for i in x:
    if i % 2 == 0:
        print i
    if i % 2 != 0:
        print i