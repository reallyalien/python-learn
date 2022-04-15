# 实例变量指的是在任意类方法内部，以“self.变量名”的方式定义的变量，其特点是只作用于调用方法的对象。另外，实例变量只能通过对象名访问，无法通过类名访问。

class Clanguage:
    def __init__(self):
        self.name = "C语言中文网"
        self.add = "http://c.biancheng.net"

    # 下面定义了一个say实例方法
    def say(self):
        self.catalog = 13


a = Clanguage()
a.say()
# print(a.catalog)
# 前面讲过，通过类对象可以访问类变量，但无法修改类变量的值。这是因为，通过类对象修改类变量的值，不是在给“类变量赋值”，
# 而是定义新的实例变量。例如，在 CLanguage 类体外，添加如下程序：
# 显然，通过类对象是无法修改类变量的值的，本质其实是给 clang 对象新添加 name 和 add 这 2 个实例变量。
# 类中，实例变量和类变量可以同名，但这种情况下使用类对象将无法调用类变量，它会首选实例变量，这也是不推荐“类变量使用对象名调用”的原因。

a.money = 10
print(a.money)
