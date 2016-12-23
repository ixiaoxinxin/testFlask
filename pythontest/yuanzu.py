a = [('a', '1'), ('b', '2'),('c', '3')]
print a
b = sorted(a, key=lambda result: result[1],reverse=True)
print b