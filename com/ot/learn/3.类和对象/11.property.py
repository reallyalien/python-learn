'''

前面章节中，我们一直在用“类对象.属性”的方式访问类中定义的属性，其实这种做法是欠妥的，因为它破坏了类的封装原则。正常情况下，类包含的属性应该是隐藏的，只允许通过类提供的方法来间接实现对类属性的访问和操作。

因此，在不破坏类封装原则的基础上，为了能够有效操作类中的属性，类中应包含读（或写）类属性的多个 getter（或 setter）方法，这样就可以通过“类对象.方法(参数)”的方式操作属性
'''


class People:
    def __init__(self, name):
        self.__name = name

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def del_name(self):
        self.__name = 'xxxx'

    name = property(fget=get_name)


clang = People("C语言中文网")
# print(clang.__name) name为私有变量，在类的外部，不可以直接调用，只能通过方法来访问
print(clang.get_name())
print('========================================================')

print(clang.set_name('aaaaa'))

'''
庆幸的是，Python 中提供了 property() 5.函数，可以实现在不破坏类封装原则的前提下，让开发者依旧使用“类对象.属性”的方式操作类中的属性。

property() 函数的基本使用格式如下：
属性名=property(fget=None, fset=None, fdel=None, doc=None)

其中，fget 参数用于指定获取该属性值的类方法，fset 参数用于指定设置该属性值的方法，fdel 参数用于指定删除该属性值的方法，最后的 doc 是一个文档字符串，用于说明此函数的作用。
注意，在使用 property() 函数时，以上 4 个参数可以仅指定第 1 个、或者前 2 个、或者前 3 个，当前也可以全部指定。也就是说，property() 函数中参数的指定并不是完全随意的。
'''

'''
注意，在此程序中，由于 getname() 方法中需要返回 name 属性，如果使用 self.name 的话，其本身又被调用 getname()，这将会先入无限死循环。
为了避免这种情况的出现，程序中的 name 属性必须设置为私有属性，即使用 __name（前面有 2 个下划线）。

同理，还可以像如下这样使用 property() 5.函数：
纯文本复制
name = property(getname)    # name 属性可读，不可写，也不能删除
name = property(getname, setname,delname)    #name属性可读、可写、也可删除，就是没有说明文档

'''
