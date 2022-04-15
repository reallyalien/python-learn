class Scope(object):
    def __init__(self, default=0):
        self._score = default

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Score must be integer')
        if not 0 <= value <= 100:
            raise ValueError('Valid value must be in [0, 100]')
        self._score = value

    def __get__(self, instance, owner):
        print('__get__')
        return self._score

    def __del__(self):
        del self._score


class People(object):
    math = Scope(0)

    def __init__(self, math):
        self.math = math

    # def __getattribute__(self, item):
    #     print('__getattribute__')


p = People(1)
p.math
