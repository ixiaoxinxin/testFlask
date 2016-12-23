from operator import itemgetter
aa = {"a":"1","b":"2","d":'4',"c":'3'}
sort_aa = sorted(aa.items(),key=itemgetter(1))
print sort_aa