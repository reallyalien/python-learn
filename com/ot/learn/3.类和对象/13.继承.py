class Shape:
    def draw(self, content):
        print("画", content)


# 注意，如果该类没有显式指定继承自哪个类，则默认继承 object 类（object 类是 Python 中所有类的父类，
# 即要么是直接父类，要么是间接父类）。另外，Python 的继承是多继承机制（和 C++ 一样），即一个子类可以同时拥有多个直接父类。
# 括号里面可以书写多个父类
# 没错，子类拥有父类所有的属性和方法，即便该属性或方法是私有（private）的。
# 可以看到，当 Person 同时继承 People 类和 Animal 类时，People 类在前，因此如果 People 和 Animal 拥有同名的类方法，实际调用的是 People 类中的。
# 虽然 Python 在语法上支持多继承，但逼不得已，建议大家不要使用多继承。
class Form(Shape):
    def area(self):
        # ....
        print("此图形的面积为...")


class People:
    def __init__(self):
        self.name = None

    def say(self):
        print("我是一个人，名字是：", self.name)


class Animal:
    def display(self):
        print("人也是高级动物")


# 同时继承 People 和 Animal 类
# 其同时拥有 name 属性、say() 和 display() 方法
class Person(People, Animal):
    pass


zhangsan = Person()
zhangsan.name = "张三"
zhangsan.say()
zhangsan.display()
