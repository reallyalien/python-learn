class People(object):
    __slots__ = ('name', 'age')


def f(self):
    return 10


a = People()
a.name = 10
from types import MethodType

a.age = MethodType(f, a)
# a.age = f
# print(dir(a))
print(type(a.age))
print(a.age())


# 与类和实例无绑定关系的function都属于函数（function）；
# 与类和实例有绑定关系的function都属于方法（method）。
