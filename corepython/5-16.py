# -*- coding: utf-8 -*-
#输出剩下的金额和当月支出
def Payment(cost, total):
    count = 0
    print ' Amount Remaining'
    print 'Pymt#   PaidBalance'
    print '-----   ------   --------'
    while True:
        print '%-2d   $%.2f  $%6.2f' % (count, total, cost)
        if cost - total >= 0:
            cost = cost - total
        else:
            if cost != 0:
                print '%-2d   $%.2f   $%6.2f' % (count + 1, cost, 0)
            break
        count += 1


if __name__ == '__main__':
    cost = input('Enter opening balance:')
    total = input('Enter monthly payment:')
    Payment(cost, total)