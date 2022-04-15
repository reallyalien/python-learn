'''
无论是类属性还是类方法，都无法像普通变量或者函数那样，在类的外部直接使用它们。我们可以将类看做一个独立的空间，
则类属性其实就是在类体中定义的变量，类方法是在类体中定义的函数。

前面章节提到过，在类体中，根据变量定义的位置不同，以及定义的方式不同，类属性又可细分为以下 3 种类型：
类体中、所有函数之外：此范围定义的变量，称为类属性或类变量；
类体中，所有函数内部：以“self.变量名”的方式定义的变量，称为实例属性或实例变量；
类体中，所有函数内部：以“变量名=变量值”的方式定义obj的变量，称为局部变量。
不仅如此，类方法也可细分为实例方法、静态方法和类方法，后续章节会做详细介绍。

'''


class CLanguage:
    # 下面定义了2个类变量
    name = "C语言中文网"
    add = "http://c.biancheng.net"

    # 下面定义了一个say实例方法
    def say(self, content):
        print(content)


# 以看到，通过类名不仅可以调用类变量，也可以修改它的值。可以理解为静态变量
print(CLanguage.name)
print(CLanguage.add)
CLanguage.name = "aaa"
CLanguage.add = "bbb"
print(CLanguage.name)
print(CLanguage.add)
a = CLanguage()
b = CLanguage()
print(a)
a.name = "aaaaaaaaa"
print(a.name)
print(b.name)
print(CLanguage.name)
# 得一提的是，除了可以通过类名访问类变量之外，还可以动态地为类和对象添加类变量。
# 当然，也可以使用类对象来调用所属类中的类变量（此方式不推荐使用，原因后续会讲）。例如，在 CLanguage 类的外部，添加如下代码：
# 类变量为所有对象拥有，可以通过类名来修改类变量，但是通过对象来修改类变量，只能修改当前对象的属性，并不会影响其他对象的属性，
