print(type(123) == int)
# 判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：
import types


def f():
    pass


print(type(f) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x * x) == types.LambdaType)
print(type(x for x in range(10)) == types.GeneratorType)
#
print(isinstance([1, 2, 3], list))

# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：

print(dir(abs))

# 类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。在Python中，如果你调用len()函数试图获取一个对象的长度，
# 实际上，在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价的：
# 我们自己写的类，如果也想用len(myObj)的话，就自己写一个__len__()方法：

print('=======================================================')


class MyDog(object):

    def __len__(self):
        return 100


a = MyDog()
print(len(a))
# 仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：

print(hasattr(a, 'x'))
print(getattr(a, 'x', 60))
setattr(a, 'x', 100)
print(getattr(a, 'x'))
# 请注意，在Python这类动态语言中，根据鸭子类型，有read()方法，不代表该fp对象就是一个文件流，它也可能是网络流，也可能是内存中的一个字节流，但只要read()方法返回的是有效的图像数据，就不影响读取图像的功能。
