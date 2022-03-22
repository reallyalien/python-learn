'''
Python 中，通过使用描述符，可以让程序员在引用一个对象属性时自定义要完成的工作。

本质上看，描述符就是一个类，只不过它定义了另一个类中属性的访问方式。换句话说，一个类可以将属性管理全权委托给描述符类。
描述符是 Python 中复杂属性访问的基础，它在内部被用于实现 property、方法、类方法、静态方法和 super 类型。

描述符类基于以下 3 个特殊方法，换句话说，这 3 个方法组成了描述符协议：
__set__(self, obj, type=None)：在设置属性时将调用这一方法（本节后续用 setter 表示）；
__get__(self, obj, value)：在读取属性时将调用这一方法（本节后续用 getter 表示）；
__delete__(self, obj)：对属性调用 del 时将调用这一方法。
其中，实现了 setter 和 getter 方法的描述符类被称为数据描述符；反之，如果只实现了 getter 方法，则称为非数据描述符。

实际上，在每次查找属性时，描述符协议中的方法都由类对象的特殊方法 __getattribute__() 调用（注意不要和 __getattr__() 弄混）。
也就是说，每次使用类对象.属性（或者 getattr(类对象，属性值)）的调用方式时，都会隐式地调用 __getattribute__()，它会按照下列顺序查找该属性：
验证该属性是否为类实例对象的数据描述符；
如果不是，就查看该属性是否能在类实例对象的 __dict__ 中找到；
最后，查看该属性是否为类实例对象的非数据描述符。
'''


# 描述符类
class RevealAccess:
    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        print("Retrieving", self.name)
        return self.val

    def __set__(self, obj, val):
        print("updating", self.name)
        self.val = val


class MyClass:
    x = RevealAccess(10, "aaaaaaaaa")
    y = 5


m = MyClass()
print(type(m.x))
m.x = 20

print("====================================================")
print(m.x)
print(m.y)

# 从这个例子可以看到，如果一个类的某个属性有数据描述符，那么每次查找这个属性时，都会调用描述符的 __get__() 方法，并返回它的值；同样，每次在对该属性赋值时，也会调用 __set__() 方法。

# 注意，虽然上面例子中没有使用 __del__() 方法，但也很容易理解，当每次使用 del 类对象.属性（或者 delattr(类对象，属性)）语句时，都会调用该方法。

# 除了使用描述符类自定义类属性被调用时做的操作外，还可以使用 property() 函数或者 @property 装饰器，它们会在后续章节做详细介绍。
