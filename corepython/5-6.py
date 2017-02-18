# -*- coding: utf-8 -*-
def jisuan(N1,cz,N2):
    if cz == '+':
        return N1+N2
    if cz == '-':
        return N1-N2
    if cz == '*':
        return N1*N2
    if cz == '/':
        return N1/N2

if __name__=='__main__':
    ss = raw_input("input your expression:")
    if len(ss) == 3:
        print jisuan(float(ss[0]), ss[1], float(ss[2]))
    else:
        print jisuan(float(ss[0]), ss[1:3], float(ss[3]))
