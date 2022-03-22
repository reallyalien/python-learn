class CLanguage:
    __slots__ = ('name', 'add', 'info')


# 下面定义了一个实例方法
def info(self):
    print("正在调用实例方法")


# 下面定义了一个类方法
@classmethod
def info2(cls):
    print("正在调用类方法")


# 下面定义个静态方法
@staticmethod
def info3():
    print("正在调用静态方法")


# 类可以动态添加以上 3 种方法，会影响所有实例对象
CLanguage.info = info
CLanguage.info2 = info2
CLanguage.info3 = info3

c = CLanguage()
c.info()
c.info2()
c.info3()

'''
庆幸的是，Python 提供了 __slots__ 属性，通过它可以避免用户频繁的给实例对象动态地添加属性或方法。
再次声明，__slots__ 只能限制为实例对象动态添加属性和方法，而无法限制动态地为类添加属性和方法。
'''

'''
__slots__ 属性值其实就是一个元组，只有其中指定的元素，才可以作为动态添加的属性或者方法的名称。举个例子：
class CLanguage:
    __slots__ = ('name','add','info')
可以看到， CLanguage 类中指定了 __slots__ 属性，这意味着，该类的实例对象仅限于动态添加 name、add、info 这 3 个属性以及 name()、add() 和 info() 这 3 个方法。
注意，对于动态添加的方法，__slots__ 限制的是其方法名，并不限制参数的个数.
使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
'''
