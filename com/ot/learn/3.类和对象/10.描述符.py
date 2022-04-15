class Scope(object):
    def __init__(self, default=0):
        self._score = default

    def __set__(self, instance, value):
        self._score = value

    def __get__(self, instance, owner):
        print('__get__')
        return self._score

    def __del__(self):
        del self._score


class TestScope(object):
    math = Scope(100)

    def __init__(self, math):
        self.math = math

    def __getattribute__(self, item):
        print('__getattribute__')
        return object.__getattribute__(self, item)


# 描述符一般用在类属性的位置，而不是实例属性的位置，用在实例属性的位置就是一个对象，用在类的位置才可以调用__get__()方法
t = TestScope(1)
print(t.math)
t.math = 11
print(t.math)
