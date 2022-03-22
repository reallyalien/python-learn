class people(object):
    __slots__ = ('b', 'a')
    pass


def f():
    print("----")


people.f = f
p1 = people()
p1.b = f
