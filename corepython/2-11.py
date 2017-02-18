# -*- coding: utf-8 -*-
while 1:
    print "1.取五个数的和"
    print "2.取五个数的平均值"
    print "X.退出"
    option = raw_input("请输入你的选择：")
    if option == '1':
        sum = 0
        for i in range(5):
            sum += int(raw_input("请输入1个数"))
        print sum
    if option == '2':
        a = [1,2,3,4,5]
        sum = 0
        for i in a:
            sum += i
        print float(sum)/5
    elif option == 'X' or option == 'x':
        break
    else:
        print "error"