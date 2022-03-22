'''
我们知道，type() 函数属于 Python 内置函数，通常用来查看某个变量的具体类型。其实，type() 函数还有一个更高级的用法，即创建一个自定义类型（也就是创建一个类）。

type() 函数的语法格式有 2 种，分别如下：
type(obj)
type(name, bases, dict)

以上这 2 种语法格式，各参数的含义及功能分别是：
第一种语法格式用来查看某个变量（类对象）的具体类型，obj 表示某个变量或者类对象。
第二种语法格式用来创建类，其中 name 表示类的名称；bases 表示一个元组，其中存储的是该类的父类；dict 表示一个字典，用于表示类内定义的属性或者方法。

'''


# 定义一个实例方法
def say(self):
    print("learn python")


# 使用type函数创建类 注意，Python 元组语法规定，当 (object,) 元组中只有一个元素时，最后的逗号（,）不能省略。
Clanguage = type('Clanguage', (object,), dict(say=say, name='c语言'))

# 创建一个对象
c = Clanguage()
c.say()
print(c.name)

# 可以看到，使用 type() 函数创建的类，和直接使用 class 定义的类并无差别。事实上，我们在使用 class 定义类时，Python 解释器底层依然是用 type() 来创建这个类

# # 定义一个实例方法
# def say(self):
#     print("我要学 Python！")
#
#
# # 使用 type() 函数创建类
# CLanguage = type("CLanguage", (object,), dict(say=say, name="C语言中文网"))
# # 创建一个 CLanguage 实例对象
# clangs = CLanguage()
# # 调用 say() 方法和 name 属性
# clangs.say()
# print(clangs.name)
