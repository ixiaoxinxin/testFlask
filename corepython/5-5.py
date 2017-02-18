# -*- coding: utf-8 -*-
#取余，取任意一个小于1美金的金额，然后计算可以换成多少枚1美分，5美分，10美分，25美分四中硬币？1美元=100美分
def meifen(num):
    num = num*100
    a25 = num // 25
    a10 = (num-a25*25)/10
    a5 = (num-a25*25-a10*10)/5
    a1 = (num-a25*25-a10*10-a5*5)/1
    return a25+a10+a5+a1

jine = float(raw_input("请输入一个美分数"))
print meifen(jine)
