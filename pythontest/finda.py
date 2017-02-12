alist =[1,'d',4,7,22,877,34,'g','a','b']
try:
    alist.index('a')
    print 'Find it.'
except ValueError:
    print 'Not Found.'
