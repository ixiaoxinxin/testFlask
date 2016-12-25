def rightStrip(temStr,splitStr):
    endindex = temStr.rfind(splitStr)
    while endindex != -1 and endindex ==len(temStr) - 1:
        temStr = temStr[:endindex]
        endindex = temStr.rfind(splitStr)
    return temStr
def leftStrip(temStr,splitStr):
    startindex = temStr.find(splitStr)
    while startindex == 0:
        temStr = temStr[startindex+1:]
        startindex = temStr.find(splitStr)
    return  temStr

testStr  = '   hello   Python     '
print testStr
print rightStrip(testStr,' ')
print leftStrip(testStr,' ')


import this



















