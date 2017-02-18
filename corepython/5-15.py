# -*- coding: utf-8 -*-
#最大公约数和最小公倍数
def gongyueshu(m, n):
    if m < n:
        min = m
    else:
        min = n


    for i in range(min, 0, -1):
        if m % i == 0 and n % i == 0:#最大公约数是能分别把两个数都除尽的数
            return i
        return 0


def gongbeishu(m, n):
    l = gongyueshu(m, n)
    return m * n / l #最小公倍数是两个数相乘除以最大公约数


if __name__ == '__main__':
    m = input("请输入第一个数：")
    n = input("请输入第二个数：")
    print '最大公约数：', gongyueshu(m, n)
    print '最小公倍数：', gongbeishu(m, n)