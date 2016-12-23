class testcalss(object):
    def __new__(cls, *args, **kwargs):
        print '__new__'
        return object.__new__(cls,*args, **kwargs)

    def __init__(self,testname):
        print '__init__'
        self.testname = testname
print testcalss('josn').testname