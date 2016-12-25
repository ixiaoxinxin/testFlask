import re
temstr = 'be happy'
print  temstr.replace('happy','sad')
print '-----'
rex = r'(be|happy)'
print re.sub(rex,'happier',temstr)