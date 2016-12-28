import os
file = 'E:/1.txt'
if os.path.exists(file):
    os.remove(file)
else:
    print 'no such file:%s' % file