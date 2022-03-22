'''
　问题2. 从上面 代码1 我们看到了，描述符的对象 x 其实是类 TestDesc  的类属性，那么可不可以把它变成实例属性呢？

　　　　答：我说了你不算，你说了也不算，解释器说了算，看看解释器怎么说的。
咦，为啥没打印 t.y 的信息呢？

　　　　因为没有访问 __get__() 方法啊，哈哈，那么为啥没有访问 __get__() 方法呢？（问题真多）

　　　　因为调用 t.y 时刻，首先会去调用TestDesc(即Owner）的 __getattribute__() 方法，该方法将 t.y 转化为TestDesc.__dict__['y'].__get__(t, TestDesc)，
但是呢，实际上 TestDesc 并没有 y这个属性，y 是属于实例对象的，所以，只能忽略了。

'''


class Desc(object):
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        print('get.........')
        print("name:", self.name)
        print('=' * 40)


class TestDesc(object):
    x = Desc('x')

    def __init__(self):
        self.y = Desc('y')


t = TestDesc()
t.x
