class SingleTon(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_instance'):
            cls._instance = object.__new__(cls,*args,**kwargs)
        return cls._instance

class TestClass(SingleTon):
        a = 1
test1 = TestClass()
test2 = TestClass()
print test1.a,test2.a

test1.a = 2
print test1.a,test2.a
print id(test1),id(test2)


def SingleTon(cls, *args, **kwargs):
    instances = {}
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return _singleton

@SingleTon
class TestClass(object):
    a = 1
test1 = TestClass()
test2 = TestClass()
print test1.a,test2.a

test1.a = 2
print test1.a,test2.a
print id(test1),id(test2)








































