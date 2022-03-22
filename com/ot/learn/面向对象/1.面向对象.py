class Student(object):
    def __init__(self, name):
        self.__name = name


a = Student("小米")
# 私有变量还可以使用这种方式访问，但是不建议这样访问
print(a._Student__name)
print(a.__name)
