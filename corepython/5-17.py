# -*- coding: utf-8 -*-
# 生成一个有 N 个元素的由随机数 n 组成的列表, 其中 N 和 n 的取值范围分别为: (1 <
# N <= 100), (0 <= n <= 231 -1)。然后再随机从这个列表中取 N (1 <= N <= 100)个随机数
# 出来, 对它们排序,然后显示这个子集。
import random
if __name__=='__main__':
    N = random.randint(1,100)
    list = []
    for i in range(N):
        n = random.randint(0,2**31-1)
        list.append(n)
    list.sort()
    print list