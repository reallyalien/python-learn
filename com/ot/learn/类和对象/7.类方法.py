'''
python 类方法和实例方法相似，它最少也要包含一个参数，只不过类方法中通常将其命名为 cls，Python 会自动将类本身绑定给 cls 参数（注意，绑定的不是类对象）。
也就是说，我们在调用类方法时，无需显式为 cls 参数传参。
和 self 一样，cls 参数的命名也不是规定的（可以随意命名），只是 Python 程序员约定俗称的习惯而已。

'''


class People:
    def __init__(self):
        pass

    def say(self):
        pass

    def eat(self):
        pass

    @classmethod
    def info(cls):
        print("正在调用类方法", cls)


People.info()
