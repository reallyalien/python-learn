class Student(object):

    def __init__(self, math):
        self.__math = math

    @property
    def math(self):
        return self.__math

    @math.setter
    def math(self, math):
        self.__math = math


s = Student(1)
# 加了@property之后，方法就变成了属性，不能使用()来调用
print(s.math)

s.math = 10

print(s.math)
