class People(object):
    __slots__ = ('name', 'age')


def f():
    return 10


a = People()
a.name = 10
from types import MethodType

a.age = MethodType(f, a)

print(dir(a))
print(type(a.age))  # method

a.age()
