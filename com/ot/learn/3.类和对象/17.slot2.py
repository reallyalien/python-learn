class CLanguage:
    # __slots__ = ('name', 'add', 'info')
    __slots__ = ('name', 'add')


def info(self, name):
    print("正在调用实例方法", self.name)


c = CLanguage()
c.name = 19
c.info = info
print(c)

CLanguage.info = info

# 另外本节前面提到，__slots__ 属性限制的对象是类的实例对象，而不是类，因此下面的代码是合法的：
# 显然，__slots__ 属性只对当前所在的类起限制作用。
# 因此，如果子类也要限制外界为其实例对象动态地添加属性和方法，必须在子类中设置 __slots__ 属性。
# 注意，如果为子类也设置有 __slots__ 属性，那么子类实例对象允许动态添加的属性和方法，是子类中 __slots__ 属性和父类 __slots__ 属性的和。
