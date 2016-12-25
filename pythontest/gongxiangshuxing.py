class SingleTon(object):
    _state = {}
    def __new__(cls, *args, **kwargs):
        obj = object.__new__(cls,*args,**kwargs)
        obj.__dict__ = cls._state
        return obj

class TestClass(SingleTon):
        a = 1
test1 = TestClass()
test2 = TestClass()
print test1.a,test2.a

test1.a = 2
print test1.a,test2.a
print id(test1),id(test2)